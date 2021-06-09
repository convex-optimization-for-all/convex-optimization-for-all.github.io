---
layout: post
title: 06 Gradient Descent
chapter: "06"
order: 1
owner: "Kyeongmin Woo"
---

이 장에서는 최적화 기법 중에 가장 기본적이고 중요한 기법인 **Gradient Descent**에 대해 살펴본다. 

최적화 기법에서 알고리즘의 수렴 여부와 수렴속도를 결정짓는 매우 중요한 요소가 search direction과 step size이다. Gradient descent 방식은 gradient의 음수 방향으로 직선 탐색을 하는 방식이다. 이때, step size는 고정 크기 방식과 곡면에 따라 적응적으로 선택하는 방식이 있는데 이 장에서는 두 방식에 대해 모두 살펴볼 것이다.

Gradinet descent가 수렴하려면 몇 가지 전제 조건이 필요하다. 이런 전제 조건이 만족된다면 gradient descent가 얼마나 빠르게 수렴할 수 있는지 계산해 볼 수 있다. 또한, Strong Convexity를 만족하게 되면 수렴은 기하급수적으로 빨라지게 된다. 이 경우에 수렴 속도도 살펴볼 것이다.

Gradient descent를 응용한 방법으로 gradient boosting과 stochastic gradient decent에 대해서도 살펴보도록 하겠다.