---
layout: post
title: 12 KKT Conditions
chapter: "12"
order: "01"
owner: "Wontak Ryu"
---

Primal problem이 convex일 때, Karush–Kuhn–Tucker (KKT) conditions는 zero duality gap인 primal & dual optimal points에 대한 충분조건이 된다. 또한 primal problem의 목적함수 및 제약함수들이 미분 가능하며 strong duality를 만족할때는 primal & dual optimal points에서 항상 KKT conditions를 만족하게 된다. KKT conditions는 최적화에서 상당히 중요한 위치를 차지하고 있다. 이 조건은 몇몇 특수한 문제들을 해석적으로(analytically) 풀 수 있게끔 해주기도 하며, 또한 컨벡스 최적화의 많은 알고리즘들이 KKT conditions를 풀기 위한 방법으로 해석되기도 한다 [1]. 이번 장에서는 KKT conditions의 정의와 성질을 알아보고 이에 기반한 몇 가지 예시를 살펴보도록 한다.

*여담으로* KKT conditions는 본래 Harold W. Kuhn과 Albert W. Tucker에 의해 1951년에 세상에 알려졌고, 당시에는 KT (Kuhn-Tucker) conditions로 불렸다. 그리고 이후 학자들에 의해 이 문제의 necessary conditions가 1939년 William Karush의 석사 논문에 의해 다루어졌음이 발견되었는데, 그 때부터 Karush의 이름이 포함되어 KKT (Karush–Kuhn–Tucker) conditions로 불리게 된다 [3].