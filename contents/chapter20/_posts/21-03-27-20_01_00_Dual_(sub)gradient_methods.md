---
layout: post
title: 20-01 Dual (sub)gradient methods
chapter: "20"
order: 2
owner: "Hooncheol Shin"
---

Close-form 형태의 dual (conjugate)을 찾을 수 없는 경우에도 dual 기반의 subgradient 또는 gradient method를 사용할 수 있다.

예를 들어, 다음의 문제를 보자. 
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

위 문제의 dual 문제는 아래와 같다. 여기서 $$f^{\ast}$$는 $$f$$의 conjugate이다.
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

이때, $$g(u)$$를 $$-f^{\ast}(-A^Tu)-b^Tu$$로 정의하면 $$g(u)$$의 subgradient는 다음과 같다.
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

위 식에서 $$\partial f^{\ast}(-A^Tu)$$를 $$x$$로 정리하면 아래와 같이 표현될 수 있다. 

>\begin{equation}
\partial g(u) = Ax-b \quad \text{where} \quad x \in \arg\min_z f(z) + u^T A z
\end{equation}

## Dual subgradient method
**Dual subgradient method**는 dual 문제의 목적식을 최대화하기 위해 시작점 $$u^{(0)}$$에서 시작해서 $$k=1,2,3,\dots$$에 대해 다음 단계를 반복한다.
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)} - b) 
> \end{alignat}
> $$

여기서 step size $$t_k(k=1,2,3,\dots$$)는 표준적인 방식으로 선택된다. 

#### Strictly Convex인 경우
만약 $$f$$가 strictly convex라면 $$f^{\ast}$$는 미분가능해진다. 

따라서, 알고리즘은 $$k=1,2,3,\dots$$에 대해 다음 단계를 반복하는 **dual gradient ascent**가 된다.
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)}-b) 
> \end{alignat}
> $$

이전 방식과 다른 점은 $$x^{(k)}$$가 유일하다는 것이다. ($$\text{argmin}$$과의 관계가 $$=$$ 관계임을 확인해보라.)

여기서 step size $$t_k(k=1,2,3,\dots$$)도 표준적인 방식으로 선택되며 $$\text{argmin}$$을 수행할 때 proximal gradient나 acceleration도 평소처럼 적용할 수 있다.
