---
layout: post
title: 02 Convex Sets
chapter: "02"
order: "00"
owner: "Wontak Ryu"
---

이 장에서는 convex optimization의 근간을 이루는 개념인 convex set에 대해 살펴볼 것이다.

#### 배경
Convex optimization이란 문제를 convex function으로 정의해서 최대 또는 최소를 구하는 기법을 말한다.
Convex set은 다음 두 가지 측면에서 convex function과 밀접한 관련이 있다.

* Convex function은 convex set으로 정의된다. 즉, 함수의 정의역과 치역이 convex set으로 정의되며 그에 따라 convex function의 주요 성질들이 convex set에 의해 결정된다.
* Optimization 문제를 convex function으로 변환하면 쉽게 풀 수 있다. 하지만, 가끔씩 내가 풀려는 문제가 convex function로 정의된 것인지 판단하기 어려울 때가 있다. 이럴 때는 함수의 epigraph가 convex set인지를 확인해서 convex function임을 판별할 수가 있다.

#### 내용
이 장에서는 convex set의 정의와 예제, 주요 속성, convexity를 유지하는 연산에 대해 살펴볼 것이다.