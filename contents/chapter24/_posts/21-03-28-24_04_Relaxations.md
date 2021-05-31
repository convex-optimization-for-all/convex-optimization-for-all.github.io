---
layout: post
title: "24-04 Relaxations"
chapter: "24"
order: "05"
owner: "YoungJae Choung"
---

Relaxation을 위해서는 특정 조건이 성립이 되어야 하며, Convex relaxation과 Lagrangian relaxation 방법을 활용할 수 있다. 자세한 내용을 살펴보도록 하자.

## Conditions for Relaxations
일반적인 optimization problem이 다음과 같이 정의된다면,
> $$\min_{x \in X} f(x)$$

이 문제의 relaxation은 임의의 optimization problem으로 나타내었을 때, 다음과 같이 정의된다.
> $$\min_{x \in Y} g(x)$$
> such that
> $$ \quad $$ ① $$ X \subset Y \quad$$ and 
> $$ \quad $$ ② $$ g(x) \leq f(x)$$ for all $$x \in X $$ 

목적함수 $$f(x)$$ 와 $$g(x)$$가 달라지면 두 조건 모두 만족해야 하고, 같다면 조건 ①만 만족해도 될 것이다.
두 조건에 의하여, relaxation에서의 optimal value는 original problem에서의 optimal value의 lower bound가 된다.

## Convex relaxations
주어진 문제가 다음과 같을 때,
> $$
> \begin{align}
> \min_{x} & \quad f(x) \\
> \text{subject to } & \quad x \in C \\
> & \quad x_j \in \mathbb{Z}, \quad j \in J \\
> \text{where f is convex} & \quad f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

convex relaxation을 아래와 같이 표현할 수 있다.
> $$
> \begin{align}
> \min_{x} & \quad f(x) \\
> \text{subject to } & \quad x \in C \\
> \text{where f is convex} & \quad f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$


## Lagrangian relaxations
$$X$$가 convex 그리고 integer constraints를 모두 포함할 때, 다음과 같이 문제를 정의 할 수 있다. 

> $$
> \begin{align}
> \min_{x} & \quad f(x) \\
> \text{subject to } & \quad Ax \leq b \\
> & \quad x_{j} \in \mathbb{Z} \quad x \in X 
> \end{align}
> $$

이 때, constraints를 objective에 더하여, 어떤 $$u \geq 0$$에 대한 Lagrangian relaxation을 하면, 다음과 같다.

> $$
> \begin{align}
> L(u) = \min_{x} & \quad f(x) + u^{\top}(Ax-b) \\
> \text{subject to } & \quad x \in X \\
> \end{align}
> $$

Lagrangian form을 통해서 constraint set이 확장되었고, feasible $$x$$에 대해 $$Ax \leq b$$을 만족하므로, 항상 $$f(x) + u^{\top}(Ax - b) \leq f(x), u \geq 0$$이 성립한다. 따라서 $$L(u)$$는 임의의 $$u \geq 0$$에 대해서 lower bound이고, 최선의 lower bound는 dual problem $$\max_{u \geq 0} L(u)$$을 해결함으로써 얻어낼 수 있다. $$L(u)$$는 convex function의 point-wise minimization이기 때문에 concave optimization problem이 된다는 것을 기억하자.

앞서 언급되었던 Facility location problem에 Lagrangian relaxation을 적용해 보면, unconstrained $$v$$에 대하여 다음 식을 푸는 문제로 변형된다.

> $$
> \begin{align}
> L(u) = \min_{x} & \quad \sum_{i = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\
> \text{subject to } & \quad x_{ij} \leq y_{j} \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\
> & \quad x_{ij}, y_{j} \in \lbrace 0, 1 \rbrace \quad  i = 1 \dotsc m, \quad j = 1 \dotsc n \\
> \end{align}
> $$

각각의 $$v$$에 대하여 Lagrange relaxation $$L(v)$$는 쉽게 풀릴 수 있다 :
> $$ x_{ij}(v) =\begin{cases}1 & \text{if} \quad c_{ij} - v_{i} < 0 \quad \text{and}  \quad \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\
> 0 & \text{otherwise.} \end{cases} $$
> $$ y_{j}(v) =\begin{cases}1 & \text{if } \quad \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\
> 0 & \text{otherwise.} \end{cases} $$

이는 lower bound $$L(v)$$ 그리고 heuristic primal solution을 도출 할 수 있도록 한다. 또한 $$-L(v)$$의 부분미분(subdifferential)을 사용한다면 계산도 쉬워진다. subgradient method를 사용하여 $$\max_{v} L(v)$$를 $$\min_{v} -L(v)$$ 로 변환시켜서 문제를 풀어갈 수 있다.