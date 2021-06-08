---
layout: post
title: 02-06-02 Dual generalized inequalities
chapter: "02"
order: 14
owner: "Wontak Ryu"
---

Proper cone으로 generalized inequality를 정의할 수 있다면, dual cone으로도 dual generalized inequality를 정의할 수 있지 않을까? Dual cone이 proper하다면 그럴 수 있다.

이 절에서는 proper dual cone을 이용해서 dual generalized inequality를 정의해보고 minimum과 minimal도 재정의 해보도록 하겠다.

## Dual generalized inequalities

Proper dual cone으로 generalized inequality를 정의해보면 다음과 같다. 어떤 점 $$y$$가 있을 때  $$K$$의 모든 점 $$x$$와 내적을 해서 0보다 크다면, $$y$$는 dual cone $$K^*$$에서 0보다 크다.

이때, $$\succeq_{K^*}$$를  $$\succeq_K$$의 **dual**이라고 한다. 즉, **dual generalized inequality**이다.

>$$y \succeq_{K^*} 0 \iff y^T x \ge 0$$ for all $$x \succeq_K 0$$


#### Generalized inequality와 dual의 주요 속성

* $$x \preceq_K y$$  if and only if $$\lambda^T x \le \lambda^T y$$ for all $$\lambda \succeq_{K^*}  0$$.
* $$x \prec_K y$$  if and only if $$\lambda^T x \lt \lambda^T y$$ for all $$\lambda \succeq_{K^*}  0, \lambda \ne 0$$.

$$K = K^{**}$$이고 $$\preceq_K^* $$와 연관된 
dual generalized inequality는 $$\preceq_K$$이기 때문에, generalized inequality와 dual이 바뀌더라도 이런 속성은 유지된다. 

예를 들어서, $$\lambda \preceq_K^* \mu$$ if and only if $$\lambda^T x \le \mu^T x$$ for all $$x \succeq_K  0$$이다.


## Minimum and minimal elements via dual inequalities

Proper cone $$K$$로 유도된 generalized inequality에 대해, dual generalized inequalities를 이용하여 (possibly nonconvex) 집합 $$S \subseteq R^m$$의 minimum, minimal element에 대한 특성을 표현할 수 있다.

#### Minimum element

모든 $$ \lambda \succ_K^* 0$$와   $$z \in S$$에 대해

$$x$$가 $$\lambda^T z$$의 unique minimizer라면, 
generalized inequality $$ \succ_K^* $$에 대해 $$x$$는 $$S$$의 minimum이다.  (Minimizer란 어떤 함수를 최소로 만드는 종속변수 값을 말한다. 여기서 함수는 $$\lambda^T z$$가 되고 종속 변수는 $$z$$이며 minimizer는 $$x$$가 된다.)

