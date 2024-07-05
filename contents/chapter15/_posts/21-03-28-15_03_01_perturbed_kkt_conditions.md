---
layout: post
title: 15-03-01 Perturbed KKT conditions
chapter: "15"
order: 8
owner: "Minjoo Lee"
---
Barrier problem과 원래 식에서 KKT condition을 도출해 보면 다음과 같다.
## KKT conditions for barrier problem
Barrier problem의 KKT condition의 두번째 항은 log barrier function의 gradient를 사용해서 도출되었다.
>
$$\begin{align}
t \nabla f(x^*(t)) - \sum_{i=1}^{m} \frac{1}{h_i(x^*(t))} \nabla h_i(x^*(t)) + A^Tw = 0  \\\ 
 Ax^*(t) = b, \quad h_i(x^*(t)) \lt 0, \quad i = 1, \cdots , m \\\
\end{align}$$

##  KKT conditions for the original problem
원래 문제의 KKT condition을 보면 complementary slackness에 의해서 $$h_i(x^*) \cdot u_i^* = 0$$이 도출되었는데 실제 이 boundary condition을 알기가 매우 어렵다.
>
$$\begin{align}
\nabla f(x^*) + \sum_{i=1}^{m} u_i^* \nabla h_i(x^*) + A^Tv^* = 0 \\\ 
Ax^* = b, \quad h_i(x^*) \le 0, \quad u_i^* \ge 0,   \\\ 
h_i(x^*) \cdot u_i^* = 0,  \quad i = 1, \cdots , m \\\
\end{align}$$


## Redefinition of KKT conditions for barrier problem
그렇다면 두 KKT condition 사이에는 어떤 관계가 있을까? 

먼저 $$u_i(t)$$와 $$v$$를 다음과 같이 두고 
>
$$\begin{align}
u_i(t) = - \frac{1}{t h_i(x^*(t))}, \quad v = \frac{1}{t}w
\end{align}$$

KKT conditions for barrier problem을 재정의해보자.

재정의된 문제를 보면 KKT conditions for the original problem과 거의 유사한 모양임을 알 수 있다. 이 식에서 $$u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}$$이 $$t \to \infty$$일 경우 0이 되는데 원래 식의 $$h_i(x^*) \cdot u_i^* = 0$$과 일치하게 된다.

>
$$\begin{align}
& \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)) + tA^Tv = 0  \\\ 
& Ax^*(t) = b, \quad u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}, \quad h_i(x^*(t)) \lt 0, \quad u_i(t) \gt 0 , \quad i = 1, \cdots , m \\\
\end{align}$$