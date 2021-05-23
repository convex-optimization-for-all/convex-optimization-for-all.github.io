---
layout: post
title: 07-02 Sub-differentials
chapter: "07"
order: 3
owner: "Kyeongmin Woo"
---

# Sub-differentials

한 볼록함수 $$f$$의 $$x$$에서의 subdifferential $$\partial f(x)$$는 $$x$$에서의 모든 subgradient들의 집합을 의미한다.  

>
\begin{equation}
\partial f(x) = \{g \in \mathbb{R}^n | \text{g is a subgradient of f at x} \}
\end{equation}

Sub-differential은 다음과 같은 특성이 있다.  

- $$\partial f(x)$$ 는 $$f$$가 볼록함수이든지 아니든지 항상 닫혀있는 볼록 집합이 된다.   

- $$\partial f(x)$$ 는 $$f$$가 볼록함수이면 항상 하나이상의 원소를 가지며, 볼록함수가 아닐때는 공집합이 될 수 도 있다. 

- 만약 $$f$$가 $$x$$ 에서 미분가능하고 볼록함수이면, $$\partial f$$는 $$\{\nabla f(x)\}$$ 만을 원소로 갖는다. 

- 만약 $$\partial f(x) = \{g\}$$ 이면, $$f$$는 $$x$$ 에서 미분가능하며, $$\nabla f(x)$$가 $$g$$가 된다.  

