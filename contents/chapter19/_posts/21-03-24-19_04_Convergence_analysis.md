---
layout: post
title: 19-04 Convergence analysis
chapter: "19"
order: 8
owner: "Hooncheol Shin"
---

Proximal newton method의 수렴을 분석하기 위해 Lee (2014) [1] 논문의 증명을 따를 것이다.

[1] J. Lee and Y. Sun and M. Saunders (2014), Proximal Newton-type methods for minimizing

수렴을 증명하기 위해 다음과 같이 가정한다.

* $$f = g + h$$, $$g$$와 $$h$$는 convex이고 $$g$$는 2차 differentiable (smooth)
* $$mI \preceq \nabla^2 g(x) \preceq LI$$.
* $$\nabla^2 g(x)$$ Lipschitz with constant $$M$$
* $$\text{prox}_H(\cdot)$$는 정확히 계산 가능

위에 세가지 가정은 strictly convex라는 것을 의미하며 $$\text{prox}_H(\cdot)$$가 정확히 계산이 가능하다고 가정한 것은 실제 이렇게 되기가 쉽지 않기 때문이다.
 
## Convergence Theorem

> **Proximal newton method**는 backtracking line search를 이용해서 global하게 수렴한다.
> \begin{align}
\parallel x^{(k)} - x^{\star} \parallel_2 \le \frac{M}{2m} \parallel x^{(k-1)} - x^{\star} \parallel_2^2
\end{align}

이것을 **local quadratic convergence**라고 한다. $$k \ge k_0$$이후에 $$f(x^{(k)}) - f^{\star} \le \epsilon$$을 만족하기 위해서는 $$O(\log \log (1/\epsilon))$$의 반복이 필요하다. 단, 각 반복에서 scaled prox를 사용한다.

## Proof sketch
**Global convergence**를 보이기 위해서는 어떤 step에서도 다음과 같은 step size $$t$$에 대해 backtracking exit condition을 만족함을 보일 수 있다.

> \begin{align}
t \le \min \left\\{ 1, \frac{2m}{L} (1-\alpha) \right\\} \\\\
\end{align}

이 식으로 global minimum에 도달했을 때인  update direction이 0으로 수렴한다는 것을 보일 수 있다

**Local quadratic convergence**를 보이기 위해 충분히 여러번 반복하게 되면 pure newton step $$t=1$$은 backtracking exit conditions을 만족하여 다음 식이 성립된다.

> $$
> \begin{align}
> \parallel x^{+} - x^{\star} \parallel_2 & \le \frac{1}{\sqrt(m)} \parallel x^{+} - x^{\star} \parallel_H \\\\
> & =  \frac{1}{\sqrt(m)} \parallel \text{prox}_H(x - H^{-1} \nabla g(x) )  - \text{prox}_H(x^{\star} - H^{-1} \nabla g(x^{\star}) )  \parallel_H \\\\
> & \le \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2 \\\\
> \end{align}
> $$

이를 정리해 보면 다음과 같다.

> \begin{align}
\parallel x^{+} - x^{\star} \parallel_2 \ \le \ \frac{1}{\sqrt(m)} \parallel x^{+} - x^{\star} \parallel_H \  \le \ \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2
\end{align}

* 첫번째 부등식은 lowest eigenvalue bound에 대해 성립하며 등식은 $$x^+$$ 정의와 global minimum $$x^{\star}$$에서 $$\text{prox}_H(\cdot)$$이 identity가 된다는 사실에 의해 성립한다.

* 두번째 부등식은 proximal operator의 nonexpansiveness, Lipschitz assumption, largest eigenvalue bound에 의해 성립한다.
