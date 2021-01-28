---
layout: post
title: 01-02 Convex optimization problem
chapter: "01"
order: 2
---

Convex optimization problem은 optimization problem의 한 종류이다.

>![](https://wikidocs.net/images/page/17206/Optimization_problem.png)

**[Fig1] Convex Optimization Problem in standard form [3]**

여기서 objective function $$f$$와 inequality constraint function $$g_i$$가 convex이고, equality constraint function $$h_j$$가 affine이라는 조건이 추가된다. 이때 affine function이란 다음과 같이 linear function에 상수합이 붙은 형태의 함수를 의미한다.
>$$h_j$$, $$j = 1, ..., r$$ are affine: $$h_j(x) = a_{j}^T x + b_{j},$$ $$j=1, ..., r$$

그렇다면 convex function은 어떤 함수를 의미하는 것일까? 이를 이해하기 위해서 convex set을 이해할 필요가 있다.

## Convex sets
두 점 $$x_1$$과 $$x_2$$를 잇는 선분(line segment)은 다음과 같이 정의된다.

>$$x = \theta x_1 + (1 - \theta) x_2$$ with $$0 \le \theta \le 1$$

어떤 집합(set)이 주어져 있다고 하자. 이 집합의 원소인 두 점 $$x_1$$과 $$x_2$$를 잇는 선분이 이 집합에 다시 포함될때 우리는 이 집합을 convex set이라고 부른다. 다시 말하면 집합 C가 convex가 될 조건은 다음과 같다.

>$$x_1, x_2 \in C$$, $$0 \le \theta \le 1$$  $$\Rightarrow$$ $$\theta x_1 + (1-\theta)x_2 \in C$$

예를 들어, 다음 세 가지 그림 중 가장 좌측의 그림만이 convex set에 해당한다.

![](https://wikidocs.net/images/page/17206/Convex_set.png)

**[Fig2] left: a convex set, mid & right: non-convex sets [2]**

## Convex functions
Convex function은 다음과 같이 정의된다.

>$$f: R^n \rightarrow R$$ is convex if dom f is a convex set and
>
>$$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1-\theta)f(y)$$ for all $$x, y \in$$ dom f, $$0 \le \theta \le 1$$

정의에서 부등식으로 표현된 조건은 다음과 같은 기하학적 의미를 가진다. f의 그래프 상의 임의의 두 점 (x, f(x)), (y, f(y))을 생각해보자. 이 두 점을 잇는 선분은 구간 [x, y]에서 그래프보다 크거나 같게 위치한다.

![](https://wikidocs.net/images/page/17206/Convex_function.png)

**[Fig3] convex function [2]**

## Relation between a convex set and a convex function*
convex function과 convex set 사이에는 다음과 같은 밀접한 관계가 있다.
> 함수 f의 epigraph가 convex set일때, 함수 f는 convex function이다.

여기서 epigraph는 무엇을 의미하는 것일까? Epigraph에서 'Epi'는 'above'를 뜻하며, 곧 epigraph는 'above the graph'를 의미한다. 즉, epi f란 f의 그래프의 위쪽 영역에 해당하는 집합이다. 함수 epigraph는 다음과 같이 정의한다.

>epigraph of f: $$R^n \rightarrow R:$$
>
>epi f = {$$(x, t) \in R^{n+1}$$ | $$x \in$$ dom f, f($$x$$) $$\le t$$}

![](https://wikidocs.net/images/page/17206/epigraph.png)

**[Fig4] epigraph [2]**

함수 f가 convex function일때 epi f는 항상 convex set이고 이의 역도 성립한다. 이를 주지하고 위의 convex function과 convex set의 정의를 다시 한번 살펴보도록 하자.

## Nice property of convex optimization problems
Convex 함수의 local minimum은 항상 global minimum이다. convex optimization problem의 경우 non-convex optimization problem에 비해 일반적으로 solution을 더 쉽게 구할 수 있는데, 그 이유는 convex 함수가 다음과 같은 특성을 가지기 때문이다.
>$$f$$가 convex이고 $$x$$가 $$f(x)$$의 locally optimal point일때(즉 $$f(x)$$가 local minimum), 사실 x는 globally optimal point이다.

이를 한번 증명해보자.

>**proof by contradiction:**
>
>Convex function f에 대해 $$x$$가 locally optimal point일때, 어딘가에 $$f(y) < f(x)$$를 만족하는 feasible $$y$$가 있다고 가정하자. (이 가정이 참임이 증명된다면 'locally optimal point = global optimal point'가 성립하지 않을 것이다.)
>
>$$x$$가 locally optimal point라는 것은 다음을 만족하는 양수 $$R$$이 존재한다는 것과 같다: 
>$$z$$ feasible, $$\| z - x \|_2 \le R \Rightarrow f(z) \ge f(x)$$
>
>이때 $$z = \theta y + (1 - \theta) x$$라고 하면 ($$0 < \theta < 1$$),
>
>1.$$\phantom{1} z$$는 두 개의 feasible points $$x, y$$에 대한 convex combination*이므로 또한 feasible하다.
>
>2.$$\phantom{1}$$가정한 것처럼 $$f(y) < f(x)$$가 성립한다면, 이는 곧 $$f(z) \le \theta f(y) + (1 - \theta) f(x) < \theta f(x) + (1 - \theta) f(x) = f(x)$$
>
>2는 x가 locally optimal point이기 위한 전제조건 $$f(z) \ge f(x)$$에 대한 모순이므로 $$f(y)<f(x)$$를 만족하는 feasible y는 존재하지 않는다. 즉, locally optimal point x가 곧 globally optimal point임을 의미한다.


*
**convex combination**
>$$x_1, ..., x_k$$에 대한 convex combination x는 다음과 같이 정의된다.
>
>$$x = \theta_1 x_1 + \theta_2 x_2 + ... + \theta_k x_k$$ with $$\theta_1 + ... + \theta_k = 1, \theta_i \ge 0$$
>
>$$D$$가 convex set일때 $$x_1, x_2, ..., x_k \in D$$이면, $$x \in D$$이다.