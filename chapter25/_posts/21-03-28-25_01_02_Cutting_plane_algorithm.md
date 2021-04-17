---
layout: post
title: "25-01-02 Cutting plane algorithm"
chapter: "25"
order: 4
owner: "YoungJae Choung"
---

이 절에서는 integer linear program을 풀 수 있는 cutting plane 알고리즘에 대해 살펴보도록 하겠다.

## Valid Inequality
Cutting plane을 정의하기 위해 먼저 valid inequality가 무엇인지 살펴보자. 

집합 $$S$$에 대해 부등식 $$\pi^{T}x \le \pi_{0}$$이 다음 조건을 만족한다면 valid하다고 말한다. 즉, 어떤 집합 $$S$$가 부등식 $$\pi^{T}x \le \pi_{0}$$이 정의하는 halfspace에 포함되어 있다면 이 부등식은 $$S$$에 대해 valid하다고 볼 수 있다.

>$$\pi^{T}x \le \pi_{0}$$ for all $$x \in S$$

부등식이 Valid해야 cutting plane이 될 수 있다.
## Cutting plane algorithm
이제 다음과 같은 integer programming이 있을 때 cutting plane algorithm을 살펴보도록 하자.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

$$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$이다.

#### Cutting plane algorithm
다음 알고리즘에서 Convex Problem은 CP로 Integer Program은 IP로 표기한다.

1. $$C_{0} := C$$으로 두고 $$x^{(0)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{0} \right\}$$를 계산
2. for $$k = 0, 1, ...$$ <br>
$$\quad$$if $$x^{k}$$가 (IP) feasible이면 $$x^{k}$$는 optimal solution이므로 Stop함 <br>
$$\quad$$else<br>
$$\quad\quad$$ $$S$$에 대해 valid하면서 $$x^{k}$$를 잘라내는 부등식 ($$\pi$$, $$\pi_{0}$$)을 찾음<br>
$$\quad\quad$$ $$C_{k+1} := C_{k} \cap \{ x : \pi^{T}x \le \pi_{0} \} $$<br>
$$\quad\quad$$ $$x^{(k+1)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{k+1} \right\}$$<br>
$$\quad$$end if<br>
end for<br>

이와 같은 valid inequality를 **cutting plane** 또는 **cut**이라고 한다.

알고리즘의 1단계는 convex relaxation을 하여 CP 문제를 푸는 단계이다. 이떄 feasible set은 $$C$$이다. 

알고리즘 2단계에서는 구한 해가 IP에서 feasible하다면 이를 해로 본다. 만일 feasible하지 않다면 해인 $$x^{k}$$와 집합 $$S$$를 나누는 valid inequality를 찾아서 $$C_{k}$$의 범위를 줄인다. 그리고, $$C_{k+1}$$로 재정의된 CP 문제를 풀고 알고리즘 2단계를 반복하게 된다. 

아래 그림에서 polygon은 집합 $$C$$를 나타내며 CP의 해는 검정색 점으로 표시되어 있다. 이때, valid inequailty는 해를 잘라내서 집합 $$C$$의 범위를 줄이게 된다.

![](https://wikidocs.net/images/page/23740/09.01_02_valid_inequality.PNG) <br>
**[Fig1] Valid Inequality [3]**<br>

이와 같이 집합 $$C$$의 범위를 계속해서 줄여나가면 IP 문제의 convex hull feasible set인 집합 $$S$$와 만나게 되어 IP에 feasible한 해를 구할 수 있게 된다.