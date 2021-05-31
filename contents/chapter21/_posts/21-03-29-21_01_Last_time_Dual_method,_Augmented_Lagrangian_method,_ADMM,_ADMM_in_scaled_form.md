---
layout: post
title: 21-01 Last time - Dual method, Augmented Lagrangian method, ADMM, ADMM in scaled form
chapter: "21"
order: 2
owner: "Hooncheol Shin"
---

이전 20장에서 우리는 Dual methods, ADMM에 대해 살펴보았다. 여기선 ADMM의 응용을 살펴보기에 앞서, Dual methods와 Augmented Lagrangian method, ADMM, ADMM in scalaed form에 대해 정리하고자 한다.

## Dual method
아래의 문제를 살펴보자.

>$$
>\begin{align}
>&\min_{x} f(x) \\\\
>&\text{ subject to } Ax = b
>\end{align}
>$$

여기서 $f$는 strictly convex하고 닫혀있다고 하자. 이 문제의 Lagrangian은 아래와 같다.
>$$
>\begin{align}
>L(x,u) = f(x)+u^{T}(Ax-b)
>\end{align}
>$$

위 문제의 dual 문제는 아래와 같다.
>$$
>\begin{equation}
>\max_u -f^{\ast}(-A^T u) - b^T u
>\end{equation}
>$$

여기에서의 u는 dual variable이다.

이 식에 대한 dual gradient ascent는 아래의 식을 반복적으로 계산한다.($k=1,2,3,...$)
>$$
>\begin{align}
>x^{(k)}=\underset{x}{\operatorname{argmin}} L(x,u^{(k-1)}) \\\\
>u^{(k)}= u^{(k-1)} +t_{k}(Ax^{(k)}-b)
>\end{align}
>$$

$$t_{k}$$는 k번째 iteration의 step size이다.

이 dual method에서는, primal 변수 $$x$$는 첫번째 식처럼 이전 스텝에서 주어진 $$u^{(k-1)}$$에서의 Lagrangian을 최소화하는 $$x$$값으로 업데이트되고, dual 변수 $$u$$는 $$Ax-b$$이 gradient 방향인 gradient ascent의 형태로 업데이트가 된다.

이 방법의 장점은 $$f$$가 B개의 문제로 분할이 가능할 때(decomposable), $$x$$ 또한 B개의 블록으로 분할하고$$( x =(x_{1}, ...,x_{B})\in \mathbb{R}^{n}, \text{ where }x_{i}\in \mathbb{R}^{n_{i}})$$, matrix A 또한 B개의 sub-matrix 블록으로 decompose가 가능해서$$(A = [A_{1}, ..., A_{B}] \text{ where }A_{i} \in \mathbb{R}^{m \times n_{i}})$$, 쉽게 병렬화 또는 확장이 가능하여 계산이 용이하다. 하지만 단점은 수렴성를 보장하기 위하여 까다로운 조건이 필요하다 ; primal의 feasible을 보장하기 위하여, $$f$$가 strongly convex하다는 조건이 필요하다.[[20-01-01]]({% post_url contents/chapter20/21-03-27-20_01_01_Convergence_Analysis %})
## Augmented Lagrangian method
Method of multipliers라고도 불리는 Augmented Lagrangian method는 primal 문제에 추가 항을 더하여 계산한다. 이렇게 하면 iteration을 반복되면서 점차 KKT의 conditions을 만족하게 된다. Dual method와 비교하여 수렴성에 대한 조건(f가 strongly convex)을 완화시킨다. 대신 문제의 분해(decompose)가 불가능해지는 단점이 있다. Primal 문제의 정의는 다음과 같다.

>$$
>\begin{align}
>&\min_{x} & f(x)+\frac{\rho}{2}||Ax-b||_{2}^{2}&\\\\
>&\text{subject to} &Ax=b&
>\end{align}
>$$

여기서 $$\rho>0$$이다. 이 문제의 Lagrangian은 아래와 같다.

>$$
>\begin{align}
>L_{\rho}(x,u)=f(x)+u^{T}(Ax-b)+\frac{\rho}{2}||Ax-b||_{2}^{2}.
>\end{align}
>$$

Dual gradient ascent는 다음을 반복한다. ($$k=1,2,3,...$$)
>$$
>\begin{align}
>x^{(k)}=\underset{x}{\operatorname{argmin}} L_{\rho}(x,u^{(k-1)}) \\\\
>u^{(k)}= u^{(k-1)} +\rho(Ax^{(k)}-b)
>\end{align}
>$$

