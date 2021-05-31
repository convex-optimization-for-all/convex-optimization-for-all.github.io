---
layout: post
title: 08-01-01 Step size choices
chapter: "08"
order: "03"
owner: "Kyeongmin Woo"
---

# Step size choices

Subgradient method에서도 다양한 방법으로 **step size**를 선택할 수 있다.  

그 중에서도 다음 2가지 방식을 자세히 살펴보도록 하자. 

- **Fixed step sizes**: $$t_k = t$$, where $$k = 1, 2, 3, ...$$
- **Diminishing step sizes**: 아래의 조건을 충족하는 $$t_k$$

>\begin{align}
> \sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^{2} < \infty
>\end{align}

#### Example of Diminishing step sizes

> $$\begin{align}
& t_k = \frac{1}{k}, k = 1,2,3,... \\
& \sum_{k=1}^{\infty}t_k = \infty \quad \text{(Harmonic  series)} \\
& \sum_{k=1 }^{\infty}t^2_k ≈ 1.644934 < \infty \quad \text{(Basel problem)} \\
\end{align} $$

Subgradient method에서 사용되는 step size는 gradient descent에서와는 달리 미리 설정 되어야 한다는 것이 특징이다. 다시 말하면 gradient descent의 backtracking line search처럼 subgradient method의 step size는 곡면의 특징에 맞게 바뀌지 않는다.
