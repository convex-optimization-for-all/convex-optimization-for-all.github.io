---
layout: post
title: 15-05 Convergence analysis
chapter: "15"
order: "11"
owner: "Minjoo Lee"
---
Barrier method는 centering step을 정확히 푼다고 가정하면 다음의 수렴 결과를 얻을 수 있다.

## Convergence Theorem
**Barrier method**는 $$k$$ centering step후 다음 식을 만족한다. (단, $$k$$는 outer iteration 수이다.)
>$$\begin{align}
f(x^{(k)}) - f^{*} \le  \frac{m}{\mu^k t^{(0)}}
\end{align}$$

즉, barrier method로 원하는 accuracy level $$\epsilon$$에 도달하려면 다음 centering step 수에 첫번째 centering step인 1을 더한 횟수의 step이 필요하다.

>$$\begin{align}
\frac{log(m/(t^{(0)}\epsilon))}{\log \mu} + 1
\end{align}$$

따라서, $$O(\log 1/\epsilon )$$으로 linear convergence임을 알 수 있다. 

Newton's method는 $$O(\log \log 1/\epsilon ) $$로 quadratic convergence이지만 이 경우 문제가 매우 어렵기 때문에 linear convergence가 그렇게 나쁜 결과는 아니다.

Linear convergence와 quadratic convergence의 정의는 Wiki를 참고하라.<br>
* 참고 : [Rate of convergnece](https://en.wikipedia.org/wiki/Rate_of_convergence)