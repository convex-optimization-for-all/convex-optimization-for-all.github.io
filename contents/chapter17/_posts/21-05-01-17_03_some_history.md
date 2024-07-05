---
layout: post
title: 17-03 Some history
chapter: "17"
order: 7
owner: "Minjoo Lee"
---
일반적으로 현대의 state-of-art LP Solver들은  Simplex method와 interior-point method를 모두 사용하고 있다.

* Dantzig(1940년대): Simplex 방법, LP의 general form을 푼 최초의 방식으로 Iteration 없이 exact solution을 구한다. 오늘날까지도 LP를 위한 가장 잘 알려지고 많이 연구되는 알고리즘 중 하나이다.

* Klee 및 Minty(1972) : $$n$$개의 변수와 $$2n$$개의 제약 조건을 갖는 pathological LP. Simplex method로 풀려면 $$2^n$$번 반복이 필요하다.

* Khachiyan (1979) : Nemirovski와 Yudin (1976)의 타원체 방법을 기반으로 한 LP의 polynomial-time 알고리즘으로 이론적으로는 강하나, 실제 문제에서는 그렇지 못하다.

* Karmarkar (1984) : interior-point polynomial-time LP 방법으로 상당히 효과적이며 breakthrough가 된 연구이다. (미국 특허 4,744,026, 2006년 만료).

* Renegar (1988) : LP를위한 Newton 기반 interior-point 알고리즘. Lee-Sidford의 최신 연구가 나올 때까지 이론적으로 가장 좋은 계산 복잡도를 갖고 있었다.