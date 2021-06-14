---
layout: post
title: 20-04-02 Converegence Guarantee
chapter: "20"
order: 10
owner: "Hooncheol Shin"
---

$$f$$와 $$g$$에 대한 적당한 조건 아래에서 (A와 B가 full rank일 필요는 없다), ADMM은 모든 $$\rho > 0$$에 대해서 다음을 만족한다. 

* **Residual convergence**: $$k$$가 $$\infty$$로 갈 때, $$r^{(k)} = A x^{(k)} - B z^{(k)} - c \to 0$$, 즉 primal iteration이 feasibility로 접근한다.  
* **Objective convergence**: $$f(x^{(k)} + g(x^{(k)} \to f^{\ast} + g^{\ast}$$, 여기서 $$f^{\ast} + g^{\ast}$$는 최적의 primal objective 값이다. 
* **Dual convergence**: $$u^{(k)} \to u^{\ast}$$, 여기서 $$u^{\ast}$$는 dual solution 이다. 

정확한 수렴속도는 아직 알려지지 않았으며, 현재 많은 연구가 진행중이다. 대략적으로는 first-order method 와 비슷하거나 약간 더 빠르게 동작한다. 
