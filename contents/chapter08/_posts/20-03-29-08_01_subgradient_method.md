---
layout: post
title: 08-01 Subgradient Method
chapter: "08"
order: "02"
owner: "Kyeongmin Woo"
---

# Subgradient Method

함수의 정의역은 $${R}^n$$이며 모든 구간에서 미분 가능하지 않은 컨벡스 함수 $$f$$가 있다고 가정하자.

Subgradient method는 gradient descent에서 gradient를 subgradient로 바꾼 형태로 정의된다. ( $$\nabla f(x^{(k-1)}) → g(x^{(k-1)})$$)

>$$ x^{(k)} = x^{(k-1)} - t_k ⋅ g^{(k-1)}, \quad k = 1, 2, 3, . . . $$

여기서 $$g^{(k-1)} \in \partial f(x^{(k-1)})$$, 즉 $$g^{(k-1)}$$는 $$x^{(k-1)}$$ 지점에서 함수 $$f$$에 대한 임의의 subgradient이다.

## Subgradient method (not subgradient "descent")

Subgradient method는 gradient descent와 다르게 항상 하강(descent)하지 않는다는 특징이 있다 (subgradient "descent"라 명명하지 않는 이유). 그러므로 subgradient method를 사용할 때는 모든 시행(iteration)에 대해 가장 좋은 결과를 파악하고 있어야 한다. 

>$$f(x_{best}^{(k)}) = \min_{i=0,...k} f(x^{(i)})$$ 

$$f(x^{(k)}_{best})$$는 subgradient method를 $$k$$번 시행하였을 때 함수 $$f$$가 반환하는 최솟값을 의미한다. 
