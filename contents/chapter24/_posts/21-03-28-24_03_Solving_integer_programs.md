---
layout: post
title: "24-03 Solving integer programs"
chapter: "24"
order: 4
owner: "YoungJae Choung"
---

Integer program으로 수식을 변형한 뒤, 문제를 해결하려면 relaxation과 같은 기법이 필요하다. integer programs에서 나타나는 제약 사항 및 문제에 대해 어떤 접근을 하는 지 살펴보도록 하자.

## Hardness of integer programs
Integer program 문제를 푸는 것은 convex optimization 문제를 푸는 것보다 훨씬 어렵다. 일반적인 Integer programming은 풀 수 있는 가능성 조차도 모르면서 최소 polynomial time이 걸리는 [NP-hard](https://en.wikipedia.org/wiki/NP-hardness) 이기 때문이다. 이 때, integer constraint에 대한 제약을 없앰으로써 convex relaxation을 하면, optimal value에 다가가는 lower bound를 구할 수 있다.<br><br>
Convex relaxation은 사용하여 문제를 풀면 다음과 같은 한계가 발생할 수 있다.


 * Feasible integer solution을 구하는 것이 어렵게 될 수 있다.
 * Relaxation 조건에서 얻어진 optimal solution이 integer program으로 얻어지는 optimal solution과 거리가 있을 수 있다.
 * 근사(Rounding)를 했을 때의 값이 optimal 값과 다를 수 있다.


## Algorithmic template for solving integer programs
$$X$$가 convex 이고 integrality constraints를 포함할 때, integer program은 다음과 같다.

> $$ z : = \min_{x \in X} f(x) $$

Convex optimization과 다르게 feasible point $$x* \in X$$가 optimal 이라는 것을 입증하는 직접적인 "optimality conditions"는 존재하지 않는다. 대신에, lower bound $$ \underline{z} \leq z$$, 그리고 upper bound $$ \bar{z} \geq z$$ 를 찾아가면서 $$\underline{z} = \bar{z}$$ 에 가까워지도록 optimal의 근사치를 찾는 방법을 사용 할 수 있다.

#### Algorithmic template
Upper bounds의 감소 시퀀스를 관찰하면,
> $$\bar{z_1} \geq \bar{z_2} \geq \dotsc \bar{z_s} \geq z$$

lower bounds의 증가 시퀀스를 관찰하면,
> $$\underline{z_1} \leq \underline{z_2} \leq \dotsc \underline{z_t} \leq z $$

임의의 $$\epsilon > 0$$에 대하여 $$\bar{z_s} - \underline{z_t} \leq \epsilon $$ 이 되는 범위에서 $$z$$의 값이 정해진다.

#### Primal bounds
앞선 $$z$$ 공식에 따라 임의의 feasible $$x \in X$$에서 항상 $$f(x) \geq z$$가 성립하고, 이 때, $$f(x)$$는 upper bound 이다. 하지만 항상 feasible $$x$$를 찾을 수는 없기 때문에, $$x$$값이 해당 셋에 포함 된다면 문제가 쉽게 풀리지만, 그렇지 않을 수도 있다.


#### Dual bounds
보통 lower bounds 로도 불리며, relaxation을 통해서 그 값을 찾게 된다. 다음 장에서 자세한 설명을 덧붙인다.
