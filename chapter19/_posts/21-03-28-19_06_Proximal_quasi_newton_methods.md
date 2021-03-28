---
layout: post
title: "19-06 Proximal quasi-Newton methods"
chapter: "19"
order: 10
owner: "YoungJae Choung"
---


문제가 커질수록 Hessian의 계산 비용이 매우 높아진다. **Proximal quasi-Newton method**는 각 step에서 Hessian $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$를 계산하지 않는 방식으로 superlinear 혹은 linear convergence의 수렴 속도를 제공한다.

## Proximal quasi-Newton method
* Lee (2014)는 Hessian을  BFGS-style로 update하는 방식을 제안했다. 이 방법은 매우 잘 실행되며 local superlinear convergence의 수렴 속도를 갖는다.
* Tseng and Yun (2009)은  Hessian을 blockwise로 근사하는 방식을 제안했다. 이 방법은 $$f = g + h$$에서 $$h$$가 일부 최적화 변수에 의존하는 부분으로 나뉠 수 있을 때만 작동한다. Hessian을 blockwise로 계산하면 계산이 매우 빨라진다. 이 방법은 linear convergence의 수렴 속도를 갖는다.

Quasi-Newton은 Hessian 계산이 힘들때 뿐 아니라 Hessian이 singular이거나 near singular인 ill-condition에서도 유용하다.

#### 참고 논문
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"