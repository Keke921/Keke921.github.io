---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
  .venue-tag {
    display: inline-block !important;
    background: #4f6fd8 !important;
    color: #ffffff !important;
    border: 1px solid #3f60cf !important;
    border-radius: 0.38rem !important;
    padding: 0.05rem 0.45rem !important;
    margin-right: 0.32rem !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    line-height: 1.2 !important;
  }

  .ccf-tag {
    display: inline-block !important;
    border-radius: 0.36rem !important;
    padding: 0.03rem 0.42rem !important;
    margin: 0 0.2rem !important;
    font-size: 0.73rem !important;
    font-weight: 700 !important;
    border: 1px solid transparent !important;
    line-height: 1.25 !important;
  }

  .ccf-tag.ccf-a {
    background: #ffe6e6 !important;
    border-color: #ffb4b4 !important;
    color: #9f1f1f !important;
  }

  .ccf-tag.ccf-b {
    background: #fff1dd !important;
    border-color: #ffd49d !important;
    color: #945900 !important;
  }

  .ccf-tag.ccf-c {
    background: #e8f7ea !important;
    border-color: #bde6c5 !important;
    color: #1f6f36 !important;
  }

  .page__content .venue-tag {
    display: inline-block !important;
    background: #4f6fd8 !important;
    color: #ffffff !important;
    border: 1px solid #3f60cf !important;
    border-radius: 0.38rem !important;
    padding: 0.05rem 0.45rem !important;
    margin-right: 0.32rem !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    line-height: 1.2 !important;
  }

  .page__content .ccf-tag {
    display: inline-block !important;
    border-radius: 0.36rem !important;
    padding: 0.03rem 0.42rem !important;
    margin: 0 0.2rem !important;
    font-size: 0.73rem !important;
    font-weight: 700 !important;
    border: 1px solid transparent !important;
    line-height: 1.25 !important;
  }

  .page__content .ccf-tag.ccf-a {
    background: #ffe6e6 !important;
    border-color: #ffb4b4 !important;
    color: #9f1f1f !important;
  }

  .page__content .ccf-tag.ccf-b {
    background: #fff1dd !important;
    border-color: #ffd49d !important;
    color: #945900 !important;
  }

  .page__content .ccf-tag.ccf-c {
    background: #e8f7ea !important;
    border-color: #bde6c5 !important;
    color: #1f6f36 !important;
  }

  .page__content .pub-year-group a,
  .page__content .selected-pubs-list a {
    display: inline-block !important;
    background: linear-gradient(135deg, #2f79d1 0%, #4a90e2 100%) !important;
    color: #ffffff !important;
    border: 1px solid #2469bb !important;
    border-radius: 999px !important;
    padding: 0.05rem 0.56rem !important;
    margin-right: 0.26rem !important;
    margin-top: 0.12rem !important;
    text-decoration: none !important;
    font-size: 0.79rem !important;
    font-weight: 700 !important;
    line-height: 1.18 !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 1px 2px rgba(24, 61, 110, 0.16) !important;
    transition: all 0.18s ease !important;
  }

  .page__content .pub-year-group a:hover,
  .page__content .selected-pubs-list a:hover {
    background: linear-gradient(135deg, #245fab 0%, #3c7fd0 100%) !important;
    border-color: #1b5497 !important;
    color: #ffffff !important;
    transform: translateY(-1px);
    box-shadow: 0 3px 8px rgba(24, 61, 110, 0.22) !important;
  }

  .page__content .pub-year-group a[href*="arxiv"],
  .page__content .selected-pubs-list a[href*="arxiv"] {
    background: linear-gradient(135deg, #6a4bc9 0%, #8365df 100%) !important;
    border-color: #5b3fb8 !important;
  }

  .page__content .pub-year-group a[href*="github"],
  .page__content .selected-pubs-list a[href*="github"],
  .page__content .pub-year-group a[href*="code"],
  .page__content .selected-pubs-list a[href*="code"] {
    background: linear-gradient(135deg, #1f7a64 0%, #2e9b7f 100%) !important;
    border-color: #176b57 !important;
  }

  .page__content .pub-year-group a[href*="openreview"],
  .page__content .selected-pubs-list a[href*="openreview"],
  .page__content .pub-year-group a[href*=".pdf"],
  .page__content .selected-pubs-list a[href*=".pdf"] {
    background: linear-gradient(135deg, #cc5b2e 0%, #e0783f 100%) !important;
    border-color: #b44b23 !important;
  }

  .page__content .pub-year-group a[href*="project"],
  .page__content .selected-pubs-list a[href*="project"] {
    background: linear-gradient(135deg, #1f73a7 0%, #2f8fc9 100%) !important;
    border-color: #1b6390 !important;
  }

  .page__content a.pub-link-arxiv {
    background: linear-gradient(135deg, #6a4bc9 0%, #8365df 100%) !important;
    border-color: #5b3fb8 !important;
  }

  .page__content a.pub-link-code {
    background: linear-gradient(135deg, #1f7a64 0%, #2e9b7f 100%) !important;
    border-color: #176b57 !important;
  }

  .page__content a.pub-link-paper {
    background: linear-gradient(135deg, #cc5b2e 0%, #e0783f 100%) !important;
    border-color: #b44b23 !important;
  }

  .page__content a.pub-link-project {
    background: linear-gradient(135deg, #1f73a7 0%, #2f8fc9 100%) !important;
    border-color: #1b6390 !important;
  }

  /* Hard fallback: style by href keywords to avoid plain blue underlined links */
  .page__content a[href*="arxiv"],
  .page__content a[href*="openreview"],
  .page__content a[href*=".pdf"],
  .page__content a[href*="github"],
  .page__content a[href*="project"],
  .page__content a[href*="ieeexplore"],
  .page__content a[href*="drive.google.com"] {
    display: inline-block !important;
    padding: 0.07rem 0.58rem !important;
    margin: 0.08rem 0.24rem 0.08rem 0 !important;
    border-radius: 999px !important;
    text-decoration: none !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    line-height: 1.18 !important;
    color: #ffffff !important;
    border: 1px solid transparent !important;
    box-shadow: 0 1px 2px rgba(20, 40, 70, 0.16) !important;
    vertical-align: baseline !important;
  }

  .page__content a[href*="arxiv"] {
    background: #6b50c9 !important;
    border-color: #5b43ad !important;
  }

  .page__content a[href*="github"] {
    background: #238264 !important;
    border-color: #1d6f55 !important;
  }

  .page__content a[href*="project"] {
    background: #1f76a9 !important;
    border-color: #1a648f !important;
  }

  .page__content a[href*="openreview"],
  .page__content a[href*=".pdf"],
  .page__content a[href*="ieeexplore"],
  .page__content a[href*="drive.google.com"] {
    background: #cf6535 !important;
    border-color: #b9582d !important;
  }

  .page__content a[href*="arxiv"]:hover,
  .page__content a[href*="openreview"]:hover,
  .page__content a[href*=".pdf"]:hover,
  .page__content a[href*="github"]:hover,
  .page__content a[href*="project"]:hover,
  .page__content a[href*="ieeexplore"]:hover,
  .page__content a[href*="drive.google.com"]:hover {
    filter: brightness(0.93) !important;
    transform: translateY(-1px);
    color: #ffffff !important;
    text-decoration: none !important;
  }
</style>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".pub-year-group a, .selected-pubs-list a");
    links.forEach(function (a) {
      const label = (a.textContent || "").trim().toLowerCase();
      a.classList.remove("pub-link-arxiv", "pub-link-code", "pub-link-paper", "pub-link-project");
      if (label.includes("arxiv")) {
        a.classList.add("pub-link-arxiv");
      } else if (label.includes("code")) {
        a.classList.add("pub-link-code");
      } else if (label.includes("project")) {
        a.classList.add("pub-link-project");
      } else if (label.includes("paper")) {
        a.classList.add("pub-link-paper");
      }
    });
  });
</script>

<div class="home-intro">
You can also find my articles on my <a href="https://scholar.google.com/citations?user=0N26QgMAAAAJ&hl=zh-CN" target="_blank" rel="noopener">Google Scholar profile</a> and <a href="https://dblp.org/pid/67/6597-1.html" target="_blank" rel="noopener">DBLP</a>.
</div>

## 🌟 Selected Publications
<ul class="selected-pubs-list">
  <li class="pub-highlight-card">
    <div class="pub-badge">ICML'25</div>
    <div class="pub-topics"><span>SAR</span><span>Recognition</span></div>
    <h3>Gamma Distribution PCA-Enhanced Feature Learning for Angle-Robust SAR Target Recognition <a class="pub-link-paper" href="https://openreview.net/pdf?id=si1iynl5y7" target="_blank" rel="noopener">[paper]</a></h3>
    <p>C. Zhang, P. Zhang<span class="corr-icon">✉</span>, M Li<span class="corr-icon">✉</span>. </p>
  </li>
  <li class="pub-highlight-card">
    <div class="pub-badge">NeurIPS'24</div>
    <div class="pub-topics"><span>Long-tail</span><span>Prompt Tuning</span></div>
    <h3>Improving Visual Prompt Tuning by Gaussian Neighborhood Minimization for Long-Tailed Visual Recognition <a class="pub-link-paper" href="https://arxiv.org/pdf/2410.21042" target="_blank" rel="noopener">[paper]</a></h3>
    <p>M Li, Y Liu, Y Lu, Y Zhang, Y Cheung, H Huang<span class="corr-icon">✉</span>.</p>
  </li>
  <li class="pub-highlight-card">
    <div class="pub-badge">AAAI'24</div>
    <div class="pub-topics"><span>Long-tail</span><span>Feature Fusion</span></div>
    <h3>Feature Fusion from Head to Tail for Long-Tailed Visual Recognition <a class="pub-link-paper" href="https://arxiv.org/abs/2306.06963" target="_blank" rel="noopener">[paper]</a> <a class="pub-link-code" href="https://github.com/Keke921/H2T" target="_blank" rel="noopener">[code]</a></h3>
    <p>M Li, Z Hu, Y Lu, W Lan, Y Cheung, H Huang<span class="corr-icon">✉</span>.</p>
  </li>
  <li class="pub-highlight-card">
    <div class="pub-badge">TPAMI'23</div>
    <div class="pub-topics"><span>Long-tail</span><span>Logit adjustment</span></div>
    <h3>Key point sensitive loss for long-tailed visual recognition <a class="pub-link-paper" href="https://drive.google.com/file/d/1gOJDHBJ_M7RmU6Iw2p6uXIyo8pNgVMrv/view?pli=1" target="_blank" rel="noopener">[paper]</a></h3>
    <p>M Li, YM Cheung<span class="corr-icon">✉</span>, Z Hu.</p>
  </li>
  <li class="pub-highlight-card">
    <div class="pub-badge">CVPR'22</div>
    <div class="pub-topics"><span>Long-tail</span><span>Logit adjustment</span></div>
    <h3>Long-tailed visual recognition via gaussian clouded logit adjustment <a class="pub-link-paper" href="https://openaccess.thecvf.com/content/CVPR2022/papers/Li_Long-Tailed_Visual_Recognition_via_Gaussian_Clouded_Logit_Adjustment_CVPR_2022_paper.pdf" target="_blank" rel="noopener">[paper]</a></h3>
    <p>M Li, YM Cheung<span class="corr-icon">✉</span>, Y Lu.</p>
  </li>
</ul>

## Preprints
- Long-Tailed Visual Recognition via Permutation-Invariant Head-to-Tail Feature Fusion,<br>
**Mengke Li**, Zhikai Hu, Yang Lu, Weichao Lan, Yiu-ming Cheung, Hui Huang<span class="corr-icon">✉</span>, <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/pdf/2506.00625" target="_blank" rel="noopener">arxiv</a>.

## 🎤 Conference
<details class="pub-year-group" open markdown="1">
  <summary>2025–2024</summary>

- <span class="venue-tag">ICML’25</span> Gamma Distribution PCA-Enhanced Feature Learning for Angle-Robust SAR Target Recognition,<br>
  Chong Zhang, Peng Zhang<span class="corr-icon">✉</span>, **Mengke Li** <span class="corr-icon">✉</span><br>
  _Forty-second International Conference on Machine Learning (ICML 2025)_, Canada – May 1, 2025. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-paper" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#cf6535;border:1px solid #b9582d;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://openreview.net/pdf?id=si1iynl5y7" target="_blank" rel="noopener">paper</a>

- <span class="venue-tag">AAAI’25</span> Asynchronous Federated Clustering with Unknown Number of Clusters,<br>
  Yunfan Zhang, Yiqun Zhang<span class="corr-icon">✉</span>, Yang Lu, **Mengke Li**, Xi Chen, Yiu-ming Cheung<br>
  _Association for the Advancement of Artificial Intelligence_, Philadelphia, Pennsylvania, USA, Feb 25 – Mar 4, 2024. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/pdf/2412.20341" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#238264;border:1px solid #1d6f55;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://github.com/Yunfan-Zhang/AFCL" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">NeurIPS’24</span> Improving Visual Prompt Tuning by Gaussian Neighborhood Minimization for Long-Tailed Visual Recognition,<br>
  **Mengke Li**, Ye Liu, Yang Lu, Yiqun Zhang, Yiu-ming Cheung, Hui Huang<span class="corr-icon">✉</span><br>
  _Advances in Neural Information Processing Systems_, Vancouver, Canada, December 10-15, 2024. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/pdf/2410.21042" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-project" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#1f76a9;border:1px solid #1a648f;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://vcc.tech/research/2024/GNM-PT" target="_blank" rel="noopener">project</a>

- <span class="venue-tag">ECAI’24</span> Dynamically Anchored Prompting for Task-Imbalanced Continual Learning,<br>
  **Mengke Li**, Da Li, Guoqing Yang, Yiu-ming Cheung, Hui Huang<span class="corr-icon">✉</span><br>
  _European Conference on Artificial Intelligence_, Santiago de Compostela, Spanish, October 19-24, 2024. <span class="ccf-tag ccf-b">CCF-B</span> <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/abs/2407.13200" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-project" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#1f76a9;border:1px solid #1a648f;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://vcc.tech/research/2024/PointFormer" target="_blank" rel="noopener">project</a>

- <span class="venue-tag">ECAI’24</span> Learning Order Forest for Qualitative-Attribute Data Clustering,<br>
  Mingjie Zhao, Sen Feng, Yiqun Zhang<span class="corr-icon">✉</span>, **Mengke Li**, Yang Lu, Yiu-Ming Cheung<br>
  _European Conference on Artificial Intelligence_, Santiago de Compostela, Spanish, October 19-24, 2024. <span class="ccf-tag ccf-b">CCF-B</span>

- <span class="venue-tag">IJCAI’24</span> Dynamically Anchored Prompting for Task-Imbalanced Continual Learning,<br>
  Chenxing Hong, Yan Jin, Zhiqi Kang, Yizhou Chen, **Mengke Li**, Yang Lu<span class="corr-icon">✉</span> and Hanzi Wang<br>
  _International Joint Conference on Artificial Intelligence_, Jeju, Korea, August 3-9, 2024. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/abs/2404.14721" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#238264;border:1px solid #1d6f55;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://github.com/chenxing6666/DAP" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">ICASSP'24</span> Key Points Centered Sparse Hashing for Cross-Modal Retrieval,<br>
  Zhikai Hu, Yiu-ming Cheung<span class="corr-icon">✉</span>, **Mengke Li**, Weichao Lan, DongLin Zhang,<br>
  _IEEE International Conference on Acoustics, Speech and Signal Processing_, Seoul, Korea, April 14-19, 2024. <span class="ccf-tag ccf-b">CCF-B</span>

- <span class="venue-tag">AAAI'24</span> Feature Fusion from Head to Tail for Long-Tailed Visual Recognition,<br>
  **Mengke Li**, Zhikai Hu, Yang Lu, Weichao Lan, Yiu-ming Cheung, and Hui Huang<span class="corr-icon">✉</span>,<br>
  _AAAI Conference on Artificial Intelligence_, vol. 38, no. 12, pp.13581-13589, Vancouver, Canada, February 20–27, 2024. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/abs/2306.06963" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#238264;border:1px solid #1d6f55;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://github.com/Keke921/H2T" target="_blank" rel="noopener">code</a>
</details>

<details class="pub-year-group" markdown="1">
  <summary>2023 and Earlier</summary>

- <span class="venue-tag">CVPR'23</span> Long-Tailed Visual Recognition via Self-Heterogeneous Integration with Knowledge Excavation,<br>
  Yan Jin, **Mengke Li**, Yang Lu<span class="corr-icon">✉</span>, Yiu-ming Cheung, and Hanzi Wang,<br>
  _IEEE/CVF Conference on Computer Vision and Pattern Recognition_, Vancouver, Canada, June 18–22, 2023. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-arxiv" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#6b50c9;border:1px solid #5b43ad;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://arxiv.org/abs/2304.01279" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" style="display:inline-block;padding:0.07rem 0.58rem;margin:0.08rem 0.24rem 0.08rem 0;border-radius:999px;text-decoration:none;font-size:0.78rem;font-weight:700;line-height:1.18;color:#fff;background:#238264;border:1px solid #1d6f55;box-shadow:0 1px 2px rgba(20,40,70,.16);" href="https://github.com/jinyan-06/SHIKE" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">PRCV'23</span> DeCAB: Debiased Semi-supervised Learning for Imbalanced Open-Set Data,
  Xiaolin Huang, **Mengke Li**, Yang Lu<span class="corr-icon">✉</span>, and Hanzi Wang, 
  _Chinese Conference on Pattern Recognition and Computer Vision_, Xiamen, Fujian, China, 2023. <span class="ccf-tag ccf-c">CCF-C</span> <a class="pub-link-paper" href="https://keke921.github.io/files/2023-11-26-XLHuang-DeCAB.pdf" target="_blank" rel="noopener">paper</a> <a class="pub-link-code" href="https://github.com/xlhuang132/decab" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">ICIP'23</span> Few-Shot Lip-Password Based Speaker Verification,<br>  
  Zhikai Hu, Yiu-Ming Cheung<span class="corr-icon">✉</span>, **Mengke Li**, and Weichao Lan,<br>
  _International Conference on Image Processing_, pp.1960-1964 , Kuala Lumpur, Malaysia, October 8-11, 2023. <span class="ccf-tag ccf-c">CCF-C</span> <a class="pub-link-paper" href="https://www.comp.hkbu.edu.hk/~ymc/papers/conference/ICIP23-publication-version.pdf" target="_blank" rel="noopener">paper</a>

- <span class="venue-tag">CVPR'22</span> Long-tailed Visual Recognition via Gaussian Clouded Logit Adjustment,<br> 
  **Mengke Li** , Yiu-ming Cheung<span class="corr-icon">✉</span>, and Yang Lu,<br>
  _IEEE/CVF Conference on Computer Vision and Pattern Recognition_, pp.6929-6938, New Orleans, USA, 2022. <span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-arxiv" href="https://arxiv.org/abs/2305.11733" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" href="https://github.com/Keke921/GCLLoss" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">ICME'22</span> Feature-Balanced Loss for Long-Tailed Visual Recognition, 
  **Mengke Li** , Yiu-ming Cheung<span class="corr-icon">✉</span>, and Juyong Jiang,<br>
  _IEEE International Conference on Multimedia and Expo_, oral, pp.1-6, Taipei, Taiwan, July18-22, 2022. oral. <span class="ccf-tag ccf-b">CCF-B</span> <a class="pub-link-arxiv" href="https://arxiv.org/pdf/2305.10772.pdf" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" href="https://github.com/juyongjiang/FBL" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">ICMR'21</span> Facial Structure Guided GAN for Identity-preserved Face Image De-occlusion,
  Yiu-Ming Cheung<span class="corr-icon">✉</span>, **Mengke Li**, and Rong Zou, <br>
  _International Conference on Multimedia Retrieval_, oral, pp.46-54, Taibei, Taiwan, August 21-24, 2021. oral. <span class="ccf-tag ccf-b">CCF-B</span> <a class="pub-link-paper" href="https://www.comp.hkbu.edu.hk/~ymc/papers/conference/ICMR21-publication-version.pdf" target="_blank" rel="noopener">paper</a>  

- <span class="venue-tag">ICME'20</span> Iterative dynamic generic learning for single sample face recognition with a contaminated gallery,<br>
  Meng Pang, Yiu-ming Cheung<span class="corr-icon">✉</span>, Qiquan Shi, and **Mengke Li**,<br>
  _IEEE International Conference on Multimedia and Expo_, oral, pp.1-6, London, UK, July 6-10, 2020. oral. <span class="ccf-tag ccf-b">CCF-B</span> <a class="pub-link-paper" href="https://www.comp.hkbu.edu.hk/~ymc/papers/conference/ICME20-publication-version.pdf" target="_blank" rel="noopener">paper</a> 

</details>

  
  
## 📘 Journal
<details class="pub-year-group" open markdown="1">
  <summary>2025–2024</summary>

- <span class="venue-tag">TNNLS'25</span> MOOD: Leveraging Out-of-Distribution Data to Enhance Imbalanced Semi-Supervised Learning,<br>
  Yang Lu, Xiaolin Huang, Yizhou Chen, **Mengke Li**, Yan Yan, Chen Gong,<br>
  _IEEE Transactions on Neural Networks and Learning Systems_, Early Access, 2025. <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-b">CCF-B</span> <a class="pub-link-paper" href="https://ieeexplore.ieee.org/abstract/document/11027917" target="_blank" rel="noopener">paper</a> <a class="pub-link-code" href="https://github.com/xlhuang132/MOODv2" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">TAI'24</span> Adjusting Logit in Gaussian Form for Long-Tailed Visual Recognition,<br>
  **Mengke Li**, Yiu-ming Cheung<span class="corr-icon">✉</span>, Yang Lu, Zhikai Hu, Weichao Lan, Hui Huang,<br>
  _IEEE Transactions on Artificial Intelligence_, vol. 5, no. 10, pp. 5026-5039, 2024.  <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-paper" href="https://ieeexplore.ieee.org/abstract/document/10531112" target="_blank" rel="noopener">paper</a> <a class="pub-link-arxiv" href="https://arxiv.org/abs/2305.10648" target="_blank" rel="noopener">arxiv</a> <a class="pub-link-code" href="https://github.com/Keke921/GCLLoss" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">TPAMI'24</span> Cross-Modal Hashing Method with Properties of Hamming Space: A New Perspective,<br>
  Zhikai Hu, Yiu-ming Cheung<span class="corr-icon">✉</span>, **Mengke Li**, Weichao Lan,<br>
  _IEEE Transactions on Pattern Analysis and Machine Intelligence_, vol. 46, no. 12, pp. 7636-7650, 2024.  <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-a">CCF-A</span>

- <span class="venue-tag">TPAMI'24</span> Compact Neural Network via Stacking Hybrid Units,<br>
  Weichao Lan, Yiu-Ming Cheung<span class="corr-icon">✉</span>, Juyong Jiang, Zhikai Hu, and **Mengke Li**,<br>
  _IEEE Transactions on Pattern Analysis and Machine Intelligence_, vol. 46, no. 1, pp.103-116, 2024.  <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-a">CCF-A</span>

- <span class="venue-tag">TCSVT'24</span> Joint Semantic Preserving Sparse Hashing for Cross-Modal Retrieval,<br>
  Zhikai Hu, Yiu-ming Cheung<span class="corr-icon">✉</span>, **Mengke Li**, Weichao Lan, Donglin Zhang, Qiang Liu,<br>
  _IEEE Transactions on Circuits and Systems for Video Technology_, vol. 34, no. 4, pp.2989-3002, 2024. <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-b">CCF-B</span>
</details>

<details class="pub-year-group" markdown="1">
  <summary>2023 and Earlier</summary>

- <span class="venue-tag">TPAMI'23</span> Key point sensitive loss for long-tailed visual recognition,<br>
  **Mengke Li**, Yiu-Ming Cheung<span class="corr-icon">✉</span>, and Zhikai Hu,<br>
  _IEEE Transactions on Pattern Analysis and Machine Intelligence_, vol. 45, no. 4, pp.4812-4825, 2023. <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-a">CCF-A</span> <a class="pub-link-paper" href="https://drive.google.com/file/d/1gOJDHBJ_M7RmU6Iw2p6uXIyo8pNgVMrv/view?pli=1" target="_blank" rel="noopener">paper</a> <a class="pub-link-code" href="https://github.com/Keke921/KPSLoss" target="_blank" rel="noopener">code</a>

- <span class="venue-tag">TETCI'23</span> Identity-Preserved Complete Face Recovering Network for Partial Face Image,<br>
  **Mengke Li**, and Yiu-Ming Cheung<span class="corr-icon">✉</span>,<br>
  _IEEE Transactions on Emerging Topics in Computational Intelligence_, vol. 7, no. 2, pp.604-609, 2023. <span class="ccf-tag ccf-a">JCR1区 Top</span><span class="ccf-tag ccf-b">中科院2区</span>


- <span class="venue-tag">TNNLS'21</span> Iterative dynamic generic learning for single sample face recognition with a contaminated gallery,  
  Meng Pang, Yiu-ming Cheung<span class="corr-icon">✉</span>, Qiquan Shi, and **Mengke Li**,<br>
  _IEEE transactions on neural networks and learning systems_, vol. 32, no. 4, pp.1560-1574, 2021. <span class="ccf-tag ccf-a">中科院1区 Top</span><span class="ccf-tag ccf-b">CCF-B</span>

- <span class="venue-tag">GRSL'19</span> TSAR image change detection using PCANet guided by saliency detection,<br>
  **Mengke Li**, Ming Li<span class="corr-icon">✉</span>, Peng Zhang, Yan Wu, Wanying Song, and Lin An,<br>
  _IEEE Geoscience and Remote Sensing Letters_, vol. 16, no. 3, pp.402-406, 2019.<span class="ccf-tag ccf-b">中科院2区 Top</span><span class="ccf-tag ccf-c">CCF-C</span>

</details>
