---
layout: post
title: 15-07 Feasibility methods
chapter: "15"
order: 13
owner: "Minjoo Lee"
---
지금까지 첫번째 centering step($$t = t^{(0)}$$)에서 $$x^{(0)} = x^*$$를 계산하기 위해 strictly feasible point에서 시작한다고 암묵적으로 가정을 했다. 

이 점은 $$x$$는 다음과 같은 조건을 만족하는 strictly feasible point이다.
>$$ h_i(x) \lt 0, \quad i = 1, \cdots, m, \quad Ax = b$$

## Maximum infeasibility
어떻게 $$x$$를 구할까? 다음 문제를 풀어서 구할 수 있다.

>
$$\begin{align}
&\min_{x, s} \        && s \\
&\text{subject to } \ && h_i(x) \le s,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

목표는 solution $$s$$이 음수가 되게 하는 것이다. 이 문제를 **feasibility method**라고 한다.

Strictly feasible starting point를 구하는 것은 쉽기 때문에 barrier method를 이용해서 풀 수도 있다. 즉, inequality constraint인 $$h_i(x) \le s$$에 slack 변수를 추가해서 equality constraint로 바꾸어 풀면 된다.

이 문제를 풀 때 high accuracy를 만족할 필요는 없으며 feasible $$s < 0$$인 $$(x,s)$$를 찾기만 하면 된다.

## Infeasibility for each inequality constraint 
다음과 같이 문제를 정의해서 풀 수도 있다. 앞에 방법은 모든 inequality의 maximum infeasbility를 찾는 문제였다면 이 문제는 각 inequality 별로  infeasible variable $$s_i, i = 1, \cdots, m$$를 찾는 문제이다.
>
$$\begin{align}
&\min_{x, s} \        && 1^Ts \\
&\text{subject to } \ && h_i(x) \le s_i,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

이 방법의 장점은 solution인 $$s$$를 보면 문제가 infeasible한지 알 수 있다는 것이다. 즉, $$s$$의 요소가 0이상이면 해당 constraint는 만족되지 않는다.