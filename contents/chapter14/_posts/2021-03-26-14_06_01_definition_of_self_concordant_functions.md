---
layout: post
title: 14-06-01 Definition of self-concordant functions
chapter: "14"
order: 11
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>
## Self-concordant on $$R$$
Convex 함수 $$f : R \rightarrow R$$ 은 아래의 식을 만족할때 self-concordant 하다고 정의한다.
>$$\begin{align}
>\|f^{'''}(x)\| \leq 2f^{''}(x)^{3/2} \qquad \text{for all }x\in \text{dom }f.
>\end{align}$$

쉬운 예시로, 선형 함수($$ax+b$$), (convex한) 2차 함수는 3계도함수(3차 미분) 값이 0이므로, self-concordant하다.

## Self-concordant on $$R^{n}$$
$$f : R^{n}\rightarrow R$$은 정의역 안에서 임의의 방향의 선분 영역에 대하여, 다시 말해 정의역에 포함되는 모든 방향의 선분 영역에 대하여, self-concordant 할 때 이 함수를 self-concordant하다고 정의한다. 예를 들어, 모든 $$x\in dom\, f$$ 와 모든 $$v$$에 대하여, $$g(t) = f(x+tv)$$로 정의될 떄, $$g(t)$$가 self-concordant하면, f를 domain of $$\mathbb{R}^{n}$$에서 self-concordant function이라고 정의한다.

## Example of self-concordance function

1) $$f : \mathbb{R}^{n}_{++}\rightarrow \mathbb{R}$$, $$f(x) = -\sum^{n}_{i=1}log(x_{i})$$.

$$f(t) = -\log{t}$$ 임은 쉽게 확인할 수 있다. 더불어 self-concordant 함수의 합 또한 self-concordant 함을 이용한다. Self-concordant한 함수 $$f_{1}, f_{2} : R\rightarrow R$$이 있다고 할 때, self-concordant 함수의 합 또한 self-concordant 함은 다음과 같이 보인다.[3]
>$$\begin{align}
>|f_{1}^{'''}(x)+f_{2}^{'''}(x)|  \leq & |f^{'''}_{1}(x)|+|f^{'''}_{2}(x)|\\\\
> \leq &2\big( f^{''}_{1}(x)^{3/2}+f^{''}_{2}(x)^{3/2}\big)\\\\
>\leq &2\big( f^{''}_{1}(x)+f^{''}_{2}(x) \big)^{3/2}.
>\end{align}$$

맨 마지막 단계의 경우 아래의 성질을 이용한다.
>$$\begin{align}
>(u^{3/2}+v^{3/2})^{2/3} \leq u+v, \qquad u, v \geq 0.
>\end{align}$$

