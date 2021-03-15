---
layout: post
title: Transformations and change of variables
chapter: "04"
order: 5
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

목적함수 또는 제약함수는 주어진 optimization problem를 유지하는 선에서 변경될 수 있으며, 때로는 이를 이용해 문제의 "hidden convexity"를 찾아낼 수 있다.

#### Theorem1
함수 $h : \mathbb{R} \rightarrow \mathbb{R} $가 monotone increasing transformation일때, 아래의 관계가 성립한다.

>$
>\begin{aligned}
>&\text{min}\_{x} f(x) &&\text{ subject to } x \in C \\\\
>\Longleftrightarrow &\text{min}\_{x} h(f(x)) &&\text{ subject to } x \in C
>\end{aligned}
>$

#### Theorem2
함수 $\phi: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$가 일대일 대응 함수이고, $\phi$의 상(image)이 feasible set $C$를 커버한다면 optimization problem의 변수는 다음과 같이 변경될 수 있다.   

>$
>\begin{aligned}
>&\min\_{x} f(x) &&\text{ subject to } x \in C \\\\ 
>\Longleftrightarrow &\min\_{y} f(\phi(y)) &&\text{ subject to } \phi(y) \in C
>\end{aligned}
>$

#### Example: geometric programming

함수 $f: \mathbb{R}\_{++}^n \rightarrow \mathbb{R}$가 다음과 같은 형태일때 이를 **monomial**이라 부른다.
> $f(x) = \gamma x\_1^{a\_1} x\_2^{a\_2} \dotsb x\_n^{a\_n} \text{ for } \gamma > 0, a\_1, \dotsc, a\_n \in \mathbb{R}.$

또한 monomial의 합을 **posynomial**이라 부른다.
> $g(x) = \sum\_{k=1}^p \gamma\_{k} x\_1^{a\_{k1}} x\_2^{a\_{k2}} \dotsb x\_n^{a\_{kn}} \text{ for } \gamma > 0, a\_1, \dotsc, a\_n \in \mathbb{R}.$

**Geometric program**은 다음과 같은 형태로 정의되며, 이는 non-convex problem이다.
>$
>\begin{aligned}
>    &\text{minimize}\_{x} &{f(x)} \\\\
>    &\text{subject to } &{g_{i}(x) \leq 1, i = 1, \dotsc, m} \\\\
>    & &{h_{j}(x) = 1, j = 1, \dotsc, r}, \\\\
>\end{aligned}\\\\
>    \text{where $f$, $g_i, i=1, \dotsc, m$ are posynomials and $h\_j, j=1, \dotsc, r$ are monomials.}
>$

Geometric program이 어떤 convex problem과 동일함을 증명해보자.

#### Proof:
>$f(x) = \gamma x\_1^{a\_1} x\_2^{a\_2} \dotsb x\_n^{a\_n}$일때, $y_i = logx_i$, $b=log \gamma$라 하면 $f$는 다음과 같이 변경될 수 있으며, **Theorem2**에 의해 이는 주어진 optimization problem을 동일하게 유지한다.
>$\gamma (e^{y\_1})^{a\_1} (e^{y\_2})^{a\_2} \dotsb (e^{y\_n})^{a\_n} = e^{a^Ty + b}$
>
>또한 posynomial은 $\sum\_{k=1}^{p} e^{a\_{k}^Ty + b\_{k}}$로 나타낼 수 있다.
>
>이때, **Theorem1**에 의해 이에 log를 취해준 형태인 $log \big( \sum\_{k=1}^{p} e^{a\_{k}^Ty + b\_{k}} \big)$ 또한 optimization problem을 동일하게 유지할 수 있다.
>
>즉, geometric program은 다음의 문제와도 동일하며 이는 convex problem이다.
>
<!-- >$
>\begin{aligned}
>    &\text{minimize}\_{x} & {log \big( \sum_{k=1}^{p\_0} e^{a\_{0k}^Ty + b\_{0k}} \big)} \\\\
>    &\text{subject to } &{{log \big( \sum\_{k=1}^{p\_i} e^{a\_{ik}^Ty + b\_{ik}} \big)} \leq 0, i = 1, \dotsc, m} \\\\
>    & &{c\_j^Ty + d\_j = 0, j = 1, \dotsc, r}, \\\\
>\end{aligned}\\\\
>$ -->

> $
> {{log \big( \sum\_{k=1}^{p\_i} e^{a\_{ik}^Ty + b\_{ik}} \big)} \leq 0, i = 1, \dotsc, m}
> $

> $
>  {c\_j^Ty + d\_j = 0, j = 1, \dotsc, r},
> $


>$
>\begin{aligned}
>    &\text{minimize}_{x} \space {log \big( \sum_{k=1}^{p\_0} e^{a\_{0k}^Ty + b\_{0k}} \big)} \\\\
>  \text{subject to } \space {{log \big( \sum\_{k=1}^{p\_i} e^{a\_{ik}^Ty + b\_{ik}} \big)} \leq 0, i = 1, \dotsc, m} \\\\
>  {c\_j^Ty + d\_j = 0, j = 1, \dotsc, r}, \\\\
>\end{aligned}
>$

<!-- >$
>\begin{aligned}
>    &\text{minimize}\_{x} & {log \big( \sum_{k=1}^{p\_0} e^{a\_{0k}^Ty + b\_{0k}} \big)} \\\\
>    &\text{subject to } &{{log \big( \sum\_{k=1}^{p\_i} e^{a\_{ik}^Ty + b\_{ik}} \big)} \leq 0, i = 1, \dotsc, m} \\\\
>    & &{c\_j^Ty + d\_j = 0, j = 1, \dotsc, r}, \\\\
>\end{aligned}\\\\
>$ -->