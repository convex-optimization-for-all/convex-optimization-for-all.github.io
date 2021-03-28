---
layout: post
title: 21 Alternating Direction Method of Multipliers
chapter: "21"
order: 1
owner: "Hooncheol Shin"
---

이 장에서는 [20장](https://wikidocs.net/edit/page/22606)에서 다루었던 ADMM을 조금 더 자세히 다루어보고자 한다. 기본적인 개념은 20장에서 다룬 내용과 깊이에서 큰 차이가 없고, 응용 사례들을 위주로 살펴본다.

#### 참고 논문

* Boyd, Stephen, et al. [BPCPE11] "Distributed optimization and statistical learning via the alternating direction method of multipliers." Foundations and Trends® in Machine learning 3.1 (2011): 1-122.
* Hong, Mingyi, and Zhi-Quan Luo. [HL12] "On the linear convergence of the alternating direction method of multipliers." Mathematical Programming 162.1-2 (2017): 165-199.
* Deng, Wei, and Wotao Yin. [DY16] "On the global and linear convergence of the generalized alternating direction method of multipliers." Journal of Scientific Computing 66.3 (2016): 889-916.
* Iutzeler, Franck, et al. [IBCH14] "Linear convergence rate for distributed optimization with the alternating direction method of multipliers." 53rd IEEE Conference on Decision and Control. IEEE, 2014.
* Nishihara, Robert, et al. [NLRPJ15] "A general analysis of the convergence of ADMM." arXiv preprint arXiv:1502.02009 (2015).
* Parikh, Neal, and Stephen Boyd. [NB13] "Proximal algorithms." Foundations and Trends® in Optimization 1.3 (2014): 127-239.
* Vu, Vincent Q., et al. [VCLR13] "Fantope projection and selection: A near-optimal convex relaxation of sparse PCA." Advances in neural information processing systems. 2013.
* Candès, Emmanuel J., et al. [CLMW09] "Robust principal component analysis?." Journal of the ACM (JACM) 58.3 (2011): 11.
* Ramdas, Aaditya, and Ryan J. Tibshirani. [RT16] "Fast and flexible ADMM algorithms for trend filtering." Journal of Computational and Graphical Statistics 25.3 (2016): 839-858.
* Wytock, Matt, Suvrit Sra, and Jeremy Z. Kolter. [WSK14] "Fast Newton methods for the group fused lasso." UAI. 2014.
* Barbero, Alvaro, and Suvrit Sra. [BS14] "Modular proximal optimization for multidimensional total-variation regularization." arXiv preprint arXiv:1411.0589 (2014).


ADMM convergence 관련 : [BPCPE11], [HL12], [DY16], [IBCH14], [NLRPJ15]  
Sparse subspace estimation : [VCLR13]  
Sparse plus low rank decomposition : [CLMW09]  
Consensus ADMM : [BPCPE11], [NB13]  
Subprogram parameterization : [RT16], [WSK14], [BS14]
