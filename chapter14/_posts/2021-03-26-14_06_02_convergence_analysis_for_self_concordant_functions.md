---
layout: post
title: 14-06-02 Convergence analysis for self-concordant functions
chapter: "14"
order: 12
owner: "Minjoo Lee"
---
Self-concordant function들에 대하여, Convergence analysis의 결과는 다음과 같다.

>Theorem(Nestrov and Nemirovskii) : backtracking line search를 사용하는 Newton's method는 $$f(x^{(k)})-f^{\star}\leq \epsilon$$에 도달함에 있어 아래 만큼의 iteration을 필요로 한다.
>\begin{align}
>C(\alpha, \beta)\big( f(x^{(0)}-f^{\star} \big) + \log\log{(1/\epsilon)},
>\end{align}
여기서 $$C(\alpha, \beta)$$는 $$\alpha, \beta$$에 결정되는 상수이다.

위의 과정에 대한 증명은 원래 Newton's method에 대한 convergence anaylsis 증명과정과 유사하다. 다만 과정 중간에  self-concordant 성질을 이용하여 식들을 추가적으로 정리한다.([1]의 p.503)