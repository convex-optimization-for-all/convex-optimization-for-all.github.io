---
layout: post
title: 21-05 Consensus ADMM
chapter: "21"
order: "06"
owner: "Hooncheol Shin"
---

## Consensus ADMM
아래와 같은 문제를 생각해보자.
>$$
>\begin{align}
>\min_{x}\sum^{B}_{i=1} f_{i}(x)
>\end{align}
>$$

위 문제에 대하여 ADMM으로 해결하기 위해서는, constraint를 도입하여야 했다. 여기서는 update를 병렬적으로 연산하기 용이한 형태로 식을 변형하고자 한다. consensus ADMM이라 불리는 이 접근은 식을 아래와 같이 reparametrize한다.
>$$
>\begin{align}
>&\min_{x_{1},...,x_{B},x} &&\sum^{B}_{i=1} f_{i}(x_{i})\\\\
>&\text{subject to } &&x_{i}=x, i = 1,...B
>\end{align}
>$$

이를 정리하면 deomposable한 ADMM step을 계산할 수 있다.

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2}, i=1,...B\\\\
>x^{(k)} &=\frac{1}{B}\sum_{i=1}^{B}(x_{i}^{(k)}+w_{i}^{(k-1)})\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...,B
>\end{align}
>$$

추가적으로 $$\overline{x}=\frac{1}{B}\sum_{i=1}^{B}x_{i}, \overline{w}=\frac{1}{B}\sum_{i=1}^{B}w_{i}$$로 둘 수 있다. 이렇게 되면, $$k>1$$인 iteration에서 $$\overline{w}^{(k)}=0$$임을 쉽게 확인할 수 있고, ADMM update의 두번째 식은 $$x^{(k)}=\overline{x}^{(k)}$$으로 정리된다. 따라서 ADMM update식을 아래와 같이 정리할 수 있다.

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-\overline{x}^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2},  i=1,...B\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-\overline{x}^{(k)},  i=1,...,B.
>\end{align}
>$$

$$i = 1,...B$$에 대한 $$x_{i}$$ update는 병렬적으로 계산될 수 있다.
정리된 식을 통하여 consensus ADMM에 대한 직관을 얻을 수 있다. 각  $$x_{i}$$ update에서는 $$f_{i}(x_{i})$$를 최소화 하려 하고, 동시에 $$l_{2} regularization$$으로 각 $$x_{i}$$를 평균인 $$\overline{x}$$에 맞추어 간다. 만약 $$x_{i}$$가 평균보다 커지면, $$w_{i}$$는 증가한다. 따라서 다음 step에서의 regularization이 커진 $$x_{i}$$를 낮추게 된다.

## General consensus ADMM
Consensus ADMM은 더 일반화된 형태로 만들어질 수 있다. x에 대하여 affine transformation과 임의의 함수 $$g$$가 적용된 문제의 형태를 살펴보자.

>$$
>\begin{align}
>\min_{x}\sum_{i=1}^{B} f_{i}(a^{T}_{i}x+b_{i})+g(x)
>\end{align}
>$$

이 식에 대해서도, constraint를 추가하기 위하여 reparameterize한다.
>$$
>\begin{align}
>&\min_{x_{1},..x_{B},x} &&\sum^{B}_{i=1}f_{i}(a_{i}^{T}x+b)+g(x)\\\\
>&\text{subject to } &&x_{i} = x, i=1,...B
>\end{align}
>$$ 

이어서 분해가능한 ADMM update를 유도할 수 있다.
>$$
>\begin{align}
>x_{i}^{(k)} &= \underset{x_{i}}{\operatorname{argmin}}f_{i}(a_{i}^{T}x+b_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||^{2}_{2}+g(x)\\\\
>x^{(k)}&=\underset{x}{\operatorname{argmin}} \frac{B\rho}{2}||x-\overline{x}^{(k)}-\overline{w}^{(k-1)}||^{2}_{2}+g(x)\\\\
>w_{i}^{(k)}&=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...B
>\end{align}
>$$ 

Generalized consensus ADMM과 위에서 유도했던 consensus ADMM과의 차이를 정리하면 다음과 같다.

* ADMM step 식이 정리가 되지 않기 때문에, $$\overline{w}^{(k)}=0$$은 더이상 만족하지 않는다.
* $$x_{i}, i=1,...,B$$는 병렬하게 업데이트 가능하다.
*  각각의 $$x_{i}$$ 업데이트는 $$l2$$ 정규화와 함께 해당 부분의 loss를 최소화하는 것으로 생각할 수 있다.
*  $$x$$ 업데이트는 임의의 함수 $$g$$(일반적으로 regularizer)에 대한 proximal operation이다.
*  reparmeterization을 어떻게 하는가에 따라 ADMM 알고리즘이 다르게 도출된다. 

더 자세한 내용은 [참고문헌]({% post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})을 참조한다.
