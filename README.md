# Mengke Li's Academic Homepage

This repository hosts my personal academic website built with Jekyll and deployed via GitHub Pages.

## Website

- Homepage: https://keke921.github.io/
- Chinese homepage: https://keke921.github.io/about_cn/

## Main Sections

- `News`: recent updates and announcements
- `Publications`: selected publications and full publication list
- `Funds`: funded projects
- `Teaching`: teaching activities and course information
- `Blog Posts`: research/activity posts
- `Contact`: office, email, profiles, and social QR code

## Repository Structure

- `_pages/`: static pages (about, publications, funds, contact, etc.)
- `_posts/`: blog post entries
- `_teaching/`: teaching entries
- `_includes/`: reusable HTML components
- `_data/`: site data, including navigation
- `assets/css/custom-theme.css`: custom site styles
- `assets/images/`: image assets (including contact QR code)

## Local Development

Run locally:

1. Install dependencies:
   - `bundle install`
2. Start local server:
   - `bundle exec jekyll serve --host 127.0.0.1 --port 4000 --config _config.yml,_config_dev.yml`
3. Open:
   - `http://127.0.0.1:4000/`

## Content Update Notes

- Add a news item:
  - Update `_pages/news.md`
  - Optionally sync highlights in `_pages/about.md` and `_pages/about_cn.md`
- Add/update a publication:
  - Update `_pages/publications.md`
- Add a blog post:
  - Add a new markdown file under `_posts/`
- Add teaching information:
  - Add a new markdown file under `_teaching/`
- Update contact information:
  - Edit `_pages/markdown.md`

## Contact

- Email: `mengkeli@szu.edu.cn`
- Google Scholar: `https://scholar.google.com/citations?user=0N26QgMAAAAJ&hl=zh-CN`
- DBLP: `https://dblp.org/pid/67/6597-1.html`