이 방법의 장점은 위에서 언급하였듯, dual method에 비하여 더 나은 수렴 조건을 가진다. 단점은 제곱 항이 추가되는 탓에 분해가능한 성질(decomposability)을 잃게 된다.

## Alternating direction method of multipliers(ADMM)
ADMM은 dual method와 augmented Lagrangian method의 장점을 섞은 방법이다. 문제가 아래의 형태로 정의 되어있다고 하자.

>$$
>\begin{align}
>\min_{x} f(x)+g(z) \qquad \text{subject to  }Ax+Bz=c
>\end{align}
>$$

이 식에 $$\rho>0$$인 augmented Lagrangian을 정의할 수 있다.
>$$
>\begin{align}
>&L_{\rho} (x,z,u) = f(x)+g(z)+u^{T}(Ax+Bz-c)+\frac{\rho}{2}||Ax+Bz-c||_{2}^{2}\\\\
>\end{align}
>$$

이어서 아래를 반복하여 변수를 업데이트한다.
>$$
>\begin{align}
>&\text{for k = 1,2,3,...}\\\\
>&x^{(k)}=\underset{x}{\operatorname{argmin}} L_{\rho}(x,z^{(k-1)},u^{(k-1)})\\\\
>&z^{(k)}=\underset{z}{\operatorname{argmin}} L_{\rho}(x^{(k)},z,u^{(k-1)})\\\\
>&u^{(k)}=u^{(k-1)}+\rho(Ax^{(k)}+Bz^{(k)}-c)
>\end{align}
>$$

ADMM에서는 primal 변수인 $$x, z$$를 함께 업데이트하지 않고, 순차적으로 각각 업데이트 한다. 그리고 순차적으로 업데이트할 때는 다른 변수는 가장 최근의 값을 이용한다. 즉, k번째 iteration에서 $$z$$를 업데이트 할때에는 이전 iteration의 값 $$x^{(k-1)}$$이 아닌 $$x^{(k)}$$를 이용하고, u를 업데이트 할때 또한 현재 iteration에서 구한 primal 변수 $$x^{(k)}, z^{(k)}$$를 바로 이용한다.

## Alternating direction method of multipliers(ADMM)
ADMM은 제약식 내의 A와 B가 full rank라는 가정 없이, $$f$$와 $$g$$에 대한 큰 제약 없이(under modeset assumption) 모든 $$\rho > 0$$에 대하여 다음을 만족한다. 

* Residual convergence: $$k$$가 $$\infty$$로 갈 때, $$r^{(k)} = A x^{(k)} - B z^{(k)} - c \to 0$$, 즉 primal iteration이 feasibility로 접근한다.  
* Objective convergence: $$f(x^{(k)}) + g(x^{(k)}) \to f^{\star} + g^{\star}$$, 여기서 $$f^{\star} + g^{\star}$$는 최적의 primal objective 값이다. 
* Dual convergence: $$u^{(k)} \to u^{\star}$$, 여기서 $$u^{\star}$$는 dual solution 이다. 

Convergence rate에 대해서는 아직 일반적으로 알려지진 않았고, 연구가 이루어지고있다. Convergence에 대한 참고문헌은 [21장 소개파트]({% post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})에 서술되어있다.

## ADMM in scaled form
ADMM의 dual 변수 $$u$$를 scale된 변수 $$w=u/\rho$$로 바꾸어서 scaled form으로 표현할 수 있다. 이를 정리하면, ADMM step은 다음과 같이 나타낼 수 있다. 
>$$
>\begin{align}
&x^{(k)} = \underset{x}{\operatorname{argmin}} f(x) + \frac{\rho}{2} ||Ax + Bz^{(k-1)} - c + w^{(k-1)} ||_2^2 \\\\
&z^{(k)} = \arg\min_z g(x) + \frac{\rho}{2} || Ax^{(k)} + Bz - c + w^{(k-1)} ||_2^2  \\\\
&w^{(k)} = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
\end{align}
>$$

여기서, $$w^{(k)}$$은 매순간 residual의 $$k$$번째 까지의 합으로 아래처럼도 표현 가능하다. 
>$$
>\begin{align}
w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
\end{align}
>$$