기하학적으로 이 의미는 어떤 $$ \lambda \succ_K^* 0 $$이 있을 때 hyperplane $$\{ z \mid  \lambda^T (z-x) = 0 \}$$은 $$x$$에서 $$S$$의 strict supporting hyperplane이라는 것을 말한다. (Strict supporting hyperplane이란 점 $$x$$에서만 hyperplane이 교차한다는 것을 말한다.) 이때, 집합 $$S$$가 convex일 필요는 없다. 다음 그림에는 minimum $$x$$와 strict supporting hyperplane이 그려져 있다.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_02_Minimum_element.png" alt="[Fig1] Minimum element [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Minimum element [1]</figcaption>
</p>
</figure>

#### Minimal element

Minimal의 경우 필요 조건과 충분 조건 사이에 약간의 차이가 있다. 

$$\lambda \succ_K^* 0$$와 $$z \in S$$에 대해 $$x$$가 $$\lambda^T z$$의 minimizer라면 $$x \in S$$는 $$S$$의 minimal이다. 즉, $$x$$가 minimal의 경우 $$\lambda^T z$$의 unique minimizer가 아니다. 따라서, 동일한  $$\lambda$$에 대해서 여러 minimal이 존재할 수도 있고 여러 $$\lambda$$에서 여러 minimal이 존재할 수도 있다.

다음 그림을 보면 여러 개의 minimal이 존재하는 것을 확인할 수 있다. 왼쪽 아래에 검정색 굵은 선으로 된 부분이 minimal이 존재하는 영역이다. 
여기서 $$\lambda^T_1 z$$의 minimizer는 $$x_1$$이며 $$\lambda_1 \succ_K^* 0$$ 이므로 minimal이다. 또다른 minimizer로 $$x_2$$가 존재한다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_05_Minimal_element.png" alt="[Fig2] Minimal element [1]" width="70%">
  <figcaption style="text-align: center;">[Fig2] Minimal element [1]</figcaption>
</p>
</figure>

하지만 반대는 성립하지 않는다. 점 $$x$$가 집합 $$S$$에 minimal이더라도 어떤 $$\lambda$$와 $$z \in S$$에 대해 $$x$$는 $$\lambda^T z$$의 minimizer는 아니다. 다음 그림을 보면 minimizer가 아닌 minimal을 확인할 수 있다. 또한, 여기서 convexity가 역을 성립시키는데 중요한 조건임을 알 수 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_06_Minimal_element2.png" alt="[Fig3] Minimal이지만 minimizer가 아닌 예 [1]" width="70%">
  <figcaption style="text-align: center;">[Fig3] Minimal이지만 minimizer가 아닌 예 [1]</figcaption>
</p>
</figure>

이 converse theorem은 $$\lambda_1 \succ_K^* 0$$으로 강화되지는 않는다. 아래 왼쪽 그림을 보면 $$x_1 \in S_1$$이 minimal이지만 $$\lambda_1^T x_1$$의 minimizer는 아님을 알 수 있다. 오른쪽 그림은 $$x_2 \in S_2$$이 minimal은 아니지만  $$\lambda_2^T x_2$$의 minimizer라는 것을 알 수 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_07_Minimal_element3.png" alt="[Fig4] $$\lambda_1 \succ_K^* 0$$으로 강화되지 않는 Minimal 예  [1]" width="70%">
  <figcaption style="text-align: center;">$$\text{[Fig4] } \lambda_1 \succ_K^* 0 \text{ 으로 강화되지 않는 Minimal 예  [1]}$$</figcaption>
</p>
</figure>

#### Optimal production frontier
$$n$$가지 자원 (노동, 전기, 천연가스, 물 등)을 이용해서 생산해야 하는 제품이 있다고 해보자. 
이 제품은 여러 방식으로 생산될 수 있다. 각 생산 방법 별로 자원 벡터 $$x \in R$$가 있으며 이때 $$x_i$$는 자원 $$i$$의 소비량을 의미한다. 자원 소비량은 $$x_i \ge 0$$이고 자원은 가치가 높다고 가정한다.

생산 집합 $$P \subseteq R^n$$은 모든 자원 벡터 $$x$$의 집합으로 정의된다. 이때, minimal 자원 벡터를 갖는 생산 방법 $$P$$를 **Pareto optimal** 또는 **efficient**라고 한다. 또한, $$P$$의 minimal 집합을 **efficient production frontier**라고 한다. 

Pareto optimality에 대해서 간단히 살펴보자. 

자원 벡터 $$x$$를 갖는 생산 방법 $$P_x$$와 자원 벡터 $$y$$를 갖는 생산 방법 $$P_y$$가 있다고 하자. 이때, 모든 $$i$$에 대해 $$x_i \le y_i$$이고 일부 $$i$$에 대해서는 $$x_i \lt y_i$$라면 $$P_x$$는  $$P_y$$보다 좋다고 말할 수 있다. 다시 말해서 다른 방법보다 자원을 더 많이 사용하지 않거나 최소한 한 자원을 덜 사용하면 더 좋은 방법이라고 말할 수 있다. 즉, $$x \preceq y$$이고 $$x \ne y$$인 경우에 해당한다. 
생산 방법 $$P_x$$보다 더 좋은 방법이 없다면 $$P_x$$를 Pareto optimal이라고 한다.

아래 식을 최소화하면 Pareto optimal 생산 방법을 찾을 수 있다. 여기서 $$ \lambda_i$$는 자원 $$i$$의 가격이라고 할 수 있다. $$P$$에 대해 $$ \lambda^T x$$를 최소화하면 가장 저렴한 생산 방법을 찾을 수 있다. 가격은 양수이므로 최소화 결과는 항상 Pareto optimal이다.

> $$ \lambda^T x =$$ $$ \lambda^T_1 x_1 + \lambda^T_2 x_2 + ... + \lambda^T_n x_n, \lambda \succ 0 $$

다음 그림은 이런 상황을 잘 보여주고 있다. 그림에서 $$x_1, x_2, x_3$$는  Pareto optimal인데  $$x_4, x_5$$는 아니다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_08_Pareto_optimal.png" alt="[Fig5] Optimal production frontier [1]" width="70%">
  <figcaption style="text-align: center;">[Fig5] Optimal production frontier [1]</figcaption>
</p>
</figure>

