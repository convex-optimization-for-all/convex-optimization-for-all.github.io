---
layout: post
title: 20-03 Augmented Lagrangians
chapter: "20"
order: "07"
owner: "Hooncheol Shin"
---

Dual ascent의 단점은 수렴을 보장하기 위해 강한 조건이 필요하다는 것이다. (수렴을 보장하려면 $$f$$가 strongly convex해야 했다.) 이런 단점은 **Augmented Lagrangian method** (또는 **Method of multipliers**)에 의해 개선될 수 있다. 

Primal 문제를 아래와 같이 변환한다. 
>\begin{equation}
\min_x f(x) + \frac{\rho}{2} \lVert Ax - b \rVert _2^2 \quad \text{ subject to } \quad Ax = b
\end{equation}

여기서 $$\rho > 0$$이다. $$A$$가 full column rank를 갖는다면 목적식은 strongly convex하다. 이는 원래의 문제와 정확히 동일한 문제가 된다. (Augmented term인 $$Ax - b$$는 0이 되기 때문이다.)

## Augmented Lagrangian Method
**Dual gradient ascent** : $$k=1,2,3,\dots$$에 대해 다음을 반복한다. 
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg\min_x f(x) + (u^{(k-1)})^T A x + \frac{\rho}{2} \lVert Ax - b \rVert_2^2  \\
> u^{(k)} & = u^{(k-1)} + \rho (A x^{(k)} - b)
> \end{alignat}
> $$

위 dual 알고리즘에서 $$\rho$$는 step size 역할을 한다, 즉 $$t_k=\rho$$이다. 이것은 다음에서 그 이유를 알 수 있다. 

#### $$\rho$$가 step size일 때 optimality 증명

$$x^{(k)}$$는 $$f(x) + (u^{(k-1)})^T Ax + \frac{\rho}{2} \lVert Ax - b\rVert _2^2$$ 를 최소화하므로, 
원래 primal 문제에 대한 stationary 조건에 따라, $$x^{(k)}$$에서 목적식의 subgradient가 아래와 같이 $$0$$을 포함해야 한다. 

> $$
> \begin{alignat}{1}
> 0 & \in \partial f(x^{(k)}) + A^T (u^{(k-1)}) + \rho (A x^{(k)} -b))  \\
>   & = \partial f(x^{(k)}) + A^T u^{(k)}
> \end{alignat}
> $$

위식에서, $$u^{(k)} = u^{(k-1)} + \rho (A x^{(k)} - b)$$로 동작하게 되면, 적당한 조건하에서 $$Ax^{(k)}-b$$가 $$0$$으로 가까워지면서 feasible한 해를 제공하기 시작하고, 궁극적으로 KKT 조건이 만족되고, $$x^{(k)}$$와 $$u^{(k)}$$가 optimality에 근접함을 보일 수 있다.  

**Augmented Lagrangian method**의 장점은 훨씬 좋은 수렴성을 갖는다는 것이고, 단점은 문제를 분해할 수 있는 decomposability를 잃는다는 것이다.
