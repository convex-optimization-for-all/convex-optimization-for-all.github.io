---
layout: post
title: 08-02-04 Batch vs Stochastic Methods
chapter: "08"
order: "16"
owner: "Kyeongmin Woo"
---

# Batch vs Stochastic Methods

Batch method와 stochastic method의 수렴은 다음과 같은 성질을 띈다. 

일반적으로 stochastic method는 초반에 빠르게 optimal point 근처로 접근하지만, optimal point 근처에서 어느 순간 더 이상의 수렴을 잘하지 못한다. 반면 batch method는 느리지만 비교적 정확하게 optimal point로 점차 수렴해가는 것을 관찰 할 수 있다.

아래는 [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)을 batch 방식과 stochastic 방식을 사용했을때, 각각의 수렴성을 비교한 그림이다. (regularizaton은 사용하지 않음)

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/18973/stochastic_vs_batch.PNG" alt="stochastic_vs_batch" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 3] Batch vs Stochastic Gradient Descent [2]</figcaption>
</figure>
