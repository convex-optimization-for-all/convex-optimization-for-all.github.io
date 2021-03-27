---
layout: post
title: 14-03 Newton decrement
chapter: "14"
order: 7
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

이 장에서는 Newton decrement를 정의하고, 이 값의 의미를 살펴본다.

최적화 문제를 아래와 같이 정의할때, $$x$$에서의 Newton decrement를 $$\lambda(x)$$로 정의한다.

>\begin{align}
>\min_{x} \quad f(x),\\\\
>\end{align}
>\begin{align}
>\lambda(x) = (\nabla f(x)^{T}(\nabla^{2}f(x))^{-1}\nabla f(x))^{1/2}.
>\end{align}

## Characteristics of Newton decrement
첫번째로, Newton decrement는 함수 $$f(x)$$와 이 함수의 이차 근사(quadratic approximation)의 최소값의 차이와 관계가 있다.
이 차이를 구해보면 다음과 같다.
>\begin{align}
>f(x)-&\min_{y} \big( f(x)+\nabla f(x)^{T}(y-x)+\frac{1}{2}(y-x)^{T}\nabla^{2}f(x)(y-x)\big),\\\\
>f(x)-&\bigg( f(x) + \nabla^{T}f(x)\big( -(\nabla^{2} f(x) )^{-1} \nabla f(x)\big) + \frac{1}{2}\big( -(\nabla^{2}f(x))^{-1} \nabla f(x) \big)^{T} \nabla ^{2}f(x) \big( -(\nabla^{2}f(x))^{-1}\nabla f(x) \big) \bigg) \\\\ 
>&= \frac{1}{2}\nabla f(x)^{T}(\nabla^{2} f(x) )^{-1}\nabla f(x) = \frac{1}{2}\lambda(x)^{2}.
>\end{align}

즉, 우리는 $$\frac{1}{2}\lambda^{2}(x)$$를 suboptimality gap인 $$f(x)-f^{\star}$$의 approximate bound로 생각할 수 있다.

두 번째로는 Newton direction을 Newton method에서 매 iteration의 update 방향 $$v = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$라고 할 때, Newton decrement는 $$f(x)$$의 hessian인 $$\nabla^{2}f(x)$$로 정의된 norm에서의 Newton step의 길이라고 볼 수 있다. 

또는 달리 말해서, 이를 일종의 mahalanobis distance[[Wikipedia](https://en.wikipedia.org/wiki/Mahalanobis_distance)]로 볼 수 있는데, 즉 새롭게 이동할 step $$y$$를 observation이라하고, 현재의 위치 $$x$$를 mean, $$f(x)$$의 hessian을 covariance로 보는 관점이다. 

Mahalanobis distance가 어떤 point와, 분포의 평균과의 거리를 해당 방향의 표준편차의 크기로 나눈 결과라는 정의로 생각하면, 현재의 위치를 mean으로 가지고 hessian을 covariance로 가지는 distribution에 대하여, 새로운 step의 point에 대한 distance를 구한 것이다.

P-quadratic norm([1]의 A1.3)의 형태를 가지는 이 식을 정리하면 다음과 같다.

>\begin{align}
>\lambda(x) = (v^{T}\nabla^{2} f(x)v)^{1/2} = \|\|v\|\|_{\nabla^{2}f(x)}
>\end{align}

세번째로 Newton's method의 step update의 크기 $$\Delta x_{nt}$$로 Newtond decrement를 나타낼 수 있다.
>\begin{align}
>x^{+} &= x-\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\ 
>\end{align}
>\begin{align}
>\Delta x_{nt} &= -\big(\nabla^{2} f(x) \big)^{-1} \nabla f(x) &\\
>\end{align}
>\begin{align}
>\nabla f(x)^{T} \Delta x_{nt} &= -\lambda (x)^{2}
>\end{align}

이 식의 중간과정을 활용하면 Newton decrement를 증분과 Hessian에 관한 식으로도 표현할 수 있다.
>\begin{align}
>\lambda(x) = (\Delta x_{nt}^{T}\nabla^{2} f(x) \Delta x_{nt})^{1/2}.
>\end{align}


마지막으로, Newton decrement 또한, Newton step와 동일하게 affine invariant하다. 다시 말해, 어떤 nonsingular matrix에 대하여 $$g(y) = f(Ay)$$이 함수가 정의되어있다면, $$x = Ay$$에서 $$\lambda_{g(y)} = \lambda_{f(x)}$$이다.