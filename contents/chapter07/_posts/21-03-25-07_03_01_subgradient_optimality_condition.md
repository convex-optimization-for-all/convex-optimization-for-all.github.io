---
layout: post
title: 07-03-01 Subgradient Optimality Condition
chapter: "07"
order: "07"
owner: "Kyeongmin Woo"
---

# Subgradient Optimality Condition

### Lemma 

모든 함수 $$f$$에 대해서, 어떤 $$x^*$$에서 함수의 최소값을 갖는 것과 $$x^*$$에서 subgradient가 $$0$$인 것은 서로 필요충분조건이다.   

> $$
\begin{equation}
f(x^*) = \min_x f(x) \Longleftrightarrow 0 \in \partial f(x^*)
\end{equation}
$$

### Proof
>
$$
\begin{align}
&f(x^*) = \min_x f(x)\\
\Longleftrightarrow &f(y) \geq f(x^*) \text{ for all } y\\
\Longleftrightarrow &f(y) \geq f(x^*) + 0^T(y-x^*)\\
\Longleftrightarrow &0 \in \partial f(x^*)
\end{align}
$$

위 증명에서 함수 $$f$$에 대한 볼록성은 전혀 이용되지 않았으며, 따라서 비볼록함수에서도 예외없이 적용되는 최적 조건이라고 할 수 있다.  

