---
layout: post
title: 21-02 Connection to proximal operators
chapter: "21"
order: 3
owner: "Hooncheol Shin"
---

아래와 같이 한 변수에 대하여 두 개의 함수로 분리된 형태의 최적화 문제를 생각해보자.
>$$
>\begin{align}
>\min_{x} f(x)+g(x)
>\end{align}
>$$

이는 제약조건을 추가한 형태로도 표현 가능하다.
>$$
>\begin{align}
>\min_{x, z} f(x)+g(z) \qquad \text{subject to  }x=z
>\end{align}
>$$

여기에서의 ADMM step은 아래와 같다.
>$$
>\begin{align}
>&x^{(k)} = {\operatorname{prox}}_{f,\frac{1}{\rho}}(z^{(k-1)}-w^{(k-1)})\\\\
>&z^{(k)} = {\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{(k)}-w^{(k-1)})\\\\
>&w^{(k)}=w^{(k-1)}+x^{(k)}-z^{(k)}
>\end{align}
>$$

$${\operatorname{prox}}_{f,\frac{1}{\rho}}, {\operatorname{prox}}_{g,\frac{1}{\rho}}$$는 각각 파라미터가 $$\frac{1}{\rho}$$일때 f와 g의 proximal operator이다.

참고로 convex 함수 $$f$$에 대한 [proximal operator의 정의]({% post_url chapter19/21-03-24-19_01_01_Reminder:_proximal_gradient_descent %})는 다음과 같다.
>$$
>\begin{align}
>{\operatorname{prox}}_{f, \lambda}(v) = \underset{x}{\operatorname{argmin}}(f(x)+\frac{1}{2\lambda}||x-v||_{2}^{2}). 
>\end{align}
>$$

Proximal operator로 ADMM의 update가 유도되는 과정은 아래와 같다.

$$x^{+}, z^{+}, w^{+}$$를 각각 $$x, z, w$$에서 한 step update된 값들이라 하자.
>$$
>\begin{align}
>x^{+}& = \underset{x}{\operatorname{argmin}}f(x)+\frac{\rho}{2}||x-z+w||^{2}_{2}\\\\
>& =\underset{x}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(z-w)-x||^{2}_{2}+f(x)\\\\
>& ={\operatorname{prox}}_{f,\frac{1}{\rho}}(z-w)
>\end{align}
>$$
>$$
>\begin{align}
>z^{+}& = \underset{z}{\operatorname{argmin}}g(z)+\frac{\rho}{2}||x^{+}-z+w||^{2}_{2}\\\\
>& =\underset{z}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(x^{+}+w)-z||^{2}_{2}+g(z)\\\\
>& ={\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{+}+w)
>\end{align}
>$$

원래의 ADMM에서의 제약식이 $$Ax+Bz = c$$이고, 여기서의 제약식은 $$x=z$$이다. 즉 x와 z의 선형변환 관계가 identity이면, 원 식의 ADMM update를 prox update로 변형할 수 있다.