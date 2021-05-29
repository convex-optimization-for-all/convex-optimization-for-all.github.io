---
layout: post
title: 04-02 Convex solution sets
chapter: "04"
order: 3
owner: "YoungJae Choung"
---
Convex solution set의 성질에 대해 알아보자. <br>
$$X_{opt}$$를 다음과 같이 어떤 convex problem에 대한 solution의 집합이라고 하겠다.

>$$
\begin{aligned}
X_{opt} = 
&\text{arg}\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m \\
&&&h_{j}(x) = 0, i = 1, .., r  \\\\
\end{aligned}
$$

## Key property1
>$$X_{opt}$$는 convex set이다. 

#### Proof
>$$x$$, $$y$$가 solution일때,
>1. Domain set $$D$$는 convex set이므로, <br>$$0 \le t \le 1$$에 대해 $$tx+ (1-t)y \in D$$를 만족한다.<br><br>
>2. $$g_i, i=1,\dotsc,m$$와 $$h_j, j=1, \dotsc,r$$은 각각 convex, affine function이므로 아래 제약조건을 만족한다. <br><br>
    $$
    \begin{aligned}
       g_{i}(tx + (1-t)y) \leq tg_i(x) + (1-t)g_i(y) \leq 0, \\
       h_{j}(tx + (1-t)y) = th_j(x) + (1-t)h_j(y) = 0 \\
    \end{aligned}
    $$<br><br>
>3. $$f$$는 convex function이므로 아래를 만족한다. <br><br>
    $$
    \begin{aligned}
      f(tx+(1-t)y) &\leq tf(x) + (1-t)f(y) \\ 
      &= tf^{\star} + (1-t) f^{\star} \\ 
      &= f^{\star}
    \end{aligned}
    $$ <br>
    즉, $$tx + (1-t)y$$ 또한 solution이다.

#### Geometric interpretation
Convex function에서의 local optimum은 곧 global optimum이기 때문에 <br>
복수의 element를 가진 solution set이 있다면 이는 아래와 같은 모양일 수 밖에 없다.<br>

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/18263/multiple-optima.png" alt="[Fig1] geometric interpretation of convexity of the solution set">
  <figcaption style="text-align: center;">[Fig1] geometric interpretation of convexity of the solution set</figcaption>
</p>
</figure>
<br>

## Key property2
>$$f$$가 strictly convex이라면 solution은 unique하다. 즉, $$X_{opt}$$는 하나의 element만을 갖는다.

$$f$$가 strictly convex라는 것은 $$f$$가 다음과 같은 성질을 항상 만족한다는 것과 같다.<br>
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y), $$
>
>$$\text{where } 0 < t < 1, x \neq y, \text{ and } x, y \in \text{dom } f.$$

즉, $$f$$는 평평한 구간이 없는 아래로 볼록한 형태이며 $$f$$의 solution은 오직 하나이다.
