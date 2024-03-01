---
title: "Compact Neural Network via Stacking Hybrid Units"
collection: publications
permalink: /publication/2023-10-10-WCLan-BUnit-Net
excerpt: 'network compression'
date: 2024-01-01
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)'
paperurl: '/files/2023-10-10-WCLan-BUnit-Net.pdf'
citation: 'W. Lan, Y.-M. Cheung, J. Jiang, Z. Hu and M. Li, "Compact Neural Network via Stacking Hybrid Units," in </i>IEEE Transactions on Pattern Analysis and Machine Intelligence</i>, vol. 46, no. 1, pp. 103-116, Jan. 2024, doi: 10.1109/TPAMI.2023.3323496.'
---
As an effective tool for network compression, pruning techniques have been widely used to reduce the large number of parameters in deep neural networks (NNs). Nevertheless, unstructured pruning has the limitation of dealing with the sparse and irregular weights. By contrast, structured pruning can help eliminate this drawback but it requires complex criteria to determine which components to be pruned. Therefore, this paper presents a new method termed BUnit-Net, which directly constructs compact NNs by stacking designed basic units, without requiring additional judgement criteria anymore. Given the basic units of various architectures, they are combined and stacked systematically to build up compact NNs which involve fewer weight parameters due to the independence among the units. In this way, BUnit-Net can achieve the same compression effect as unstructured pruning while the weight tensors can still remain regular and dense. We formulate BUnit-Net in diverse popular backbones in comparison with the state-of-the-art pruning methods on different benchmark datasets. Moreover, two new metrics are proposed to evaluate the trade-off of compression performance. Experiment results show that BUnit-Net can achieve comparable classification accuracy while saving around 80% FLOPs and 73% parameters. That is, stacking basic units provides a new promising way for network compression.

![image](https://keke921.github.io/files/2023-10-10-WCLan-BUnit-Net.png)

```bibtex
@ARTICLE{10275036,
  author={Lan, Weichao and Cheung, Yiu-Ming and Jiang, Juyong and Hu, Zhikai and Li, Mengke},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title={Compact Neural Network via Stacking Hybrid Units}, 
  year={2024},
  volume={46},
  number={1},
  pages={103-116},
  doi={10.1109/TPAMI.2023.3323496}}
```

<!--
The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.
-->
