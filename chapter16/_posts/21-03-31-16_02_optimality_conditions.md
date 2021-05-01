---
layout: post
title: 16-02 Optimality conditions
chapter: "16"
order: 3
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

이번 절에서는 primal problem과 barrier problem에 대한 KKT optimality conditions를 각각 살펴보고 나아가 둘의 차이점을 비교해보도록 한다.
<br/>

## KKT optimality conditions

12장에서 다루어 보았던 KKT conditions를 다시 한 번 정리해보도록 하겠다. KKT conditions는 optimality를 판정하는 조건으로써 사용된다.

#### Primal problem
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

주어진 primal problem이 convex일때, KKT conditions는 primal & dual optimal에 대한 충분조건이 된다. 즉, $$f, h_1, \dots, h_m$$가 convex이고 $$l_1, \dots, l_r$$가 affine일때, $$x^\star, u^\star, v^\star$$가 다음의 KKT conditions를 만족한다면 $$x^\star$$와 $$(u^\star, v^\star)$$는 zero duality gap인 primal & dual optimal이다. ($$f, h_1, \dots, h_m, l_1, \dots, l_r$$는 미분 가능하다고 가정한다.) <br>

* 참고: [12-01 KKT conditions]({% post_url chapter12/21-04-02-12_KKT_conditions %})

#### KKT conditions for the given primal problem
>$$
>\begin{align}
>l_i &= 0, \quad i=1, \dots, r\\\\
>u_i^\star, -h_i(x^\star) &\ge 0, \quad i=1, \dots, m\\\\
>u_i^\star h_i(x^\star) &= 0, \quad i=1, \dots, m\\\\
>\nabla f(x^\star) + \sum_{i=1}^m \nabla h_i(x^\star) u^\star_i + \sum_{i=1}^r \nabla l_i(x^\star) v_i^\star &= 0.\\\\
>\end{align}
>$$

## Central path equations

Barrier problem의 optimality를 판정하는 조건 또한 살펴보도록 하자.

#### Barrier problem

>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad f(x) + \tau \phi(x) \\\\
    &\quad l_j(x) = 0, j = 1, \ldots, r  \\\\
\end{align} \\\\ 
$$
>where $$\phi(x) = - \sum_{i=1}^m \log \big( -h_i(x) \big).$$


Barrier problem에 대한 KKT conditions를 정리하면 아래와 같은 optimality conditions를 유도할 수 있다. 앞서 살펴본 primal problem에 대한 KKT optimality conditions의 inequality constraint, complementary slackness 조건에 대해 차이가 있는 것을 주목하자. (참고: [15-03-01 Perturbed KKT conditions](https://wikidocs.net/21311))

#### Optimality conditions for barrier problem (and its dual)

>$$
\begin{align}
l_i &= 0, \quad i=1, \dots, r\\\\
u_i(t), -h_i(x^\star(t)) &\gt 0, \quad i=1, \dots, m\\\\
u_i(t) h_i(x^\star(t)) &= -\tau, \quad i=1, \dots, m\\\\
\nabla f(x^\star(t)) + \sum_{i=1}^m \nabla h_i(x^\star(t)) u_i(t) + \sum_{i=1}^r \nabla l_i(x^\star(t)) \hat{v}_i^\star &= 0,\\\\
\end{align} \\\\
$$
>where $$\tau = \frac{1}{t}, u_i(t) = - \frac{1}{t h_i(x^\star(t))}, \quad \hat{v} = \frac{1}{t}v.$$

## Special case: linear programming

#### Recall: Primal problem of LP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

#### Recall: Dual problem of LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Linear programming은 inequality constraint가 affine이므로 refined Slater's condition에 의해 항상 strong duality를 만족하는 좋은 성질을 지니고 있다. LP에 대한 optimality conditions는 다음과 같다.

>$$
>\begin{align}
>A^T y^\star + s^\star &= c\\\\
>Ax^\star &= b\\\\
>X S \mathbb{1} &= 0\\\\
>x^\star, s^\star &\ge 0,\\\\
>\end{align} \\
>\text{where }X = Diag(x^\star), S = Diag(s^\star)$$.

참고로 $$X S \mathbb{1} = 0$$는 $$Xs^\star=(x_1^\star s_1^\star, \dots, x_n^\star s_n^\star)=0$$와 같다. 차후 소개될 알고리즘에서의 편의성을 위해 $$X, S$$를 사용하여 표현하였다.

#### Algorithms for linear programming

Optimality conditions를 이용하여 LP를 푸는 대표적인 두 가지 방식을 소개한다.

1. Simplex: 1,2,3번째 조건을 유지하면서 4번째 조건을 차츰 만족하도록 하는 방식.
2. Interior-point methods: 4번째 조건을 유지하면서 1,2,3번째 조건을 점차 만족하도록 하는 방식. 다음 챕터에서 다루게 될 것이다.

## Central path for linear programming

#### Recall: Barrier problem for LP
>$$\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\\\
    \text{subject to} &\quad Ax = b, \\\\
\end{align} \\\\
$$
where $$\tau > 0$$.

#### Recall: Dual problem of Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

LP의 barrier problem에 대한 optimality conditions는 다음과 같다.

>$$
\begin{align}
A^T y^\star + s^\star &= c\\\\
Ax^\star &= b\\\\
X S \mathbb{1} &= \tau \mathbb{1}\\\\
x^\star, s^\star &\gt 0,\\\\
\end{align} \\\\
$$
where $$X = Diag(x^\star), S = Diag(s^\star)$$.

3, 4번째 조건에서 primal LP의 KKT conditions와 차이를 보인다.