---
layout: post
title: 13-04-02 Conjugates and dual problems
chapter: "13"
order: 7
owner: "Wontak Ryu"
---

다음과 같은 Lagrangian의 최소화 문제의 Dual 문제 유도를 통해 종종 Conjugate를 나타낼 수 있다.

> $$−f^{∗}(u) = \min_x f(x)−u^Tx$$

  예를 들면, 다음과 같은 수식을 고려해 보자

> $$ \min_x  f(x) + g(x)$$

다음 수식은 위 수식에 제약 조건이 추가되었으며 위식과 동치이다.

> $$ \min_{x,z} f(x) + g(z) \text{ subject to } x = z $$

이를 라그랑지 듀얼 함수로 바꾸면 아래와 같다.

> $$g(u) = \min_{x,z} f(x) + g(z) + u^T(z−x) = −f^{∗}(u)−g^{∗}(−u)$$

따라서 처음 수식의 dual 문제는 아래와 같이 정의 할 수 있다.
> $$ \max_u −f^{∗}(u)−g^{∗}(−u)$$

##### [Examples]
• Indicator function: $$ \min_x f(x) + I_C(x)$$의 dual은 다음과 같다.
> $$ \max_u −f^{∗}(u)−I^{∗}_C(−u)$$
> 
> where $$I^{∗}_C$$ is the support function of $$C$$

• Norms: 

$$ \min_x f(x) + \rVert x \rVert \text{의 dual은 다음과 같다.}$$
$$ \max_u −f^{∗}(u) \text{ subject to } \rVert u \rVert^{∗} ≤ 1 \text{ where } \rVert · \rVert_{∗} \text{ is the dual norm of } \rVert · \rVert$$
