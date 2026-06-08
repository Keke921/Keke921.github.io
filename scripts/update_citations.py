#!/usr/bin/env python3
"""Update Google Scholar citation counts for publications listed on the site."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_PAGE = ROOT / "_pages" / "publications.md"
CITATIONS_FILE = ROOT / "_data" / "citations.yml"
SCHOLAR_AUTHOR_ID = "0N26QgMAAAAJ"
TITLE_MATCH_THRESHOLD = 0.82

ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)
OPENREVIEW_RE = re.compile(r"openreview\.net/(?:pdf|forum)\?id=([^\"&\s]+)", re.I)
IEEE_RE = re.compile(r"ieeexplore\.ieee\.org/abstract/document/(\d+)", re.I)
VENUE_TITLE_RE = re.compile(
    r"<span class=\"venue-tag\">[^<]+</span>\s*([^,<]+)",
    re.I,
)
H3_TITLE_RE = re.compile(r"<h3>([^<]+)", re.I)
LIST_TITLE_RE = re.compile(r"^\s*-\s+(.+?),", re.M)
NEXT_VENUE_ITEM_RE = re.compile(r"\n- <span class=\"venue-tag\">")
NEXT_HIGHLIGHT_ITEM_RE = re.compile(r"(?=<li class=\"pub-highlight-card\">)")
DISTINCTIVE_STOPWORDS = {
    "learning",
    "visual",
    "recognition",
    "long",
    "tailed",
    "for",
    "with",
    "via",
    "and",
    "the",
    "from",
}


def normalize_title(title: str) -> str:
    text = title.lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_ids_from_href(href: str) -> dict[str, str]:
    ids: dict[str, str] = {}
    if match := ARXIV_RE.search(href):
        ids["arxiv"] = match.group(1)
    if match := OPENREVIEW_RE.search(href):
        ids["openreview"] = match.group(1)
    if match := IEEE_RE.search(href):
        ids["doi"] = f"10.1109/{match.group(1)}"
        ids["ieee"] = match.group(1)
    return ids


def parse_publications_page(path: Path) -> list[dict]:
    content = path.read_text(encoding="utf-8")
    papers: list[dict] = []
    seen: set[str] = set()

    def add_paper(title: str, ids: dict[str, str]) -> None:
        title = re.sub(r"\s+", " ", title).strip(" .")
        if not title:
            return
        key = ids.get("arxiv") or ids.get("openreview") or ids.get("ieee") or normalize_title(title)
        if key in seen:
            return
        seen.add(key)
        papers.append(
            {
                "id": key,
                "title": title,
                "title_norm": normalize_title(title),
                "arxiv": ids.get("arxiv"),
                "openreview": ids.get("openreview"),
                "ieee": ids.get("ieee"),
                "citations": None,
                "scholar_url": None,
            }
        )

    for block in re.split(r"(?=<li class=\"pub-highlight-card\">)", content):
        if "pub-highlight-card" not in block:
            continue
        block = block.split("</li>", maxsplit=1)[0]
        title_match = H3_TITLE_RE.search(block)
        if not title_match:
            continue
        title = title_match.group(1).strip()
        ids: dict[str, str] = {}
        for href in re.findall(r'href="([^"]+)"', block):
            ids.update(extract_ids_from_href(href))
        add_paper(title, ids)

    for block in re.split(r"(?=- <span class=\"venue-tag\">)", content):
        if "venue-tag" not in block:
            continue
        block = NEXT_VENUE_ITEM_RE.split(block, maxsplit=1)[0]
        title_match = VENUE_TITLE_RE.search(block)
        if not title_match:
            continue
        title = title_match.group(1).strip()
        ids = {}
        for href in re.findall(r'href="([^"]+)"', block):
            ids.update(extract_ids_from_href(href))
        add_paper(title, ids)

    preprints_match = re.search(r"## Preprints\s*(.*?)(?=\n## |\Z)", content, re.S)
    if preprints_match:
        preprints_section = preprints_match.group(1)
        for match in LIST_TITLE_RE.finditer(preprints_section):
            title = match.group(1).strip()
            if title.startswith("<span"):
                continue
            block_start = match.start()
            block = preprints_section[block_start : block_start + 800]
            ids = {}
            for href in re.findall(r'href="([^"]+)"', block):
                ids.update(extract_ids_from_href(href))
            add_paper(title, ids)

    return papers


def load_citations(path: Path) -> dict:
    if not path.exists():
        return {
            "scholar_author_id": SCHOLAR_AUTHOR_ID,
            "updated_at": None,
            "papers": [],
        }
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {"papers": []}


def save_citations(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)


def merge_registry(existing: dict, parsed: list[dict]) -> dict:
    by_id = {paper["id"]: paper for paper in existing.get("papers", []) if paper.get("id")}
    merged: list[dict] = []

    for paper in parsed:
        current = by_id.get(paper["id"], {})
        merged.append(
            {
                "id": paper["id"],
                "title": paper["title"],
                "title_norm": paper["title_norm"],
                "arxiv": paper.get("arxiv"),
                "openreview": paper.get("openreview"),
                "ieee": paper.get("ieee"),
                "citations": current.get("citations"),
                "scholar_url": current.get("scholar_url"),
                "scholar_title": current.get("scholar_title"),
            }
        )

    existing_ids = {paper["id"] for paper in merged}
    for paper_id, paper in by_id.items():
        if paper_id not in existing_ids:
            merged.append(paper)

    existing["papers"] = merged
    existing["scholar_author_id"] = SCHOLAR_AUTHOR_ID
    return existing


def fetch_scholar_publications(author_id: str) -> list[dict]:
    try:
        from scholarly import scholarly
    except ImportError as exc:
        raise SystemExit("Missing dependency: pip install -r scripts/requirements-citations.txt") from exc

    print(f"Fetching Google Scholar profile: {author_id}")
    author = scholarly.search_author_id(author_id)
    author = scholarly.fill(author, sections=["basics", "publications"])

    publications: list[dict] = []
    for index, pub in enumerate(author.get("publications", []), start=1):
        try:
            filled = scholarly.fill(pub)
        except Exception as error:  # noqa: BLE001 - scholarly raises varied errors
            print(f"  skip publication {index}: {error}")
            continue

        bib = filled.get("bib", {})
        title = bib.get("title", "").strip()
        if not title:
            continue

        publications.append(
            {
                "title": title,
                "title_norm": normalize_title(title),
                "citations": filled.get("num_citations", 0) or 0,
                "scholar_url": filled.get("pub_url"),
                "arxiv": None,
            }
        )

        if index % 5 == 0:
            time.sleep(2)

    print(f"Fetched {len(publications)} publications from Google Scholar")
    return publications


def title_match_score(target: str, candidate: str) -> float:
    score = difflib.SequenceMatcher(None, target, candidate).ratio()
    target_tokens = set(target.split())
    candidate_tokens = set(candidate.split())
    distinctive = [
        token
        for token in target_tokens
        if len(token) > 3 and token not in DISTINCTIVE_STOPWORDS
    ]
    missing = sum(1 for token in distinctive if token not in candidate_tokens)
    return score - (0.1 * missing)


def best_title_match(target: str, candidates: list[dict]) -> dict | None:
    best: dict | None = None
    best_score = 0.0
    for candidate in candidates:
        score = title_match_score(target, candidate["title_norm"])
        if score > best_score:
            best_score = score
            best = candidate
    if best_score >= TITLE_MATCH_THRESHOLD:
        return best
    return None


def update_counts(data: dict, scholar_pubs: list[dict]) -> tuple[int, int]:
    matched = 0
    for paper in data.get("papers", []):
        scholar_pub = None
        title_norm = paper.get("title_norm") or normalize_title(paper.get("title", ""))
        override_title = paper.get("scholar_title")
        if override_title:
            override_norm = normalize_title(override_title)
            for candidate in scholar_pubs:
                if candidate["title_norm"] == override_norm:
                    scholar_pub = candidate
                    break
            if scholar_pub is None:
                scholar_pub = best_title_match(override_norm, scholar_pubs)

        if scholar_pub is None:
            for candidate in scholar_pubs:
                if candidate["title_norm"] == title_norm:
                    scholar_pub = candidate
                    break

        if scholar_pub is None:
            scholar_pub = best_title_match(title_norm, scholar_pubs)

        if scholar_pub is None:
            continue

        paper["citations"] = scholar_pub["citations"]
        if scholar_pub.get("scholar_url"):
            paper["scholar_url"] = scholar_pub["scholar_url"]
        matched += 1

    return matched, len(data.get("papers", []))


def bootstrap() -> dict:
    if not PUBLICATIONS_PAGE.exists():
        raise SystemExit(f"Publications page not found: {PUBLICATIONS_PAGE}")
    parsed = parse_publications_page(PUBLICATIONS_PAGE)
    data = merge_registry(load_citations(CITATIONS_FILE), parsed)
    save_citations(CITATIONS_FILE, data)
    print(f"Bootstrapped {len(data['papers'])} papers into {CITATIONS_FILE}")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bootstrap",
        action="store_true",
        help="Parse _pages/publications.md and refresh the paper registry without fetching Scholar.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and match citations but do not write _data/citations.yml.",
    )
    args = parser.parse_args()

    if args.bootstrap:
        bootstrap()
        return 0

    data = bootstrap()
    try:
        scholar_pubs = fetch_scholar_publications(data.get("scholar_author_id", SCHOLAR_AUTHOR_ID))
    except Exception as error:  # noqa: BLE001
        print(f"Scholar fetch failed: {error}")
        return 1

    matched, total = update_counts(data, scholar_pubs)
    data["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["matched_count"] = matched
    data["registry_count"] = total

    print(f"Matched {matched}/{total} site papers to Google Scholar entries")

    if args.dry_run:
        for paper in data["papers"]:
            cite = paper.get("citations")
            print(f"  [{cite if cite is not None else '-'}] {paper['title'][:70]}")
        return 0

    save_citations(CITATIONS_FILE, data)
    print(f"Wrote citation counts to {CITATIONS_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
