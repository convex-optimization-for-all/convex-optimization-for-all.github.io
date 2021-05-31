---
layout: post
title: "24-05 Branch and bound algorithm (B&B)"
chapter: "24"
order: "06"
owner: "YoungJae Choung"
---

Branch and bound 알고리즘과 Convex relaxation 을 통해 Integer program을 풀어가는 방법을 알아보자.

## Definition and properties
Branch and bound 알고리즘은 integer program을 푸는 가장 보편적인 방법이다. 주로 divide and conquer 방식으로 원래의 문제를 여러 개의 작은 문제(sub-problems)로 쪼개서 정답에 접근해나가는 방식이다. 

Constraint set $$X = X_{1} \cup X_{1} \cup \dotsc \cup X_{k}$$ 가 각각의 $$X_{i}$$로 이루어진 partition의 합집합일 때,
> $$ \min_{x \in X} f(x) = \min_{i = 1, \dotsc , k} \lbrace \min_{x \in X_{i}} f(x) \rbrace .$$

영역을 분할하여 minimum을 찾아나가면서 최적의 해를 구할 수 있다.

Sub-problem의 임의의 feasible solution을 upper bound $$u(X)$$로 정할 수 있다. lower bound를 얻기 위해서, 각각의 sub-problem에서의 lower bound $$l(X_{i})$$ 를 구한다. 그리고 나서 만약 $$l(X_{i}) \geq u(X)$$ 일 경우에 이 부분에 해당하는 sub-problem $$\min_{x \in X_{i}} f(x)$$ 을 제외한다. 
 
Integer Programming problem (IP) 문제를 다음과 같이 정의한다.

> $$
> \begin{align}
> \min_{x} & \quad f(x) \\
> \text{subject to } & \quad x \in C \\
> & \quad x_j \in \mathbb{Z}, \quad j \in J \\
> \text{where f is convex} & \quad f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

그리고 Convex Relaxation (CR) 문제가 다음과 같을 때,

> $$
> \begin{align}
> \min_{x} & \quad f(x) \\
> \text{subject to } & \quad x \in C \\
> \text{where f is convex} & \quad f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

recursive하게 문제를 풀어간다.

* Constraint set이 trivial 하다면, (CR) 문제를 푼다. 만약 solution이 현재 upper bound 보다 적다면, upper bound를 업데이트 한다. Stop.
    * (CR) 이 infeasible 하다면, (IP) 역시 infeasible 하다. Stop.
    * (CR) 에서의 해 $$x^{\star}$$가 (IP) 에서도 feasible 하다면, $$x^{\star}$$는 해가 된다. Stop.
* 문제에서의 lower bound를 찾는다.
    * (CR) 에서의 해 $$x^{\star}$$가 (IP) 에서는 infeasible 하다면, (IP) 에서의 lower bound 를 갱신한다.
* Lower bound가 현재의 upper bound보다 크다면, Stop.
* Constraint set을 쪼갠다, 그리고 각각의 sub-problem을 recursive하게 푼다.  


## After branching

* Branching 이후에 각각의 subproblem을 푼다.
* 만약에 subproblem의 lower bound가 현재의 upper bound보다 크다면, 그 하부의 subproblem을 고려할 필요가 없다.
* Lower bound를 계산하는 가장 확실한 방법은 convex relaxation을 거쳐서 구하는 것이지만, 다른 방법들 (e.g., Lagrangian relaxation) 또한 사용되기도 한다.