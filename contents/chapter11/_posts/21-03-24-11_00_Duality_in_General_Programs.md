---
layout: post
title: 11 Duality in General Programs
chapter: "11"
order: "01"
owner: "Wontak Ryu"
---

### Review: duality in linear program

$$c \in \mathbb{R}^n$$, $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$, $$G \in \mathbb{R}^{r \times n}$$, $$h \in \mathbb{R}^r$$ 일 때, 

##### Primal LP: 
>
$$
\begin{alignat}{1}
min_{x} & \quad c^T x   \\\\ 
  s.t.   & \quad Ax = b  \\\\
         & \quad Gx \leq h 
\end{alignat}
$$


##### Dual LP: 
>
$$
\begin{alignat}{1}
max_{u,b} & \quad -b^T u - h^T v   \\\\
         s.t. & \quad - A^T u - G^T v = c  \\\\
             & \quad v \geq 0 
\end{alignat}
$$

#### Explanantion 1: 

모든 $$u$$와 $$v \geq 0$$, 그리고 primal feasible $$x$$에 대해 다음이 성립된다. 
>
$$
\begin{equation}
u^T (Ax-b) + v^T(Gx-h) \leq 0
\end{equation}
$$

즉,

>
$$
\begin{equation}
(-A^Tu - G^Tv)^T x \geq -b^Tu - h^T v
\end{equation}
$$

위 관계에 의해, 만약, $$c=-A^Tu - G^Tv$$이면, primal 최적해에 대한 lower bound를 얻을 수 있다. 


#### Explanation 2: 

모든 $$u$$와 $$v \geq 0$$, 그리고 primal feasible $$x$$에 대해,

>
$$
\begin{equation}
c^T x \geq c^T x + u^T (Ax-b) + v^T (Gx -h) := L(x,u,v)
\end{equation}
$$

그래서, 만약 $$C$$가 primal feasible set이고, $$f^*$$가 primal 최적해라면, 

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

다시말해, $$g(u,v)$$는 $$f^*$$에 대한 lower bound이다. 

>
$$
g(u,v) =
\begin{cases}
-b^T u - h^T v & \text{if $c=-A^Tu - G^T v$} \\\\
-\infty            & \text{otherwise} 
\end{cases}
$$

두번째 설명은 첫번째와 같은 dual을 가져오지만, completely general하고 (convex하지 않은 문제를 포함한) 임의의 모든 최적 문제에 적용된다.