---
layout: post
title: 05 Canonical Problems
chapter: "05"
order: "01"
owner: "Hooncheol Shin"
---

# Canonical Problems

[첫 번째 장](/chapter01/2021/01/07/optimization_problems/)에서 convex optimization problem이 다음과 같이 정의됨을 알아보았다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/17203/Optimization_problem.png" alt="[Fig1] Convex Optimization Problem in standard form [3]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Convex Optimization Problem in standard form [3]</figcaption>
</p>
</figure>

* The domain set is convex
* The objective function $$ f $$ and the inequality constraint function $$ g_i $$ are convex
* The equality constraint function $$ h_j $$ is affine

이때 objective function과 constraint function의 유형에 따라 optimization problem은 다양한 범주로 나뉘어지게 된다. 이 장에서는 그 중 다음 6가지 세부항목에 대해 알아보도록 할 것이다.

- Linear Programming (LP)
- Quadratic Programming (QP)
- Quadratically Constrained Quadratic Programming (QCQP)
- Second-Order Cone Programming (SOCP)
- Semidefinite Programming (SDP)
- Conic Programming (CP)

위의 문제들은 다음과 같은 포함관계를 가지고 있으며, 우측으로 갈수록 좀 더 일반화된 형식이라고 볼 수 있다.

$$ LP \subseteq QP \subseteq QCQP \subseteq SOCP \subseteq SDP \subseteq CP $$
<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/17851/canonical_problems.jpg" alt="[Fig2] Canonical Problems" width="90%">
  <figcaption style="text-align: center;">[Fig2] Canonical Problems</figcaption>
</p>
</figure>