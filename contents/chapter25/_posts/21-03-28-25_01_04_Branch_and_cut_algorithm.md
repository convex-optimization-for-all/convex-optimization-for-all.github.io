---
layout: post
title: "25-01-04 Branch and cut algorithm"
chapter: "25"
order: "06"
owner: "YoungJae Choung"
---

1990년 CMU의 Sebastian Ceria는 cutting plane method를 branch and bound 알고리즘을 이용해서 성공적으로 구현을 하였으며 이를 branch and cut이라고 한다. 이때부터 cutting plane은 상용 최적화 solver의 핵심적인 컴포넌트가 되었다.

## Branch and cut algorithm
다음과 같은 integer programing 문제가 있다고 하자. 이때 $$f : \mathbb{R}^{n} \to \mathbb{R}$$이고  $$C \subseteq \mathbb{R}^{n}$$는 convex이며 $$J \subseteq {1, ..., n}$$이다.

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

#### Branch and cut algorithm
알고리즘에서 Convex Problem은 CP로 Integer Program은 IP로 표기한다.

1. 다음 convex relaxation 문제를 푼다.

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

2. (CR) infeasible $$\Rightarrow$$ (IP) infeasible <br>
3. (CR)의 solution $$x^{\star}$$이 (IP) feasible $$\Rightarrow$$ $$x^{\star}$$는 (IP)의 solution <br>
4. (CR)의 solution $$x^{\star}$$이 (IP) infeasible하면 다음 두 가지 중에 선택 <br>
$$\quad$$4.1 cut을 추가하고 step 1로 간다. <br>
$$\quad$$4.2 branch해서 반복적으로 subproblem을 푼다. <br>

Branch and cut algorithm은 branch and bound 와 cutting plane method를 결합한 알고리즘으로서, step 4에서 branch-and-bound를 할지, cut을 할지 선택할 수 있다. 

## Integer programming technology
Gurobi, CPLEX, FICO와 같은 state-of-the-art solver들은 매우 효율적인 simplex, interior-point method 등의 알고리즘 구현을 포함하고 있다. 특히, mixed integer optimization의 경우 대부분의 solver들은 branch and cut algorithm을 사용하고 있으며 이들은 convex relaxation과 warm start의 이점을 많이 활용하고 있다.

약 30년 전에 비하면 Integer programming의 성능 향상은 매우 비약적이다. 따라서, 그동안 풀지 못했던  실생활의 많은 문제들이 최근에 Integer programming을 통해 해결되고 있으며 computing power가 향상됨에 따라 더욱 적극적으로 활용될 전망이다.

* Algorithm에서의 속도 향상 1990-2016 : over $$500,000$$
* Hardware에서의 속도 향상 1990-2016 : over $$500,000$$
* Total speedup over $$250$$ billion = $$2:5 \cdot 10^{11}$$
