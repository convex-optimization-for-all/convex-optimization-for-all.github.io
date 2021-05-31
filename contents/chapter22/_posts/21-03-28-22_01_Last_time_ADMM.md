---
layout: post
title: "22-01 Last time: ADMM"
chapter: "22"
order: "02"
owner: "YoungJae Choung"
---


## Last time: ADMM
다음과 같은 최적화 문제를 고려해보자
> $$ min_{x,z} f(x) + g(z)\qquad \text{ subject to } Ax + Bz = c $$

이를 Augmented Lagrangian 형식으로 바꾸어 보면 아래와 같다. (for some $$ρ > 0$$)
> $$ L_ρ(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{ρ}{2} \| Ax + Bz − c \|^2_2$$

위 식은 $$\frac{ρ}{2} \| Ax + Bz − c \|^2_2$$가 추가 됨으로 Strongly Convex가 되며, 이를 다음 수식과 같이 병렬 처리에 유용한 형태로  바꿀 수 있다.
* 자세한 증명은 앞장의 내용을 참고하기 바란다.
ADMM: for $k = 1, 2, 3, . . .$
> $$x^{(k)} = argmin_{x} L_ρ(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = argmin_{z} L_ρ(x^{(k)}  , z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + ρ(Ax^{(k)} + Bz^{(k)} − c)$$
 
## ADMM in scaled form
dual variable $$u$$를 scaled variable $$w = u/ρ$$로 바꾸어 보자. 여기서 ADMM step은 다음과 같이 계산 가능하다.

> $$x^{(k)} = argmin_{x} f(x) + \frac{ρ}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = argmin_{z} g(z) + \frac{ρ}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$
