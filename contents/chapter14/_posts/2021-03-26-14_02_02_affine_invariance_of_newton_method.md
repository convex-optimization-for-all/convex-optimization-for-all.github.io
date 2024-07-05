---
layout: post
title: 14-02-02 Affine invariance of Newton's method
chapter: "14"
order: 6
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Newton's method의 중요한 성질 중 하나는 affine invariance하다는 것이다. 이는 update의 방향이 좌표계의 affine한 변환에 대하여 독립적이라는 의미이다. 예를 들어, gradient descent의 경우 affine 변환에 variant 하기 때문에, 좌표계 공간에 따라 수렴 속도가 다르다.

이 페이지에서는 affine invariance를 유도해본다.

## Affine invariance : proof
$$f:\mathbb{R}^{n}\rightarrow \mathbb{R}$$이 두 번 미분 가능하고, $$A\in \mathbb{R}^{n\times n}$$은 nonsingular하다고 하자. 또한 $$g(y)$$를 $$f(Ay)$$로 정의하자. $$g(y):=f(Ay)$$. 이는 $$y$$를 입력으로 받는 어떤 함수 $$g$$와, $$y$$에 대해서 $$A$$로 affine transformation된 $$Ay$$를 입력으로 받는 함수 $$f$$의 출력값이 같음을 의미한다. Notation과 gradient의 인자에 대한 혼선을 줄이고자, $$x:=Ay$$로 정의한다.

Chain rule을 활용하여 양변을 미분, 두 번 미분한 결과를 정리하면 다음과 같다.

>$$
>\begin{align}
>\nabla g(y) &= A^{T} \nabla f(x)\\\\
>\nabla^{2} g(y) &= A^{T}\nabla^{2}f(x)A,
>\end{align}
>$$

 $$y$$에 대한 $$g$$의 Newton step은 다음과 같다.

>$$
>\begin{align}
>y^{+}  = y-(\nabla^{2}g(y))^{-1}\nabla g(y).
>\end{align}
>$$

여기서 함수 $$g$$ 대신에, $$x$$에 대한 함수 $$f$$로 변환하고 정리하면, $$x$$와 $$f$$에 대한 Newton step을 유도할 수 있다.

>$$
>\begin{align}
>y^{+} &= y-(A^{T}\nabla^{2}f(x)A)^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow y^{+} &= y-A^{-1}(\nabla^{2}f(x))^{-1}(A^{T})^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow Ay^{+} &= Ay-(\nabla^{2}f(x))^{-1}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - \nabla^{2}f(x)^{-1}\nabla f(x).
>\end{align}
>$$

이는 Newton step이 non singular한 matrix로 표현되는 affine transformation에 대하여 좌표변환된 좌표계에서의 update가 서로 같다는 것, 즉 affine invariant함을 의미한다.

동일한 방법으로 gradient descent의 affine invariance를 확인해보고자 step update에 대하여 유도해보면, 다음과 같은 결과를 얻을 수 있다.

>$$
>\begin{align}
>y^{+} &= y-t_{k}\cdot \nabla g(y)\\\\
>\Leftrightarrow y^{+} &= y-t_{k}\cdot \nabla f(x)A^{T}\\\\
>\Leftrightarrow x^{+} &= x - t_{k}\cdot A\nabla f(x)A^{T}. 
>\end{align}
>$$

Gradient descent의 경우 Hessian matrix를 $$\frac{1}{t}I$$로 근사하여 업데이트하기 때문에, affine transformation된 coordinate에 대하여 update의 방향이 달라짐을 알 수 있다.