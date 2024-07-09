---
layout: post
title: 01-01 Optimization problems?
chapter: "01"
order: 2
owner: "Kyeongmin Woo"
---

최적화 문제(Optimization problems)란 여러개의 선택가능한 후보 중에서 최적의 해(Optimal value) 또는 최적의 해에 근접한 값을 찾는 문제를 일컫는다. 일반적으로 기계학습 분야에서는 비용함수(Cost function)를 최소화 또는 최대화 시키는 모델의 파라미터(parameter)를 구하게 되는데, 이것은 최적화 문제로 정의될 수 있다.

## Mathematical optimization problems
Mathematical optimization problem은 다음과 같은 형태로 표현될 수 있다.

>$$\begin{align*} 
>&\min_{x\in D}\ && f(x) \\
>&\text{subject to} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Mathematical Optimization Problem in standard form [3]**

* $$x \in R^n$$ is the optimization variable
* $$f: R^n \rightarrow R$$ is the objective or cost function
* $$g_i: R^n \rightarrow R, i = 1, ..., m$$ are the inequality constraint functions
* $$h_j: R^n \rightarrow R, j = 1, ..., r$$ are the equality constraint functions

위의 제약조건을 모두 만족하는 정의역(feasible domain)에서 objective function f를 최소로 만드는 벡터 $$x$$를 $$x^*$$로 표시하고 이를 optimal solution이라 부른다. [1]

제약조건의 경우 다음과 같이 두 가지로 구분될 수 있다. [2]

1. Explicit constraints: 말 그대로 optimization problem에 직접적으로 명시된 제약조건을 뜻한다. 위에서 서술한 optimization problem의 standard form에서 함수 $$g_i$$와 $$h_j$$로 표현된 제약조건이 이에 해당한다. 참고로 explicit constraint가 없는 문제를 unconstrained problem이라고 부른다.
2. Implicit constraints: Optimization problem에 직접적으로 명시되지 않는 제약조건을 말한다. 이는 Objective function과 모든 constraint function들의 정의역에 대한 교집합이다.

$$D = dom(f) \cap \bigcap_{i=1}^m {\rm dom}(g_i) \cap \bigcap_{j=1}^r dom(h_j)$$<br/>

**Note:** $$dom(f)$$는 함수 $$f$$의 정의역을 의미한다.

>**Example: implicit constraint ↔ explicit constraint**
>
>최적화 문제가 다음과 같이 주어졌다고 하자.
>
>$$\begin{align*} \text{minimize } & & \log(x) \end{align*}$$
>
>여기서 objective function인 log함수의 정의역이 $$x > 0$$이므로 $$x > 0$$이 이 문제에서의 implicit constraint가 된다. 이 문제를 explicit constraint가 포함된 형태의 최적화문제로 표현하면 다음과 같다.
>
>$$\begin{align*} &\text{minimize } && \log(x) \\ &\text{subject to } &&x > 0 \end{align*}$$

## Applications

최적화 문제는 다양한 영역에 걸쳐 적용될 수 있다. [2]

#### Portfolio optimization
* variables: 각 자산에 대한 투자금
* constraints: 예산, 자산당 최소/최대 투자가능 금액, 최소 수익
* objective: 전반적인 위험도 또는 주가 수익률 분산 (return variance)

#### Device sizing in electronic circuits
* variables: 각 부품의 너비와 길이
* constraints: 제조 공정상 제약사항, 최대 면적
* objective: 전력소비량

#### Data fitting
* variables: 모델 파라미터
* constraints: 사전 정보(e.g. 어떤 파라미터는 non-negative), 파라미터에 대한 제약사항
* objective: 예측값에 대한 에러
