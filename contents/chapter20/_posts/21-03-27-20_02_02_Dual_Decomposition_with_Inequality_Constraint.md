---
layout: post
title: 20-02-02 Dual Decomposition with Inequality Constraint
chapter: "20"
order: "06"
owner: "Hooncheol Shin"
---

다음의 문제를 생각해 보자. 앞의 문제와 다른점은 제약식이 부등식의 관계를 갖는 것이다. 
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Dual decomposition (projected subgradient method) 
위 문제에서는 dual 변수가 항상 $$0$$보다 같거나 커야 한다, 즉 $$u \geq 0$$. 따라서, 다음 스텝의 $$u$$값을 계산할 때, $$0$$보다 큰 범위안으로 projection을 시켜서 업데이트를 한다. 

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)_+
> \end{alignat}
> $$

여기서, $$u_{+}$$는 0보다 큰 $$u$$를 의미한다, 즉, $$(u_+)_i = \max \left\{0,u_i \right\}, i=1,\dots,m$$. 
위  과정을 $$k=1,2,3,\dots$$에 대해서 반복한다. 

#### Price coordination interpretation
일반적으로 dual decomposition 문제들은 price coordination 관점에서 다음과 같이 해석될 수 있다. (Vandenberghe)
> * $$B$$개의 독립적인 유닛이 있고, 각 유닛은 자신의 결정 변수 $$x_i$$를 결정한다. 
> * 각 제약조건은 $$B$$개의 유닛이 공유하고 있는 자원에 대한 제약을 의미하며, dual 변수 $$u_j$$는 자원 $$j$$의 가격을 의미한다. 
> * Dual 변수는 아래와 같이 업데이트되며
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ 여기서, $$s=b-\sum_{i=1}^B A_ix_i$$는 슬랙 변수로써 \\
> $$\qquad$$ - $$s_j < 0$$이면, 자원 $$j$$가 over-utilized 되고 있다는 의미이고, 따라서, price $$u_j$$를 증가시킨다 \\
> $$\qquad$$ - $$s_j > 0$$이면, 자원 $$j$$가 under-utilized되고 있다는 의미이고,  따라서, price $$u_j$$를 감소시킨다 \\
> $$\qquad$$ - price는 향상 음수가 되지 않도록 한다.
