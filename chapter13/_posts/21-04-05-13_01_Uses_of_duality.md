---
layout: post
title: 13-01 Uses of duality
chapter: "13"
order: 2
owner: "Wontak Ryu"
---

### Two key uses of duality
앞서 11장에서 다룬 duality의 두가지 핵심적인 특징에 대해 다시 살펴보자.

• $$x$$가 primal feasible 이고 $$u,v$$가 dual feasible 일 때, primal 문제 $$f(x)$$와 dual 문제 $$g(u,v)$$ 간의 차이를 $$x$$와 $$u,v$$간의 **duality gap**이라 부른다. 
> $$f(x)-f^{\star}  \le f(x)-g(u, v)$$

duality gap이 0일 때 이를 zero duality gap이라 하며 이는 dual 문제의 해가 optimal임을 의미 한다.
또한 upper bound인 $$g(u, v)$$는 최적값인 $$f^{\star}$$보다는 항상 작거나 같다. 자세한 이유는 앞의 [[11장]](/chapter11/)의 내용을 참고하기 바란다.
따라서 아래와 같이 유도가 가능하다.

##### [Proof]
> $$f^{\star} \ge g(u, v) \\$$
> $$-f^{\star} \le -g(u, v) \\$$
> $$f(x)-f^{\star} \le \underbrace{f(x)-g(u, v)}_{\text{dualityh gap}}\\$$
> also, \\
> $$g^{\star}-g(x) \le \underbrace{f(x)-g(u, v)}_{\text{dualityh gap}}\\$$


그리고, duality gap은 알고리즘의 중지 기준(stopping criterion)으로 사용될 수도 있다. 

• Dual optimal $$u^{\star}, v^{\star}$$이 주어졌을 때 Strong duality의 조건하에서, primal solution은 모든 $$x$$에 대해 라그랑지안 $$L (x, u^{\star}, v^{\star})$$을 최소화 시킨다. (즉, stationarity condition을 만족시킨다).

이를 primal solution 계산에 이용할 수 있다.