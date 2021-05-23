---
layout: post
title: 12-01 Karush-Kuhn-Tucker conditions
chapter: "12"
order: 2
owner: "Wontak Ryu"
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

다음과 같은 일반적인 최적화 문제가 주어졌다고 하자.

>$$
>\begin{align}
>    &\min_{x} &{f(x)} \\\\
>    &\text{subject to } &{h_i(x) \le 0, \text{ } i=1,\dots,m} \\\\
>    & &{l_j(x) = 0, \text{ } j=1,\dots,r}.\\\\
>\end{align}
>$$

이때 **Karush–Kuhn–Tucker (KKT) conditions** 또는 **KKT conditions**는 다음과 같은 조건들로 구성된다 [3].

* $$0 \in \partial \big( f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{r} \nu_j l_j(x) \big)$$ (Stationarity): $$\lambda, \nu$$를 고정했을 때 $$x$$에 대한 subdifferential이 0을 포함하고 있음을 의미한다. 
* $$\lambda_i \cdot h_i(x) = 0 \text{ for all } i$$ (Complementary Slackness):  $$\lambda_i$$와 $$h_i$$ 중 적어도 하나의 값은 0을 가짐을 의미한다.
* $$h_i(x) \le 0, l_j(x) = 0 \text{ for all } i, j$$ (Primal Feasibility): Primal problem의 제약조건들에 대한 만족여부를 나타낸다.
* $$\lambda_i \ge 0 \text{ for all } i$$ (Dual Feasibility): Dual problem의 제약조건들에 대한 만족여부를 나타낸다.

## Sufficiency
Convex인 primal problem에 대해 KKT conditions를 만족하는 $$x^\star, \lambda^\star, \nu^\star$$가 있을때, 다음의 과정은 $$x^\star, \lambda^\star, \nu^\star$$가 zero duality gap의 primal & dual solutions임을 보인다.

>$$
>\begin{align}
>    g(\lambda^\star, \nu^\star) &= \min_x L(x, \lambda^\star, \nu^\star) \\\\
>                                &= L(x^\star, \lambda^\star, \nu^\star) \\\\
>                                &= f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                                &= f(x^\star)
>\end{align}
>$$

1. $$L(x,\lambda^\star,\nu^\star) = f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x)$$는 convex 함수다. (convex함수들의 합) 
2. $$0 \in \partial \big( f(x^\star) + \sum_{i=1}^{m} \lambda_i^\star h_i(x^\star) + \sum_{j=1}^{r} \nu_j^\star l_j(x^\star) \big)$$이므로 $$\min_x L(x, \lambda^\star, \nu^\star) = L(x^\star, \lambda^\star, \nu^\star)$$이다.
3. Complementary slackness와 primal feasibility에 의해 $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$이다.

## Neccessity
$$x^\star, \lambda^\star, \nu^\star$$가 zero duality gap(가령, Slater's condition을 만족)의 primal & dual solutions일때, 다음의 부등호들이 전부 등호가 되므로 이 문제에서 $$x^\star, \lambda^\star, \nu^\star$$는 KKT conditions를 만족하게 된다.
>$$
>\begin{align}
>    f(x^\star) &= g(\lambda^\star, \nu^\star) \\\\
>                   &= \min_x  \big( f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x) \big) \\\\
>                   &\le f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                   &\le f(x^\star)
>\end{align}
>$$

1. $$f(x^\star) = g(\lambda^\star, \nu^\star)$$는 zero duality gap을 의미한다.
2. $$f(x^\star) + \sum_{i=1}^m \underbrace{\lambda_i^\star h_i(x^\star)}_{0} + \sum_{j=1}^r \underbrace{\nu_j^\star l_j(x^\star)}_{0} = f(x^\star)$$를 만족하기 위해서는 complementary slackness와 primal feasibility를 만족해야 한다.
3. $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$를 만족하면 위 전개의 모든 부등호는 등호가 된다.

## Putting it together
요약하자면 KKT conditions는:

* Zero duality gap의 primal & dual solutions에 대한 충분조건이다.
* Strong duality를 만족한다면 primal & dual solutions에 대한 필요조건이 된다.

즉, strong duality를 만족하는 문제에 대해 다음과 같은 관계가 성립한다.
>$$
>\begin{align}
>    x^\star, \lambda^\star, \nu^\star \text{ are primal and dual solutions} \\\\
>    \Leftrightarrow x^\star, \lambda^\star, \nu^\star \text{ satisfy the KKT conditions} \\\\
>\end{align}
>$$