---
layout: post
title: 17-02 Primal-dual interior-point method
chapter: "17"
order: 3
owner: "Minjoo Lee"
---
Barrier method와 같이 **primal-dual interior-point method**도 central path 위의 점을 (근사적으로) 계산하는 것을 목표로 한다. 그러나 두 가지 방법은 여러 차이점이 있다.

## Primal-dual interior-point method와 barrier method의 차이점
* 일반적으로 iteration 별로 **한 번의 뉴턴 스텝**을 실행한다. (즉, 센터링 스텝을 위한 추가 반복문이 없다.)
* **반드시 feasible일 필요는 없다**.  (Backtracking line search를 통해 feasible한 곳으로 밀어준다.)
* 일반적으로 **더 효과적**이다. 특히 적절한 조건 위에서 linear convergence보다 뛰어난 성능을 보인다.
* Barrier method에 비해 조금은 덜 직관적이다.
