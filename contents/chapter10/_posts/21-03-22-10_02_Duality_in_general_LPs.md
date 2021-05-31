---
layout: post
title: 10-02 Duality in general LPs
chapter: "10"
order: "03"
owner: "Wontak Ryu"
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

[10-01]({% post_url contents/chapter10/21-03-22-10_01_Lower_Bounds_in_Linear_Programs %})에서 단일 차원의 변수의 LP 문제에 대한 primal, dual을 살펴보았다. 10-02에서는 general form(일반형)을 가지는 LP에 대한 dual을 살펴보고자 한다.

LP의 general form은 다음과 같다.

$$c\in\mathbb{R}^{n},\, A\in\mathbb{R}^{m\times n},\, b\in\mathbb{R}^{m},\, G\in\mathbb{R}^{r\times n},\, h\in\mathbb{R}^{r}$$ 라 주어졌을 때,

>$$
>\begin{align}
>&\min_{x} &c^{T}x\\\\
>&\text{subject to} &Ax = b\\\\
>& &Gx \leq h.\\\\
>\end{align}
>$$

앞 10-01의 예시와 동일하게, constraint 개수와 동일한 수의 dual variable $$u, v$$를 정의하고,
constraint와 각 dual variable의 곱의 합으로 dual 문제의 objective function을 정의하고, constraint를 정의할 수 있다. 

>$$
>\begin{align}
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0.\\\\
>\end{align}
>$$

등호에 대한 dual variable $$u$$는 조건이 없고, $$v$$는 부등호에 대한 dual variable이기 때문에 양수라는 조건이 추가됨을 기억하자.
마지막 식을 정리하여 primal LP의 objective function을 나타내면, dual LP가 된다.

>$$
>\begin{align}
>u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0 \\\\
>\underbrace{(-A^{T}u-G^{T}v)^{T}}_{=c^{T}}x\geq-b^{T}u-h^{T}v \\\\
>\text{Lower bound is} -b^{T}u-h^{T}v \\\\ 
>\text{for } x \text{ primal feasible, and any u, v satisfies,} \\\\
>c = -A^{T}u-G^{T}v \\\\
>v\geq 0. \\\\
>\end{align}
>$$

즉, $$c = -A^{T}u-G^{T}v$$ 일 때, primal의 optimal value는 $$-b^{T}u-h^{T}v$$의 하한을 가진다.

결과적으로, dual LP는 다음과 같이 정의할 수 있다.

>$$
>\begin{align}
>&\max_{u,v} &-b^{T}u-h^{T}v \\\\
>&\text{subject to} &c = -A^{T}u-G^{T}v \\\\
>& &v\geq 0.
>\end{align}
>$$

