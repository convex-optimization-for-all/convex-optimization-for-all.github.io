---
layout: post
title: 14-09 Quasi-Newton methods
chapter: "14"
order: "01"5
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

만약 우리가 구해야하는 Hessian의 연산량이 너무 크거나, singular한 경우, quasi-Newton method를 사용하여 Hessian matrix, 즉 $$\nabla^{2}f(x)$$를 $$H>0$$로 근사할 수 있고, 이 $$H$$를 사용하여 update를 수행할 수 있다.

>\begin{align}
>x^{+} = x - tH^{-1}\nabla f(x)
>\end{align}

아래는 Quasi-Newton method의 특징이다. 조금 더 자세한 내용은 [18장]({% post_url contents/chapter18/21-03-23-18_00_Quasi_Newton_methods %})에서 다룬다.

* Hessian을 approximate하는 $$H$$는 매 스텝마다 갱신하여 계산된다. 목표는 $$H^{-1}$$을 비교적 적은 연산으로 구하여 적용하는 것이다.
* 수렴속도가 superlinear로 빠르다. 하지만 Newton과 같은 수렴속도를 갖지는 않는다. 일반적으로 $$n$$ steps의 quasi-Newton은 1 step의 Newton과 동일한 수렴의 크기를 보인다. 
* 많은 quasi-Newton methods는 iteration마다 $$H$$를 업데이트(propagate)해나가는 방식을 사용한다.
