---
layout: post
title: 13-04-03 Shifting linear transformations
chapter: "13"
order: 8
owner: "Wontak Ryu"
---

Dual formulation은 목적 함수의 일부와 또 다른 영역 사이의 선형 변환의 shifting으로 도움이 된다.

다음을 살펴보자
> $$ \min_x f(x) + g(Ax)$$

아래 수식은 위의 식과 동치 이다.
> $$min_{x,z} f(x) + g(z) \text { subject to } Ax = z$$

이는 다음의 유도 과정을 거친다.
> $$\text {g(u)} = \min_{x,z} f(x) + g(z) + u^T(z - Ax)$$
> $$\qquad  = -\max_{x} (A^T u)^T x - f(x) - \max_{z} (-u)^T z - g(z)  $$
> $$\qquad = -\ f^{∗} (A^T u) - g^{∗} (-u) $$

그리고 dual은 다음과 같다.
> $$\max_u −f^{∗}(A^Tu) − g^{∗}(−u)$$

##### [Example]
norm과 그 norm의 dual norm은 다음의 관계에 있다. $$\rVert · \rVert, \rVert · \rVert_{∗}$$, the problems 

> $$ \min_x f(x) +\rVert Ax \rVert$$
> $$ \max_u −f(A^Tu) \text{ subject to } \rVert u \rVert_{∗} ≤ 1$$

첫번째 수식은 primal이며 두번째 수식은 dual로, 쌍으로 나타내어 질 수 있다.
