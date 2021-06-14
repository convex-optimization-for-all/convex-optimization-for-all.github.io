---
layout: post
title: "23-03 Example: lasso regression"
chapter: "23"
order: "04"
owner: "YoungJae Choung"
---


Lasso regression 문제를 아래와 같이 nonsmooth part가 분리되어있는 목적함수의 형태로 정의해보겠다.

> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

**Note:**
$$\|\beta\|_1 = \sum_{i=1}^p | \beta_i |$$

$$\beta_j, j \neq i$$ 가 고정된 값일때, 주어진 목적함수를 최소화시키는 $$\beta_i$$를 구해보자.

$$\begin{align}
&0 = \nabla_i f(\beta) = X_i^T X_i \beta_i + X_i^T(X_{-i} \beta_{-i} - y) + \lambda s_i,\\\\
&\text{where } s_i \in \partial |\beta_i|
\Rightarrow 
\beta_i = S_{\lambda / \|X_i\|_2^2} \big( \frac{X_i^T(y-X_{-i} \beta_{-i})}{X_i^TX_i} \big)
\end{align}$$

Solution은 thresholding level이 $$\lambda / \|X_i\|_2^2$$인 soft-thresholding 함수와도 같다. Coordinate descent를 통해 $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$를 반복하며 업데이트 한다.

## 실험: 수렴속도 비교 - PG vs AGD vs CD

아래 그래프는 $$n=100, p=20$$인 lasso regression 문제에 대해 proximal gradient descent, accelerated gradient descent, coordinate descent의 수렴속도를 비교하여 보여준다. (가로축의 k는 한 step (PD, AGD) 또는 한 cycle (CD)을 나타낸다.)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/pd_vs_agd_vs_cd.png" alt="[Fig1] PD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] PD vs AGD vs CD [3]</figcaption>
</p>
</figure>
<br><br>

[Linear regression의 예시]({% post_url contents/chapter23/21-03-28-23_02_Example_linear_regression %})에서와 마찬가지로 lasso regression 문제에서도 coordinate descent는 월등한 수렴속도를 보인다. (First-order method보다 더 많은 정보를 활용한다.)

* **Note:** 위 실험에서의 모든 methods는 각 iteration당 $$O(np)$$ flops의 시간복잡도를 보인다.
