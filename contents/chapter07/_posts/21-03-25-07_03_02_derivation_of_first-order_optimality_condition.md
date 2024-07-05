---
layout: post
title: 07-03-02 Derivation of First-Order Optimality Condition
chapter: "07"
order: 8
owner: "Kyeongmin Woo"
---

만약 $$f$$가 볼록함수이고 미분가능하면, subgradient 최적 조건은 first-order 최적 조건과 일치함을 아래와 같이 증명할 수 있다. 

#### Proof
>
$$
\begin{alignat}{2}
f(x^{*}) = \min_{x\in C} f(x)  \quad & \Longleftrightarrow & & \quad f(x^{*}) = \min_x f(x) + I_C(x) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \partial(f(x^{*}) + I_C(x^{*})) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \{\nabla f(x^{*}) \} + \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*}) \in \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*})^Tx^{*} \geq -\nabla f(x^{*})^Ty, \text{ for all }  y \in C \\                      
					  \quad & \Longleftrightarrow & &\quad \nabla f(x^{*})^T(y-x^{*}) \geq 0, \text{ for all } y \in C 
\end{alignat}
$$