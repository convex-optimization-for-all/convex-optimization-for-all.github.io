---
layout: post
title: 18-02 Symmetric Rank-One Update (SR1)
chapter: "18"
order: "03"
owner: "Hooncheol Shin"
---

SR1 update는 rank-1의 symmetric matrix로 $$B$$를 업데이트 함으로써 $$B^+$$가 symmetry를 유지하고 secant equation을 계속해서 만족하게끔 업데이트하는 방법이다. Rank-1의 symmetric matrix가 $$a \in \left\{-1, 1\right\}$$와 $$u \in \mathbb{R^n}$$의 곱으로 분해된다고 하면 update form은 다음과 같을 것이다.

>$$B^+ = B + auu^T.$$

## Key Observation
$$a$$와 $$u$$는 $$B^+$$가 secant equation을 만족하게끔 선택되어야 한다. 그러므로 secant equation $$y = B^+s$$에 위에서 소개한 update form을 대입해보자.

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

$$(au^Ts)$$는 scalar이므로 $$u$$는 $$y-Bs$$와 임의의 scalar $$\delta$$와의 곱으로도 표현할 수 있을 것이다 $$\big( u = \delta(y - Bs) \big)$$. (1)의 $$u$$를 $$\delta(y - Bs)$$으로 치환해보자.

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

위 등식을 만족하는 파라미터 $$\delta$$와 $$a$$는 다음과 같다.

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## The Only SR1 Updating Formula
Key observation에서 얻은 정보를 활용해 유일한 형태의  SR1 update를 유도할 수 있다 ([14]의 6.2). <br/>
$$\big( u = \delta (y - Bs)$$ 와 (2)를 $$B^+ = B + auu^T$$에 대입. $$\big)$$

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$
>

## The Update Formula for the Inverse Hessian Approximation

$$x^+$$를 구하기 위해서는 $$B^{-1}$$의 계산이 필요해진다.

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

$$B$$ 대신 $$B^{-1}$$를 업데이트 할 수 있다면 매번 $$B^{-1}$$을 계산하기 위한 비용을 줄일 수 있지 않을까?

[Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula)를 이용하면 유도과정을 통해 $$B^{-1}$$ 또한 동일한 형태로 업데이트 할 수 있다는 것을 알 수 있다. ($$H = B^{-1}$$)

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Shortcomings of SR1

SR1 은 아주 간단하다는 장점이 있지만 두 가지 치명적인 단점을 가지고 있다.

1. $$(y-Bs)^Ts$$가 0에 가까워지면 업데이트에 실패할 수 있다.
2. $$B$$와 $$H$$의 positive definiteness를 유지하지 못한다.

이 뒤의 절에서는 SR1의 단점을 보완한 방법들을 소개한다. 