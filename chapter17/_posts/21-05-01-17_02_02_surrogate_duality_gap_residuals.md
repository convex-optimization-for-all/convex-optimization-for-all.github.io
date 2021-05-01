---
layout: post
title: 17-02-02 Surrogate duality gap, residuals
chapter: "17"
order: 5
owner: "Minjoo Lee"
---
Primal-Dual 알고리즘을 정의하기 위해 먼저 세 가지 residual 종류와 surrogate duality gap을 정의해보자. Residual과 surrogate duality gap은 Primal-Dual 알고리즘에서 최소화해야 할 목표이다.

## Residuals
$(x,u,v)$에서의 dual, central, primal residual는 다음과 같이 정의된다. 

> $$r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv$$
> $$r_{cent} =  Uh(x) + τ\mathbb{1}$$ 
> $$r_{prim} = Ax−b$$

이들은 함수 $r(x,u,v)$의 각 row에 해당된다. **Primal-dual interior point method**는 이 세 가지 residual이 계속해서 0이 되게하기 보다는 0을 만족하는 방향으로 실행한다. 즉, 실행 과정에서 반드시 feasible일 필요는 없다는 이야기이다.

$r_{dual}$를 dual residual이라고 부르는 이유는 아래 식에서와 같이 $r_{dual} = 0$이면 $u, v$가 $g$의 domain에 있다는 것을 보장하게 되며 이는 곧 dual feasible임을 의미하기 때문이다.

>\begin{align}
& r_{dual} = \nabla f(x) +\nabla h(x)u + A^Tv = 0 \\\\
& \iff \min_{x} L(x,u.v) = g(u,v) \\\\
\end{align}

비슷하게 $r_{prim}=0$을 만족하면 primal feasble하기 때문에 $r_{prim}$을 primal residual이라고 부른다.

## Surrogate duality gap
Barrier method는 feasible하기 때문에 duality gap이 존재하지만, primal-dual interior-point method는  반드시 feasible할 필요가 없기 때문에 **surrogate duality gap**을 사용한다. **Surrogate duality gap**은 다음 식으로 정의된다.

> $$−h(x)^Tu  \quad \text{for} \quad h(x) \le 0, u \ge 0$$ 

만일 $r_{dual} = 0$이고  $r_{prim} = 0$라면 surrogate duality gap은 true duality gap이 된다. 즉, primal and dual feasible하면 surrogate duality gap은 실제 duality gap $\frac{m}{t}$과 같아진다.

**[참고] Perturbed KKT 조건과 파라미터 t** <br>

* Perturbed KKT 조건에서 파라미터 t는 $t = −\frac{m}{h(x)^Tu}$이다. 
* 자세한 내용은 [15-03-01 Perturbed KKT conditions](https://wikidocs.net/21311)와 [15-03-02 Suboptimality gap](https://wikidocs.net/21312)을 참조

그리고, $u > 0,h(x) < 0$이고 아래의 조건을 만족하면 $(x,u,v)$는 central path 상에 존재하게 된다.

> $r(x,u,v) = 0$ for $\tau = -\frac{h(x)^Tu}{m}$

즉, central path 상에 존재하는 점에서 residual은 0이다.

