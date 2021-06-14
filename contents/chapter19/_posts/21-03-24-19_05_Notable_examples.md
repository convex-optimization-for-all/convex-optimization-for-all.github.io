---
layout: post
title: 19-05 Notable examples
chapter: "19"
order: "09"
owner: "Hooncheol Shin"
---

## Glmnet and QUIC
Proximal newton method의 매우 유명한 패키지가 두 가지가 있다.

* **glmnet** (Friedman et al., 2009): $$l_1$$ penalized generalized linear models에 대한 prox Newton를 구현한 패키지. Coordinate descent를 이용해서 inner problem을 푼다.

* **QUIC**  (Hsiesh et al., 2011): graphical lasso problem에 대한 prox Newton을 구현한 패키지. Factorization trick을 사용하고 coordinate descent를 이용해서 inner problem을 푼다.

두 구현 패키지는 각자의 용도에 맞춰서 매우 광범위하게 사용되고 있으며 state-of-the-art라고 할 수 있다.

Proximal Newton method는  proximal gradient보다 $$g$$의 gradient을 덜 자주 계산한다. 따라서, 계산 비용이 커질수록 proximal newton이 유리하다. 또한, inner solver를 신중하게 선택할수록 좋은 성능을 얻을 수 있다.

## Example: lasso logistic regression
Lee et al. (2012)논문에서 제시된 예제를 살펴보자. 

$$l_1$$ regularized logistic regression에대해 다음 세가지 방법에 대해서 성능을 평가하였다.
1.FISTA : accelerated prox grad 2. spaRSA : spectral projected gradient method 3. PN  : proximal Newton

#### Dense hessian X (n=5000, p=6000) 예시
데이터 수 n = 5000, feature 개수 p = 6000인 dense feature matrix $$X$$를 갖는 문제에 대해 다음과 같은 성능을 보였다. Hessian이 dense하기 때문에 매우 challenging한 문제라고 할 수 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example1.PNG" alt="[Fig 1] Dense hessian X (n=5000, p=6000) [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Dense hessian X (n=5000, p=6000) [2]</figcaption>
</p>
</figure>

오른쪽은 함수 호출 기준으로, 왼쪽은 시간 기준으로 평가한 것으로서, 함수 호출 기준으로 봤을 때가 PN의 성능이 매우 우세함을 알 수 있다. 

여기서 비용은 $$g$$와 $$\nabla g$$를 계산하는 시간이 대부분이며 특히 $$\exp$$와 $$\log$$함수를 계산하는 시간이 많이 들었다.

#### Sparse hessian X (n=542,000, p=47,000) 예시

다음의 경우는 $$X$$가 sparse하기 때문에 $$g$$와 $$\nabla g$$를 계산하는 시간이 덜 들었다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example-sparse.PNG" alt="[Fig 2] Sparse hessian X (n=542,000, p=47,000) [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Sparse hessian X (n=542,000, p=47,000) [2]</figcaption>
</p>
</figure>

## Inexact prox evaluations
Proximal Newton method에서 proximal operation을 계산할 때  prox operator가 closed form이 아니기 때문에 정확히 계산하지 못한다. 그럼에도 불구하고, 매우 높은 정확도를 갖는다면 매우 좋은 성질이 될 수 있다. 

Lee (2014)에서는 global convergence와  local superlinear convergence를 보장하는 inner problem의 stopping rule을 제안했다.

#### Three stopping rules 
Graphical lasso estimation 문제에 inner optimizations을 위한 세 가지 stopping rules을 비교하였다. 이때, 데이터 개수는 n = 72이고 feature 개수는 p = 1255이다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Inexact_prox.PNG" alt="[Fig 3] Three stopping rules [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 3] Three stopping rules [2]</figcaption>
</p>
</figure>

세 가지 stopping rule은 adaptive, maxiter = 10, exact이다. Maxiter는 inner iteration을 최대 10번까지만 하는 방식이고 exact는 정확한 해를 구할 때까지 반복하는 방식이다.

Proximal newton method가 quadratic convergence를 만족하므로 exact는  quadratic convergence를 만족한다고 볼 수 있다. Maxiter=10의 경우 최대 10번의 inner iteration으로는 quadratic convergence를 만족하지 못하지만 adaptive의 경우 quadratic convergence를 만족하며 세 가지 방식 중 가장 빠르다. 

#### Stopping rule of usual newton method
일반적인 newton's method에서는 inner problem은 $$x^{(k-1)}$$의 $$g$$에 대한 qudratic approximation인 $$\tilde{g}_{k-1}$$를 최소화한다. 그리고, $$\eta_k, k=1,2,3,...$$를 선택해서 다음 조건을 만족할 때 중지한다. (이를 forcing sequence라고 한다.)

> \begin{align}
\parallel \nabla \tilde{g}_{k-1}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  \nabla g(x^{(k-1)})  \parallel_2 \\\\
\end{align}

이 조건은 다음 위치에서의 gradient가 현재 위치에서의 gradient보다 $$\eta_k$$배 만큼 작다는 것을 의미한다. 이때, Quadratic approximation은 $$\tilde{g}_{k-1}(z) = \nabla g(x)^T (z-x) + \frac{1}{2t} \parallel  z - x \parallel_2^2$$이다.

#### Stopping rule of proximal gradient method
Lee et al. (2012)에서는 proximal gradient에서는 gradient 대신에 generalized gradient를 사용하는 방식을 제안하였다.

> $$
> \begin{align}
\parallel G_{\tilde{f}_{k-1}/M}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  G_{f/M}(x^{(k-1)})  \parallel_2
\end{align}
> $$

여기서 $$\tilde{f}_{k-1} = \tilde{g}_{k-1} + h$$이고 $$mI \preceq \nabla^2 g \preceq MI$$이다.

그리고, 다음과 같이 $$\eta_k$$를 설정하여 inexact proximal newton이 local superlinear rate를 갖는다는 것을 증명하였다.

> $$
> \begin{align} 
> \eta_k \le \min \left\{ \frac{m}{2},  \frac{\parallel  G_{\tilde{f}_{k-2}/M}(x^{(k-1)}) - G_{f/M}(x^{(k-1)})  \parallel_2}{\parallel  G_{f/M}(x^{(k-2)})  \parallel_2} \right\}
> \end{align}
> $$
