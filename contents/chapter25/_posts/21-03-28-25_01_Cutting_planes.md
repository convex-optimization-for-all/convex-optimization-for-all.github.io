---
layout: post
title: "25-01 Cutting Planes"
chapter: "25"
order: "02"
owner: "YoungJae Choung"
---

Cutting plane method는 integer linear program을 convex problem으로 변경하여 해를 구한 후, 이 해가  original feasible set에 포함되지 않으면 cut을 이용해서 해가 있는 영역을 잘라내서 새롭게 구한 해가 original feasible set 안에 포함되도록 점진적으로 유도하는 방식이다. 이떄, cut은 feasible set을 자르는 직선(또는 초평면)으로 cutting plane이라고도 한다.

## Concept of cutting plane
개념적으로 아래 그림과 같이 original feasible set과 feasible set 사이에 직선을 그어서 original feasible set이 아닌 영역을 잘라내는 방식이라고 생각하면 된다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://wikidocs.net/images/page/23719/09.01_01_cutting_plane_concept.PNG" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>

* 빨간색 영역 : original integer linear program의 feasible set
* 파란색 영역 : convex relaxation problem의 feasible set
* 녹색 직선 :  cutting plane (cutting plane은 파란색과 빨간색 영역의 사이에 존재한다.)

자세한 알고리즘은 본문에서 다시 소개하도록 하겠다.


## A bit of history on cutting planes
Cutting plane method는 이론으로부터 실용적인 방법으로 발전해 오기까지 매우 오래 시간이 걸렸다. 

1954년에 Dantzig, Fulkerson, Johnson이 TSP(traveling salesman problem)를 풀기 위해 처음으로 Cutting plane method를 제안했으며, 1958년에 수학자인 Gomory가 임의의 integer linear program을 풀 수 있는 범용적인 cutting plane method를 제안했다. 그러나 그 이후 약 30년 동안 Gomory cut은 실제 문제를 풀기에는 실용적이지 않은 상태로 묻혀있었다.

1990년 CMU의 Sebastian Ceria는  cutting plane method를 branch and bound 알고리즘을 이용해서 성공적으로 구현을 하였으며 이를 branch and cut이라고 한다. 이때부터 cutting plane은 상용 최적화 solver의 핵심적인 컴포넌트가 되었다.