---
layout: post
title: 03-06 Convexity with respect to generalized inequalities
chapter: "03"
order: 11
owner: "Minjoo Lee"
---
$$R$$ 공간 이외의 공간에서는 $$R$$ 공간에서 통상적으로 사용되는 ordering 개념에서 확장된, 일반화된 inequality 표현을 할 때 Cone의 정의를 활용한다. ([02-01-04](https://wikidocs.net/17414) 참고) 이번 절에서는 Cone의 개념을 활용하여, $$R$$공간 이외에서도 확장되는 monotonicity와 convexity의 개념을 살펴본다.

## Monotonicity with respect to a generalized inequality

$$K \subseteq R^n$$이 $$\preceq_K$$로 나타나는 proper cone이라 가정하자. Convex cone $$K \subseteq R^n$$에 대해 다음과 같은 조건을 만족하면 **proper cone**이다.

• $$K$$ is closed. (contains its boudary)</br>
• $$K$$ is solid (has nonempty interior)</br>
• $$K$$ is pointed (contains no line)</br>

 **$$K$$-nondecreasing**를 다음과 같이 정의한다.
> $$f : R \rightarrow R$$ is K-nondecreasing if $$x \preceq_K y \Longrightarrow f(x) \leq f(y)$$


또한, 다음 조건을 만족할 때, **$$K$$-increasing**하다고 이야기 한다.
> $$f : R \rightarrow R$$ is K-increasing if $$x \preceq_K y, x \neq y \Longrightarrow f(x) < f(y)$$


#### Gradient conditions for monotonicity

어떤 미분 가능한 function $$f : R \rightarrow R$$이 convex (즉, interval) domain 상에서 nondecreasing 하다는 것은, 모든 $$x \in dom$$ $$f$$에서 $$f'(x) \geq 0$$이라는 뜻이며, 모든 $$x \in dom$$ $$f$$에서 $$f'(x) > 0$$이면, increasing 하다는 것이다. 이와 유사하게 generalized inequality에서도 확장된 개념으로써, monotonicity를 표현할 수 있다.

도메인이 Convex일 때 미분가능한 function $$f$$가 K-nondecreasing하다는 것은 다음과 식을 만족한다는 의미이다. 잘 살펴보면 단순한 scalar와는 달리 gradient $$\nabla f(x)$$는 dual inequality에서 nonnegative이어야만 한다.
> A differentiable function $$f$$ is K-nondecreasing $$\Longleftrightarrow$$ $$\nabla f(x) \succeq_{K^*} 0$$ for all $$x \in dom$$ $$f$$

다음 조건을 만족하면, $$f$$는 **$$K$$-increasing** 이라고 부른다. Scalar일 때와 같이 역은 성립하지 않는다.
> $$\nabla f(x) \succ_{K^*} 0$$ for all $$x \in dom$$ $$f$$ $$\Longrightarrow$$ $$f$$ is K-incerasing.


#### Convexity with respect to generalized inequality

$$K \subseteq R^m$$를 generalized inequality $$\preceq_K$$와 연관된 proper cone이라고 하자.</br>
이때, $$f : R^n \rightarrow R^m$$을  모든 $$x, y$$, 그리고 $$0 \leq \theta \leq 1$$에서 **$$K$$-convex**라고 하면, 다음과 같은 부등식이 성립한다.
> $$f : R^n \rightarrow R^m$$ is K-convex $$\Longrightarrow$$ $$f(\theta x + (1 - \theta) y) \preceq_K \theta f(x) + (1 - \theta) f(y)$$ with $$0 < \theta < 1$$ for all x, y.
 
또한, **strictly $$K$$-convex**의 조건은 다음과 같다.
> $$f(\theta x + (1 - \theta) y) \prec_K \theta f(x) + (1 - \theta) f(y)$$  for all $$x \neq y$$ and $$0 < \theta < 1$$.
 
m = 1이고 K = $$R_+$$ 일 때가, 앞서 이야기해왔던 일반적인 convexity를 만족하는 부등식이 된다.

#### Dual characterization of $$K$$-convexity

$$f$$가 $$K$$-convex하다는 것은, 모든 $$w \succeq_K * 0$$에 대하여 (real-valued) function $$w^T f$$가 convex라는 것이다. $$f$$가 strictly convex 하다는 것은 모든 $$w \succeq_{K*} 0$$ 에 대하여 (real-valued) function $$w^T f$$가 strictly convex 라는 것이다. 이는 dual inequality의 정의 및 성질을 따른다.

</br>
#### Differentiable K-convex functions

미분가능한 함수 $$f$$가 $$K$$-convex라면 함수 도메인이 convex일 때 다음 식이 성립한다.
> $$f(y) \succeq_K f(x) + Df(x)(y - x)$$ with all $$x, y \in dom$$ $$f$$

여기서 $$Df(x) \in R^{m \times n}$$는 derivative 혹은 점 $$x$$에서 $$f$$의 Jacobian matrix 이다.</br>

$$f$$가 strictly $$K$$-convex 라면 함수 도메인이 convex일 때 다음 식이 성립한다.
> $$f(y) \succ_K f(x) + Df(x)(y - x)$$ with all $$x, y \in dom$$ $$f$$, $$x \neq y$$
 

#### Composition theorem

Composition 의 결과로 나타나는 많은 것들은 $$K$$-convexity 로 일반화 될 수 있다.</br>
예를 들면, 만약 $$g : R^n \rightarrow R^P$$ 가 $$K$$-convex 이고, $$h : R^P \rightarrow R$$ 이 convex, 
그리고 $$h$$의 extended-value extension $$\widetilde{h}$$ 가 $$K$$-nondecreasing이면, $$h \circ g$$는 convex이다. 이는 convex function의 nondecreasing convex function은 convex 임을 일반화한다.</br>
($$\widetilde{h}$$가 $$K$$-nondecreasing이라는 조건이 의미하는 것은 $$dom$$ $$h$$ - $$K$$ = $$dom$$ $$h$$이다.)