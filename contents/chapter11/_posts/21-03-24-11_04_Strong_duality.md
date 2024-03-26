---
layout: post
title: 11-4 Strong duality
chapter: "11"
order: 5
owner: "Wontak Ryu"
---

어떤 문제에서 $$f^* = g^*$$를 만족하면 이를 **strong duality**라 한다. **Slater 조건**은 strong duality를  만족하기 위한 충분조건이다. 

## Slater 조건: 
만약 primal 문제가 convex이고  strictly feasible한 $$x \in \mathbb{R}^n$$가 하나 이상 있으면 strong duality가 만족된다.
>
$$
\begin{equation}
h_1(x)<0,\dots,h_m(x)<0, \text{ and } l_1(x) = 0,\dots,l_r(x) = 0,
\end{equation}
$$

Important Refinement : Strict inequality는 affine인 경우에는 만족하지 않아도 된다.
## Example: Support Vector Machine Dual 
$$y \in \{-1,1\}^n$$, $$X \in \mathbb{R}^{n \times p}$$ ($$X$$의 열은 $$x_1, ..., x_n$$)라고 할 때, SVM(Support Vector Machine) 문제는 다음과 같이 정의된다.

>
$$
\begin{alignat}{1}
\min_{\beta, \beta_0, \xi} & \quad \frac{1}{2}\parallel\beta\parallel_2^2 + C \sum_{i=1}^n \xi_i   \\\\
                                  s.t. & \quad \xi_i \geq 0, i=1,\dots,n   \\\\
                                       & \quad y_i(x_i^T \beta + \beta_o) \geq 1 - \xi_i, i=1,\dots,n
\end{alignat}
$$

Dual 변수, $$v, w \geq 0$$를 사용하여 Lagrangian을 정의해보자.
>
\begin{equation}
L(\beta,\beta_0,\xi,v,w) = \frac{1}{2} \parallel\beta\parallel\_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i +  \sum_{i=1}^n w_i (1-\xi_i - y_i(x_i^T\beta + \beta_o))
\end{equation}


$$\beta, \beta_0, \xi$$에 대해 최소화해서 다음과 같은 Lagrangian dual function을 구할 수 있다.
>
$$
g(v,w) = 
\begin{cases}
-\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw, &\text{if $w=C1-v, w^Ty=0$} \\\\
-\infty, &\text{otherwise}
\end{cases}
$$

여기서 $$\tilde{X}=\text{diag}(y) X$$임. 따라서, SVM dual 문제는 (slack 변수 $$v$$를 제거하면) 아래와 같이 된다. 
>
$$
\begin{alignat}{1}
\max_{w}  & \quad -\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw \\\\
     s.t. &  \quad 0 \leq w \leq C1, w^Ty = 0
\end{alignat}
$$

Primal 문제가 slater조건을 만족하므로 strong duality가 성립된다. (즉, Objective function이 convex이고 inequality constraint가 $$\beta, \beta_0, \xi$$에 대해 affine이므로 slater 조건을 만족한다.)



