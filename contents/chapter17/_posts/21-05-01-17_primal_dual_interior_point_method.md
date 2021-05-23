---
layout: post
title: 17 Primal-Dual Interior-Point Methods
chapter: "17"
order: 1
owner: "Minjoo Lee"
---

본 장에서는 앞서 배운 Barrier method의 centering step을 한 단계로 줄여서 성능을 개선한 **Primal-Dual Interior-Point Method**를 살펴볼 것이다. 

**Primal-Dual Interior-Point Method**는 centering step에서 반드시 feasible해야 한다는 제약조건을 완화하고  Newton's Method의 root finding 버전을 이용하여 비선형 방정식을 선형 방정식으로 근사하여 해를 구하는  방식으로 Barrier method에 비해 빠르고 정확도가 높다.

## References and further readings
* S. Boyd and L. Vandenberghe (2004), “Convex optimization,” Chapter 11
* S. Wright (1997), “Primal-dual interior-point methods,” Chapters 5 and 6
* J. Renegar (2001), “A mathematical view of interior-point methods”
* Y. Nesterov and M. Todd (1998), “Primal-dual interior-point methods for self-scaled cones.” SIAM J. Optim.