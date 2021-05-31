---
layout: post
title: 14-06 Self concordance
chapter: "14"
order: "10"
owner: "Minjoo Lee"
---
앞서 살펴본 Newton's method의 convergence analysis에서는 크게 두 가지의 단점이 존재한다. [1]

첫 번째로는, 현실상의 문제에서는 찾기 어려운 Lipschitz constant L, strong convexity의 lower bound, upper bound m, M 등이 수식에 포함되기 때문이다. 이 때문에, 수렴성과 수렴속도를 보일 수는 있지만, 구체적으로 해를 찾는 데 있어 얼마만큼의 Newton step이 필요한가 등의 분석은 거의 불가능하다.

두 번째로는, Newton's method 자체는 affine invariant 하지만, Newton's method의 convergence analysis에 있어서는 affine invariant 하지 않다. 이는 일반적인 함수에 대해서는 좌표축의 변화에 따라 Lipschitz constant나 strong convexity의 bound value들이 바뀌기 때문이다.

따라서 이 장에서는 위 두 가지 단점을 보완하는 Self-concordant function에 대해서 알아보고자 한다.

Self-concordant function이 중요하고, 의미 있는 이유는 크게 3가지로 정리할 수 있다.

1. 뒷장에서 다룰 interior-point methods에 있어 중요한 역할을 하는 log barrier function들이 Self-concordant function에 속한다.
2. Self-concordant function들의 Newton's method analysis에서는 상수들에 대한 term이 존재하지 않는다.
3. Self-concordance는 affine-invariant 하다. 즉, Newton's method의 iteration 횟수 등의 추정에 있어, 좌표축의 affine transformation에 대하여 독립적이다.