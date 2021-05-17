---
layout: post
title: "22-02 Conditional gradient method"
chapter: "22"
order: 3
owner: "YoungJae Choung"
---

## Projected Gradient Descent
아래와 같은 제약조건을 가진 문제를 고려해 보자.

> $$\min_{x} f(x) \qquad \text{ subject to } x ∈ C $$

$$f$$가 convex이면서 smooth하고, $$C$$ 또한 convex 이면,  **projected gradient descent** 방법을 이용할 수 있음을 앞에서 살펴보았다.
$$P_{C}$$가 집합 $$C$$에 대한 projection operator 일 때, 선택한 초깃값 $$x^{(0)}$$ 과 $$k = 1, 2, 3, . . .$$에 대해서 다음 식이 성립한다.

> $$ x^{(k)} = P_{C } \bigl( x^{(k−1)} − t_k∇f(x^{(k−1)} \bigr)$$

Projected Gradient Descent는 본질적으로 local quadratic expansion(2nd Taylor Expansion)에서의 $$y$$값이 다음 $$x^{(k)}$$이 된다는 것을 모티브로 하는, proximal gradient descent의 스페셜 케이스로 다음과 같이 나타낼 수도 있다.

> $$x^{(k)} = P_{C} \Bigl( \arg\min_{y} ∇f(x^{(k−1)})^T(y − x^{(k−1)}) + \frac{1}{2t} \| y − x^{(k−1)} \|^2_ 2 \Bigr) $$

Projected Gradient Descent에 대한 좀 더 자세한 내용은 [9-4]({% post_url chapter09/20-01-08-09_04_special_cases %})를  참고 하기 바란다.



## Conditional gradient (Frank-Wolfe) method
여기서 2차 근사를 최소화 하는 대신, 더 간단한 무언가를  시도해 보자.
먼저 집합 $$C$$에서 $$\nabla f(x)$$와 내적했을 때 값이 최소화되는 점을 살펴보도록 하자.

근본적으로, Projection 대신 집합 $$C$$ 안의 점에서 선형함수를 최소화하여 더 간편하고 효과적으로 문제를 해결할 수 있다. 여기서는 현재 포인트에서 최소점 사이에 convex combination을 활용하여 line search 방법을 적용해 나간다.

다음 정형화된 방법을 살펴보자.

초깃값 $$x^{(0)} ∈ C$$를 선택한다. $$k = 1, 2, 3, . . . $$

> $$\begin{array}{rcl}
> s^{(k−1)} & ∈ & \arg\min_{s ∈ C} ∇f(x^{(k−1)})^Ts \\\
> x^{(k)} & = & (1 − γ_k)x^{(k−1)} + γ_ks^{(k−1)}
> \end{array}$$

#### [참고]
> $$f(y) \approx f(x) + \nabla f(x)(y-x)$$
> $$\arg\min_y = f(x) + \nabla f(x)(y-x)$$
> $$\equiv \arg\min_y f(x)y$$

여기서, 이전과 다르게 Projection 과정을 거치지 않고 업데이트를 할 떄, 제약 조건 집합 $$C$$에 있는 점을 사용하여 문제를 풀어나간다.

기본적으로 step size는 $$γ_k =  \frac{2}{(k + 1)}, k = 1, 2, 3, . . ..$$으로 설정된다.

임의의 $$0 ≤ γ_k ≤ 1$$에서 convexity에 의해 $$x^{(k)} ∈ C$$ 임을 보인다.

또한 다음과 같은 식으로 업데이트가 진행되기도 한다.
> $$ x^{(k)} = x^{(k−1)} + γ_k\bigl( s^{(k−1)} − x^{(k−1)} \bigr) $$


즉, 알고리즘 수행됨에 따라 선형 minimizer 방향으로 점차적으로 조금씩 덜 이동하게 된다.
대부분의 경우, co-ordinate descent의 스페셜 케이스인 Ball L1에 대해서 sub gradient 방식을 사용하는 것이 projection 방식을 사용하는 것 보다 문제를 해결하기 더 쉽다.


#### [참고]
흥미로운 사실은, Frank와 Wolfe는 Tucker와 함께 일하던 post-doc 였다고 알려져 있으며. 그들은 먼저 첫번째로 이 알고리즘을 2 차 함수로 제안했다고 한다. 그리고 그 알고리즘은 1956년에 출판되고, 후에 논문으로도 발표되었다. 그리고 이 후로 오랫동안 더 이상 이에 대한 후속 논문은 전혀 나오지 못했다. 그러나 지난 몇년 동안 Jaggi의 통찰력에 힘임어 세상에 소개되면서 다시 주목을 받게 되었다.


<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/22689/frank_wolfe.png" alt="[Fig 1] Conditional Gradient (Frank-Wolfe) method (From Jaggi 2011)[3]">
  <figcaption style="text-align: center;">[Fig 1] Conditional Gradient (Frank-Wolfe) method (From Jaggi 2011)[3]</figcaption>
</p>
</figure>
<br>

## Norm constraints
norm $$\| · \|$$에 대해 $$C = \{x : \| x \| ≤ t \}$$일 때 무슨일이 발생할까? 

다음을 살펴보자

> $$\begin{align}
> s &∈ \arg\min_{\|s\|≤t} ∇f(x^{(k−1)})^Ts \\\
> &= −t ·  \arg\max_{\|s\|≤1}  ∇f(x^{(k−1)})^Ts \\\
> &= −t · ∂ \| ∇f(x^{(k−1)}) \|_{∗}
> \end{align}$$

여기서 $$\| · \|_{∗}$$는 dual norm을 의마한다.

다시 말해, dual norm의 subgradient를 계산하는 방법을 안다면, Frank-Wolfe 단계를 쉽게 수행 할 수 있다는 뜻이다.

Frank-Wolfe의 핵심은 $$C = \{x : \| x \| ≤ t \}$$에 projection 방법을 사용하는 것보다 더 간단하거나 낮은 비용으로 구할 수 있으며, 또한 때로는 $$\| · \|$$의 prox operator보다도 간단하거나 더 낮은 비용을 요한다는 것이다.


## Example: $$l_1$$ regularization
다음은 **$$l_1$$-regularized** 이다.
> $$\min_x f(x) \qquad \text{ subject to } \| x \|_1 ≤ t$$

앞선 공식대로 전개하면, $$s^{(k−1)} ∈ −t∂ \|∇f(x^{(k−1)}) \|_∞$$ 를 얻을 수 있다.
 
Frank-Wolfe 방법은 다음의 과정을 통해 업데이트 된다.
> $$\begin{array}{rcl}
> i_{k−1} & ∈  & \arg\max_{i=1,...p} ∇_i f(x^{(k−1)}) \\\
> x^{(k)}  & = & (1 − γ_k)x^{(k−1)} − γ_kt · sign ∇_{i_{k−1}} f(x^{(k−1)})· e_{i_{k−1}}
> \end{array}$$

이것은 coordinate descent의 일종이다(coordinate descent에 대해서는 나중에 자세히 살펴보자).<br>
Note : 두 가지 모두 $$O(n)$$의 복잡도가 필요하지만 $$l1$$ ball에 projection 하는 것보다 훨씬 간단하다.

## Example: $$l_p$$ regularization
다음은 $$l_p$$-regularized 문제다.

> $$\min_{x}  f(x) \qquad \text{ subject to } \| x \|_{p} ≤ t$$

$$1 ≤ p ≤ ∞$$에서 p가 q의 dual일 때  $$s^{(k−1)} ∈ −t∂ \| ∇f(x^{(k−1)}) \|_{q}$$ 이다. 즉, $$1/p + 1/q = 1$$이다.
   
즉 다음과 같이 선택할 수 있다. 
> $$s_i^{(k−1)} = −α · sign ∇f_i(x^{(k−1)}) · \left| ∇f_i(x^{(k−1)}) \right|^{p/q}, i = 1, . . . n$$

여기서 $$α$$는 $$\| s^{(k-1)} \|_{q} = t$$와 같은 상수이고, Frank-Wolfe 업데이트도 동일하다.

Note: 일반 $$p$$의 경우 **p Ball에 Projection**하는 것보다 훨씬 간단하다.<br>
특별한 경우($$p = 1, 2, ∞$$)를 제외하고 이러한 projection은 직접 계산할 수 없다(최적화로 처리되어야 함).

## Example: trace norm regularization
**trace-regularized** 문제를 살펴보자
> $$\min_{X} f(X) \text{ subject to } \| X \|_{tr} ≤ t$$

$$S^{(k−1)} ∈ −t· ∂\| ∇f(X(k−1)) \|_{op}.$$ 이다.

다음과 같이 $$S_i^{(k−1)}$$를 선택할 수 있다.
> $$S_i^{(k−1)} = −t · uv^T$$

여기서 $$u, v$$는 $$∇f(X^{(k−1)})$$의 왼쪽, 오른쪽 singular 벡터이고, Frank-Wolfe 업데이트는 평소와 같다.

Note: 이 방법은 특이 값 분해(SVD)가 가능하면, **trace norm ball에 projection**하는 것보다 훨씬 간단하고 효율적으로 해를 구할 수 있는 방법이다.


## Constrained and Lagrange forms
제약 조건이 있는 문제의 solution을 다시 한번 상기해보자
> $$\min_x f(x) \qquad \text{ subject to } \| x \| ≤ t$$

다음의 Lagrange 문제는 위 식과 동치이다.
> $$\min_x f(x) + λ \| x \| $$

튜닝 파라미터 $$t$$와 $$λ$$는 [0,∞]구간에서 변한다. 또한 $$\| · \|$$의 Frank-Wolfe 업데이트를 $$\| · \|$$의  proximal 오퍼레이터와 비교해야 한다.

• **$$l_1$$ norm**: Frank-Wolfe 방법은 gradient의 최댓값을 스캔하여 업데이트 한다.
proximal operator soft-threshold를 진행하면서 업데이트 한다. 두 단계 모두 $$O(n)$$ flops을 사용 한다.
 
• **$$l_p$$ norm**: 프랭크-울프(Frank-Wolfe) 업데이트는 gradient의 각 항목마다 제곱하고 모두 합산하여 $$O(n)$$ flop으로 증가시킨다. proximal operator는 일반적으로 직접 계산할 수 없다.

• **Trace norm**: 프랭크-울프(Frank-Wolfe) 업데이트는 gradient의 상단 왼쪽 및 오른쪽 singular vector를 계산한다. proximal operator에서는 soft-thresholds gradient step을 진행하며, 특이값 분해(SVD)를 필요로 한다.

다른 많은 regularizer들이 효율적인 Frank-Wolfe update를 도출하였다.
예를 들면, special polyhedra 혹은 cone constraints, sum-of-norms (group-based) regularization, atomic norms. 같은 것들이다.


Constrained Lasso에 대한 projectied gradient 기법과 conditional gradient 기법을 활용했을 때 성능을 비교하면 다음과 같다. (여기서 $$n=100, p = 500$$)

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/22689/comparing_projected_and_conditional_gradient.png" alt="[Fig 2] Comparing projected and conditional gradient for constrained lasso
problem [3]">
  <figcaption style="text-align: center;">[Fig 2] Comparing projected and conditional gradient for constrained lasso
problem [3]</figcaption>
</p>
</figure>
<br>

<!-- <center>
![](https://wikidocs.net/images/page/22689/comparing_projected_and_conditional_gradient.png)

**[Fig 2] Comparing projected and conditional gradient for constrained lasso
problem [3]**
</center> -->

프랭크-울프(Frank-Wolfe) 방법이 first-order method의 수렴율과 비슷한 양상을 띠고 있는 것을 확인할 수 있을 것이다. 그러나 실제로는 높은 정확도로 수렴하기 위해서는 속도가 더 느려질 수 있다. (참고: 여기서 fixed step size를 사용하지만, line search를 사용하여 수렴 속도를 향상시킬 수도 있다.)


## Duality gap
프랭크-울프(Frank-Wolfe) iteration 과정에서 자연스럽게 duality gap 이 발생되며, 이는 실제로 suboptimality gap을 의미한다.
> $$g(x^{(k-1)}) := \max_{s∈C} ∇f(x^{(k−1)})^T(x^{(k−1)} − s) $$

이것은 $$f(x^{(k−1)}) − f^{\star}$$의 upper bound 이다.

##### [Proof]
convexity의 first-order condition을 이용해 증명할 수 있다.
> $$f(s) ≥ f(x^{(k−1)}) + ∇f(x^{(k−1)})^T(s − x^{(k−1)})$$

모든 $s ∈ C$에 대해 양쪽을 최소화 한다.
>  $$f^{\star} ≥ f(x^{(k−1)}) + min_{s∈C} ∇f(x^{(k−1)})^T(s − x^{(k−1)})$$

최종적으로, 다시 정리하여 다음 식은 duality gap이 upper bound임을 보여 준다.
> $$\max_{s∈C} ∇f(x^{(k−1)})^T(x^{(k−1)} − s) = ∇f(x^{(k−1)})^T(x^{(k−1)} − s^{(k−1)})$$

##### [Note]
따라서 이 quantity는 Frank-Wolfe 업데이트에서 직접 나온 것이다.
왜 우리는 이를 “duality gap”이라 부를까?

original problem을 다시 써보면 아래와 같이 쓸 수있다.
> $$\min_{x} f(x) + I_C(x)$$

여기서 $$I_C$$는 $$C$$의 indicator function을 의미한다. dual 문제는 아래와 같다.
> $$\max_u −f^{*} (u) − I^{*}_C(−u)$$

$$I_C^{*}$$가 $$C$$의 support function을 의미한다. Indicator function의 conjuage는 support function 이 됨을 앞서 살펴보았다.

##### [Recall]
> $$
> I_C (X) =  
> \begin{cases}
> +& \infty &if &x &\notin; C \\\
>  & 0      &if &x &\in; C
> \end{cases}
> $$

> $$
> \begin{align}
> I_C^{*} &= \max_{x} \{ <s, x\> - I_C(x)\} \\
>         &= \max_{x \in C} <s, x> \\
>         &= \text{Support function of } C \text{ at } S
> \end{align}
> $$

$$ x = x ^ {(k-1)}, u = ∇f (x ^ {(k-1)}) $$ 일 때, $$x, u$$에서 발생하는 duality gap은 다음과 같다. (13-04 [Fenchel's inequality]({% post_url chapter13/21-04-05-13_04_Conjugate_function %}) 로부터 유도되기도 한다.)
> $$f(x) + f^{*}(u) + I^{*}_C(−u) ≥ x^Tu + I^{*}_C(−u)$$
