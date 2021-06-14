---
layout: post
title: 19-01-03 Scaled proximal map
chapter: "19"
order: "05"
owner: "Hooncheol Shin"
---

**Proximal newton method**를 **proximal gradient descent**와 같은 형식으로 다시 작성해 볼 수 있다. 

## Scaled proximal map
만일 $$H \succ 0$$라고 하면 **scaled proximal map**은 다음과 같이 정의된다.

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\text{argmin}}  \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

여기서 $$\parallel x\parallel_H^2 = x^THx$$으로 $$H\text{-norm}$$이다.  $$H = \frac{1}{t} I$$일 때 일반적인 **unscaled proximal map**이 된다. 

일반적으로 **scaled proximal map**는 보통의 prox보다 좋은 성질을 갖고 있다. 

* **uniqueness** : 해가 하나만 존재하는 성질 ($$H \succ 0$$이므로 strictly convex optimization problem이기 때문에 만족된다.)
* **non-expansiveness** :  팽창하지 않는 성질 (scaled proximal map이 non-expansive 성질을 갖는 projection operator의 일반화이기 때문에 만족된다.)

#### [참고] Projection operator의 non-expansiveness
두 점 $$x$$, $$y$$와 convex set $$C$$에 대한 projection operator $$P_c$$에 대해 non-expansiveness란 $$\parallel P_c(x) - P_c(y) \parallel_2 \le \parallel x - y \parallel_2$$를 만족한다는 것을 의미한다. 즉,  $$P_c$$는 Lipschitz-1을 만족하며 $$C$$가 convex일 경우에만 만족한다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.PNG" alt="[Fig 1] Projection onto a convex set C [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Projection onto a convex set C [3]</figcaption>
</p>
</figure>

## Proximal newton update
**Scaled proximal map**을 이용해서 Proximal newton update를 다시 표현해보면 다음과 같다.

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \nabla g(x)^T (z - x)^T v + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

다르게 표현하면 다음과 같다.

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

직관적으로 $$g$$에 대해서 newton step을 수행하고, $$H^{(k-1)}$$에 대해 scaled prox operator를 적용해서 그 방향으로 이동한다는 것을 의미한다.

이로부터 다음과 같은 사항을 알 수 있다.

* $$h(z) = 0$$일때 proximal operator는 identity 함수가 되여 일반적인 Newton update가 된다.
* $$H^{(k+1)}$$를 $$\frac{1}{r_k} I$$로 대체하고 $$t_k = 1$$로 두면 step size $$r_k$$에 대해 proximal gradient update를 구할 수 있다. 
* Prox의 어려움은 $$h$$뿐만 아니라 $$g$$의 hessian의 구조에 따라 달라진다. 예를 들어 $$H$$가 diagonal이거나 banded이면 dense한 $$H$$일 경우에 비해 문제가 매우 쉬워진다.

따라서,  proximal Newton method는 proximal gradient descent와 Newton's method를 둘 다 일반화한 것임을 알 수 있다.
