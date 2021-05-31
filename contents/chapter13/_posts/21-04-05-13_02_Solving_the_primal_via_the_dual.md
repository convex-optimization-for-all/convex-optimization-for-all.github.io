---
layout: post
title: 13-02 Solving the primal via the dual
chapter: "13"
order: 3
owner: "Wontak Ryu"
---

### An important consequence of stationarity
Strong duality의 조건하에서 Dual solution $$u^{\star}, v^{\star}$$가 주어졌을 때, primal solution $$x^{\star}$$으로 다음의 라그랑지안을 풀 수 있다.

> $$ \min_x f(x) + \sum_{i=1}^m u_i^{\star} h_i(x) + \sum_{j=1}^r v^{\star}_i l_j(x)$$

종종 이러한 제약 없는 문제(unconstrained problem)의 솔루션은 dual solution을 통해 primal solution의 특징을 명시적으로 가져다 씀으로써 나타낼 수 있다.

게다가, 이 문제의 해가 유일하다면, dual solution이 primal solution $$x^{\star}$$가 된다.
즉, primal 문제를 직접 풀 때보다 dual 문제로 푸는 것이 더 쉬울 때 매우 유용하다.



### Example from B & V page 249:
> $$ \min_x \sum_{i=1}^n f_i(x_i) \qquad \text{ subject to }\qquad a^Tx = b$$

각각의 $$f_i : \mathbb{R} → \mathbb{R}$$ 가 smooth하고, strictly convex이면 Dual function은 아래와 같다.

> $$\begin{align}
> g(v) &= \min_x \sum_{i=1}^n f_i(x_i) + v(b−a^Tx) \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −va^Tx \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −v \sum_{i=1}^n a_ix_i \\\
> &= bv + \sum_{i=1}^n (\underbrace{\min_{x_i} \{ f_i(x_i) − a_ivx_i \}}_{-f^{*}_i(a_iv)}) \\\
> &= bv − \sum_{i=1}^n f^{*}_i (a_iv)
> \end{align}$$
 
여기서 $$f^{*}$$는 $$f_i$$의 conjugate를 의미 한다.

그러므로 dual problem은 다음과 같이 나타낼 수 있다.
> $$ \max_v bv − \sum^n_{i=1} f^{*}_i (a_iv)$$

또한 마이너스(-)를 곱해 maximum 문제를 다음과 minimum 문제로 나타낼 수도 있다.
> $$ \min_v \sum^n_{i=1} f^{*}_i (a_iv) − bv$$

이것은 스칼라 변수의 볼록 최소화 (convex minimization) 문제로 primal 문제보다 훨씬 쉽게 풀 수 있다.

$$v^{\star}$$가 주어졌을 때 primal solution $$x^{\star}$$은 아래와 같이 풀 수 있다.
> $$ \min_{x} \sum^n_{i=1} (f_i(x_i) − a_iv^{\star}x_i)$$

각 $$f_i$$의 Strict convexity는 이것이 유일한 솔루션을 가진다는 것을 의미한다.
즉, $$x^{\star}$$는 각 $$i$$에 대해 $$∇f_i(x_i) = a_iv^{\star}$$의 계산을 통해 얻어진다.

