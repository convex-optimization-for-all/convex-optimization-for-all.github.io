---
layout: post
title: Convex solution sets
chapter: "04"
order: 2
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Convex solution set의 성질에 대해 알아보자. $X\_{opt}$를 다음과 같이 어떤 convex problem에 대한 solution의 집합이라고 하겠다.

>$$
>\begin{aligned}
>    X\_{opt}=&\text{argmin}_x &f(x) \\\\
>    &\text{subject to } &{g\_{i}(x) \leq 0, i = 1, .., m} \\\\
>    & &{h\_{j}(x) = 0, i = 1, .., r}  \\\\
>\end{aligned}
>$$

## Key property1
>$X\_{opt}$는 convex set이다. 

#### Proof
>$x$, $y$가 solution일때, </br></br>
>1. Domain set $D$는 convex set이므로, $0 \le t \le 1$에 대해 $tx+ (1-t)y \in D$를 만족한다.</br></br>
>2. $g_i, i=1,\dotsc,m$와 $h_j, j=1, \dotsc,r$은 각각 convex, affine function이므로 아래 제약조건을 만족한다.</br>
> $g\_{i}(tx + (1-t)y) \leq tg\_i(x) + (1-t)g\_i(y) \leq 0$,</br>
> $h\_{j}(tx + (1-t)y) = th\_j(x) + (1-t)h\_j(y) = 0$.</br></br>
>3. $f$는 convex function이므로 아래를 만족한다.</br>
>$f(tx+(1-t)y) \leq tf(x) + (1-t)f(y)$ = $tf^{\star} + (1-t) f^{\star} = f^{\star} $.</br>
></br></br>
>즉, $tx + (1-t)y$ 또한 solution이다. </br>
>

#### Geometric interpretation
Convex function에서의 local optimum은 곧 global optimum이기 때문에 복수의 element를 가진 solution set이 있다면 이는 아래와 같은 모양일 수 밖에 없다.</br>
<center>
![](https://wikidocs.net/images/page/18263/multiple-optima.png)</br>
**[Fig1] geometric interpretation of convexity of the solution set**
</center>

## Key property2
>$f$가 strictly convex이라면 solution은 unique하다. 즉, $X_{opt}$는 하나의 element만을 갖는다.

$f$가 strictly convex라는 것은 $f$가 다음과 같은 성질을 항상 만족한다는 것과 같다.</br>
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y) \text{ where } 0 < t < 1, x \neq y, \text{ and } x, y \in \text{dom } f.$$

즉, $f$는 평평한 구간이 없는 아래로 볼록한 형태이며 $f$의 solution은 오직 하나이다.