---
layout: post
title: 10-04 Another Perspective on LP duality
chapter: "10"
order: "05"
owner: "Wontak Ryu"
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
앞에서 다룬 duality의 경우, LP에 대하여, primal 문제의 constraint에 dual variable을 곱하고, 이들의 선형 결합(linear combination)을 구한 뒤, 정리하여 primal의 objective function을 분리해내어 bound를 구하는 형태였다. 분리된 나머지 항(아래 수식의 something)이 primal 문제의 bound 역할을 하였다. 즉, dual 문제의 objective function이 되고, 수식 전개 과정에서 만들어진 조건들이 dual 문제의 constraint가 되었다.
이 일부 과정(위의 내용 중 primal objective function을 분리해 내어 bound를 구하는 부분)을 수식으로 적어보면 다음과 같다.

>$$
>\begin{align}
>&\min_{x} &f(x)\\\\
>&\text{subject to} &Ax = b\\\\
>& &Gx \leq h\\\\
>\end{align}
>$$

>$$
>\begin{align}
>& &\text{for any }u,\, v\geq 0,\\\\
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0\\\\
>&{\approx} &f(x)+\text{something}. \\\\
>\end{align}
>$$

하지만 linear program이 아닌 최적화 문제의 경우, 대부분이 constraint의 선형 결합으로 objective function을 표현할 수 없다. 

이 장에서는 좀 더 보편적으로 통용되는 문제(모든 convex, 대부분의 non-convex)에 적용가능한 duality의 관점에 대해 살펴본다. lagrangian으로 불리는 이 방법으로 LP의 duality를 구하고, 좀 더 자세한 논의에 대해서는 11장에서 살펴보자.

위에 서술되었던 primal LP 문제에 대하여 선형 결합 형태까지의 식을 보게 되면, 다음과 같은 관계를 알 수 있다.
>$$
>\begin{align}
>c^{T}x\geq c^{T}x+\overbrace{u^{T} \underbrace{(Ax-b)} _ {=0}+\underbrace{v^{T}} _ {\geq 0} \underbrace{(Gx-h)} _ {\leq 0}} ^ {\leq 0} := L(x,u,v).
>\end{align}
>$$

부등호의 우항은 조건들에 의하여 좌항보다 작거나 같은 값을 가진다. 또한 이 식을 $$L(x, u, v)$$라는 x, u, v에 대한 함수로 정의한다.
여기서 primal LP의 constraint를 만족하는 집합(primal feasible set)을 C라 칭하면, 다음과 같은 관계를 알 수 있다.

>$$
>\begin{align}
>C =  \{ x: Ax=b, Gx\leq h \},
>\end{align}
>$$
>$$
>\begin{align}
>f^{*}=\min_{x\in C} f(x) \geq \min_{x\in C}L(x,u,v)\geq \min_{x}L(x,u,v):=g(u,v).\\\\
>\end{align}
>$$

다시말해서, $$g(u,v)$$는 어떤  u나 $$v\geq0$$을 만족하는 $$v$$에 대해서 $$f^{*}$$의  Lower bound가 된다.
이때 $$g(u,v)$$로 결정되는 Lower bound 값을 살펴보자.

>$$
>\begin{align}
g(u,v) = min_{x} c^{T}x+u^{T}(Ax-b) + v^{T}(Gx-h) \\\\
= \min_{x} (c+A^{T}u+G^{T}v)^{T}x - b^{T}u-h^{T}v \\\\
\begin{cases}= -b^{T}u-h^{T}v \qquad &\text{if }\ c = -A^{T}u-G^{T}v \\\\
-\infty \qquad &\text{otherwise}.
\end{cases}
>\end{align}
>$$


식에서도 알 수 있다시피, $$c = -A^{T}u-G^{T}v$$를 만족하지 않을 때엔 $$x$$항으로 인하여 $$-\infty$$의 값을 갖는다.
우리는 $$f^{*}$$에 가장 가까운 Lower bound를 찾길 원하므로, $$g(u, v)$$를 Maximize(최대화)하는 값을 찾고자 한다. 이는 $$c = -A^{T}u-G^{T}v$$를 만족할때의 값인 $$-b^{T}u-h^{T}v$$이고, 이는 우리가 첫 번째 방법으로 구했던 Dual LP와 일치한다.

>$$
>\begin{align}
>f^{*} \geq g(u,v), \qquad \text{provided } v \geq 0\\\\
>\text{find the biggest lowerbound  } g(u,v)\\\\
>\max_{u,v} g(u,v)\\\\
>\text{s.t. }v \geq 0. 
>\end{align}
>$$

이 방법은 LP형태가 아닌 다른 형태의 최적화 문제에 대해서도 적용 가능하다.