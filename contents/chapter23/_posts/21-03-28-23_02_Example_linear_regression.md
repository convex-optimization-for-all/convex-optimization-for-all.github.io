---
layout: post
title: "23-02 Example: linear regression"
chapter: "23"
order: "03"
owner: "YoungJae Choung"
---

Linear regression 문제를 다음과 같이 정의해보겠다.

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^{n \times p} \text{ with columns } X_1, \dots, X_p.$$

$$\beta_j,\: j \neq i$$가 고정된 값일때, 주어진 목적함수를 최소화시키는 $$\beta_i$$를 구해보자.
($$-i$$는 $$i$$를 제외한 나머지 항을 의미한다. - $$X$$의 경우 $$i$$번째 column을 제외한 나머지 column.)

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Coordinate descent를 통해 $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$를 반복하며 업데이트 한다.

## 실험: 수렴속도 비교 - GD vs AGD vs CD

아래 그래프는 $$n=100, p=20$$인 linear regression 문제에 대해 coordinate descent, gradient descent, accelerated gradient descent의 수렴속도를 비교하여 보여준다. (가로축의 k는 한 step (GD, AGD) 또는 한 cycle (CD)을 나타낸다.)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Fig1] GD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] GD vs AGD vs CD [3]</figcaption>
</p>
</figure>
<br/>

위 결과에 의하면 coordinate descent는 first-order method의 optimal인 AGD보다도 월등히 좋은 수렴속도를 보인다. 어째서 이런 현상이 발생할 수 있는 것일까? 결론부터 말하자면, coordinate descent는 first-order method보다 더 많은 정보를 활용하므로 AGD를 훌쩍 상회하는 성능을 내는 것이 가능하다. Coordinate descent는 한 cycle 내에서 각 step마다 이전 step에서 갱신된 최신 정보를 이용하기 때문이다. (즉, CD는 first-order method가 아니다.)

#### Q. 그렇다면 위 실험에서 CD의 한 cycle을 GD의 한 step과 비교한 것은 공정한 것일까?

**A. 그렇다.** 앞서 소개한 CD의 업데이트 식을 한 step의 시간복잡도가 $$O(n)$$인 형태로 변형시킬 수 있다. 그렇다면 CD에 대한 한 cycle의 시간복잡도는 $$O(np)$$가 되며 GD의 한 step과 같은 시간복잡도를 가지게 된다.

* **Gradient descent update:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, $$X\beta$$ 연산에 의해 시간복잡도는 $$O(np)$$ flops가 된다.
