---
layout: post
title: 03-03 The conjugate function
chapter: "03"
order: 7
owner: "Minjoo Lee"
---
Conjugate 함수에 대해 알아보자

Conjugate function은 뒷장에서 다룰 Lagrange Dual에서 최적화 문제를 상응하는 Dual problem으로 변환하는 데 사용된다. Lagrange Dual에서 미분을 할 때, 직접 미분하지 않고 Conjugate function을 이용해 바로 대입할 수 있다. <br>

함수 $$f$$의 conjugate 는 아래와 같다.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Conjugate function [2]</figcaption>
</p>
</figure>

•$$f$$가 convex가 아니어도 $$f^∗$$ 는 convex이다.

#### Example
>• *Negative logarithm* $$f(x)=−\log x$$

> $$f∗(y)=\sup_{x>0} (xy+ \log x)$$ 
> $$=
\begin{cases}
-1-\log(-y), & y < 0 \\ 
\infty, & \text{ otherwise}
\end{cases}
$$

>• *Strictly convex quadratic* $$f(x) = (1/2)x^TQx$$ with $$Q∈S_{++}^n$$

>$$
\begin{align}
f∗(y)=\sup_{x} (y^Tx−(1/2)x^TQx)
& = {1 \over 2}y^TQ^−1y 
\end{align}
$$


이는 13장에서 좀 더 상세히 다루도록 한다.

