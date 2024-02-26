---
title: "DeCAB: Debiased Semi-supervised Learning for Imbalanced Open-Set Data"
collection: publications
permalink: /publication/2023-11-26-XLHuang-DeCAB
excerpt: 'Solving the data that distributed wiht long-tailed distributions and OOD samples'
date: 2024-02-17
venue: 'Chinese Conference on Pattern Recognition and Computer Vision (PRCV)'
paperurl: 'https://keke921.github.io/files/2023-11-26-XLHuang-DeCAB.pdf'
citation: 'Huang, X., Li, M., Lu, Y., & Wang, H. (2023). &quot;DeCAB: Debiased Semi-supervised Learning for Imbalanced Open-Set Data.&quot; <i>Chinese Conference on Pattern Recognition and Computer Vision (PRCV)</i>. pp.104-119.'
---
Semi-supervised learning (SSL) has received significant attention due to its ability to use limited labeled data and various unlabeled data to train models with high generalization performance. However, the assumption of a balanced class distribution in traditional SSL approaches limits a wide range of real applications, where the training data exhibits long-tailed distributions. As a consequence, the model is biased towards head classes and disregards tail classes, thereby leading to severe class-aware bias. Additionally, since the unlabeled data may contain out-of-distribution (OOD) samples without manual filtering, the model will be inclined to assign OOD samples to non-tail classes with high confidence, which further overwhelms the tail classes. To alleviate this class-aware bias, we propose an end-to-end semi-supervised method Debias Class-Aware Bias (DeCAB). DeCAB introduces positive-pair scores for contrastive learning instead of positive-negative pairs based on unreliable pseudo-labels, avoiding false negative pairs negatively impacts the feature space. At the same time, DeCAB utilizes class-aware thresholds to select more tail samples and selective sample reweighting for feature learning, preventing OOD samples from being misclassified as head classes and accelerating the convergence speed of the model. Experimental results demonstrate that DeCAB is robust in various semi-supervised benchmarks and achieves state-of-the-art performance. Our code is temporarily available at https://github.com/xlhuang132/decab.



```bibtex
@inproceedings{huang2023decab,
  title={DeCAB: Debiased Semi-supervised Learning for Imbalanced Open-Set Data},
  author={Huang, Xiaolin and Li, Mengke and Lu, Yang and Wang, Hanzi},
  booktitle={Chinese Conference on Pattern Recognition and Computer Vision (PRCV)},
  pages={104--119},
  year={2023},
  organization={Springer}
}
```

<!--
The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.
-->
