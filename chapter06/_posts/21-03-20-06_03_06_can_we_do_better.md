---
layout: post
title: 06-03-06 Can we do better?
chapter: "06"
order: 12
owner: "Kyeongmin Woo"
---

# Can we do better?

Gradient descent는 Lipschitz gradients를 가지며 convex이고 differentiable한 함수로 표현되는 문제에 대해 $$O(1/\epsilon)$$ 수렴 속도를 갖는다. Gradient descent보다 더 빠른 first-order method가 있을까?

#### First-order method
First-order method는 $$x^{(k)}$$번째 반복에서 다음과 같이 변경을 표현할 수 있다. 따라서, $$x^{(k)}$$번째 반복에서의 변경은 초기 위치 $$x^{(0)}$$와 $$x^{(0)}$$에서 $$ x^{(k−1)}$$까지의 gradient span으로 표현된다.

> $$x^{(0)} + $$ **span**$$\{∇f(x^{(0)}),∇f(x^{(1)}),...,∇f(x^{(k−1)})\}$$

####  Theorem (Nesterov)
Nesterov theorem은 first-order method의 수렴에 대한 lower bound를 제시한다.

> **Nesterov Theorem** 임의의 $$k ≤ (n−1)/2$$와 시작점 $$x^{(0)}$$에 대해, 임의의 first-order method가 다음 조건을 만족하게 하는 함수 $$f$$가 존재한다. ($$n$$은 차원을 의미한다.)<br>
\begin{align}
f(x^{(k)})−f^{\star} ≥ \frac{3L \lVert x^{(0)} −x^{\star} \rVert_2^2}{32(k + 1)^2 }\\\
\end{align}

Nesterov theorem의 lower bound의 분모에 $$k^2$$이 있으므로 수렴 속도 $$O(1/k^2)$$가 된다. 그리고, 반복 회수는 $$O(1/\sqrt{\epsilon})$$가 된다. 이에 대한 내용은 나중에 자세히 살펴볼 것이다.