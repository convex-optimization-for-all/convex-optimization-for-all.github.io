---
layout: post
title: "22 Conditional Gradient (Frank-Wolfe) Method"
chapter: "22"
order: 1
owner: "YoungJae Choung"
---

본 장에서는 1956 년에 Marguerite Frank와 Philip Wolfe에 의해 제안된 Frank-Wolfe알고리즘을 살펴 볼 것이다.

Frank-Wolfe 알고리즘은 제약조건이 있는 볼록(convex) 최적화를 위한 반복적인 선형(first-order) 최적화 알고리즘으로 조건부 그레디언드 방법, 감소(reduced) 그레디언드 방법 그리고 컨벡스 컴비네이션 알고리즘이라고도 부른다. 

이 방법은 원래 1956 년에 Marguerite Frank와 Philip Wolfe에 의해 제안되었으며, Frank-Wolfe 알고리즘은 각 반복(iteration)에서 목적 함수의 선형 근사를 고려해 이 선형 함수의 mimimizer로 이동한다.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)
