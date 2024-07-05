---
layout: post
title: 13-06 Dual subtleties & Double dual
chapter: "13"
order: 10   
owner: "Wontak Ryu"
---

## Dual subtleties
• 때로는 우리는 dual 문제를 동치의 문제로 바꿀 수 있고 이를 여전히 dual 문제라 부른다. 또한 Strong Duality에서, Primal 솔루션의 특징 분석이나 계산을 위해 변형된 dual 문제의 솔루션을 사용할 수 있다.

##### [주의]
변형된 dual 문제의 최적값은 반드시 primal의 최적값은 아니다.


• 제약 조건이 없는 문제에 대해 dual 문제를 유도하는 일반적인 방법은 먼저 더미 변수와 equality 제약 조건을 추가함으로써 primal을 변형시키는 것이다.

일반적으로 이것을 어떻게 하는지는 모호하다. 다양한 선택으로 다른 dual 문제들을 이끌어 낼 수 있다.


## Double dual
선형 제약 조건에서 일반적인 최소화 문제를 고려해보자

> $$ \min_x f(x) \text{ subject to } Ax ≤ b, Cx = d$$

라그랑지안은 다음과 같다.
> $$L(x,u,v) = f(x) + (A^Tu + C^Tv)^Tx−b^Tu−d^Tv$$

그러므로 dual 문제는 다음과 같다.

> $$ \max_{u,v} −f^∗(−A^Tu−C^Tv)−b^Tu−d^Tv \text{ subject to } u ≥ 0 $$

##### Recall property
만약 $$f$$가 closed이고 convex라면, 이 경우에 dual의 dual은 primal임을 앞서 설명하였다.($$f^{∗∗} = f$$)

실제로, 선형 제약 조건을 넘어(dual과 dual의 conjugate 사이의)연결이 이보다 훨씬 더 깊다.
다음을 살펴보자

> $$ 
>\begin{align}
> & \min_x && f(x) \\
> &\text{ subject to } && h_i(x) ≤ 0, i = 1,...m \\
> &&&l_j(x) = 0, j = 1,...r
> \end{align}$$


$$f$$와 $$h_1,...h_m$$가 closed이고 convex이고, $$1,...r$$ 은 affine이면, then dual의 dual은 primal이다.

이것은 bifunction의 관점에서 최소화 문제로 제공되어 진다.
이 프레임 워크에서 dual 함수는이 dual 함수의 conjugate에 해당 한다.

(for more, read Chapters 29 and 30 of Rockafellar)
