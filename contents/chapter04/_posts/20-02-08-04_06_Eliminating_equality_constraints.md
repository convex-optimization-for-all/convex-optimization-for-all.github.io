---
layout: post
title: 04-06 Eliminating equality constraints
chapter: "04"
order: "07"
owner: "YoungJae Choung"
---
변수를 변경함으로써 convex problem에서 equality constraints를 소거하는 방법에 대해 알아보겠다.

>$$
\begin{aligned}
&\min_{x} &&f(x)\\
&\text{subject to } &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&{Ax = b}.\\
\end{aligned}
$$

임의의 solution $$x_{0}$$에 대해 $$Ax_{0} = b$$이고 $$\text{col}(M) = \text{null}(A)$$이면, equality constraint를 만족하는 임의의 $$x$$를 다음과 같이 표현할 수 있다.
>$$x = My + x_{0}$$

즉, $$Ax = A(My + x_{0}) = AMy + Ax_{0} = 0 + b = b$$이므로, 주어진 문제의 $$x$$를 $$My+x_{0}$$로 치환하면 equality constraint를 소거할 수 있다.

그러므로 다음의 문제는 최초에 주어진 문제와 동치이다.

>$$
\begin{aligned}
&\min_y &&f(My+x_0)\\
&\text{subject to} &&g_{i}(My+x_{0}) \leq 0, i = 1, .., m.\\
\end{aligned}
$$

단, 이와 같은 방법은 다음과 같은 이유들로 사용에 주의해야한다.
1. $$M$$을 계산하는 비용은 대체로 굉장히 크다.
2. $$x$$가 $$y$$보다 더 희소(sparse)하다면 $$y$$를 써서 계산하는 비용이 더 클 수 있다.
