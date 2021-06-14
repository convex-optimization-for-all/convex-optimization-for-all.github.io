---
layout: post
title: 12-02 Example quadratic with equality constraints
chapter: "12"
order: "03"
owner: "Wontak Ryu"
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Equality constraint만을 가진 [quadratic program]()은 다음과 같다.
>$$
>\begin{align}
>    &\min_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to} &&{Ax = b},\\\\
>&\text{where } &&P \in \mathbb{S}_{+}^n \text{ and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

위 문제는 convex이고 inequality constraint가 없으므로 이 문제는 Slater's condition을 만족한다 (Strong duality). 이때, primal & dual solutions가 $$x^\star, \nu^\star$$라고 하면 KKT conditions에 의해 아래의 조건들을 만족한다 [1].

* Stationarity: $$Px^\star + q + A^T\nu^\star = 0$$
* Complementary Slackness: Inequality constraint가 없으므로 고려하지 않아도 된다.
* Primal & dual feasibility: $$Ax^\star = b$$

위 조건들은 block matrix를 이용하여 간략하게 표현할 수 있으며, 이를 KKT matrix라고 부른다 [3].
> $$
> \begin{bmatrix}
>     P       & A^T  \\\\
>     A       & 0  \\\\
> \end{bmatrix}
> \begin{bmatrix}
>     x^\star  \\\\
>     \nu^\star  \\\\
> \end{bmatrix}
> =
> \begin{bmatrix}
>     -q  \\\\
>     b  \\\\
> \end{bmatrix}
> $$

이 matrix곱을 풀면 주어진 문제에 대한 primal & dual solutions를 구할 수 있다.

흥미로운 사실은 이 문제는 equality constrained problem에 대한 Newton step을 구하는 것과 같다고도 볼 수 있다는 것이다 [3]. $$min_x f(x) \text{ subject to } Ax = b$$ 라는 문제에 대해 P, q, r을 다음과 같이 설정하면 quadratic program의 목적함수는 $$f(x)$$의 second-order Taylor expansion과 동일해진다.<br/>
> $$P = \nabla^2 f(x^{(k-1)})$$, $$q = \nabla f(x^{(k-1)})$$, $$r = f(x^{(k-1)})$$