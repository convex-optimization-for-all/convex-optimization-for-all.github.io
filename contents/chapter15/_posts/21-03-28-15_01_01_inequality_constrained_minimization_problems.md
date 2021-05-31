---
layout: post
title: 15-01-01 Inequality constrained minimization problems
chapter: "15"
order: "03"
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
다음과 같은 convex optimization 문제를 고려해보자.
>
$$\begin{align}
\min_{x} & \quad f(x) \\ 
\text{subject to } & \quad Ax = b \\\
                        & \quad h_{i}(x) \leq 0, i = 1, \dotsc, m
\end{align}$$

이와 같이 inquality가 포함된 문제에서는 binding contraints와 non-binding contraints를 파악하기 어려우며, 특히 feasible region의 boundary에서 이러한 어려움이 발생한다. 참고로, Binding constraints란 solution을 찾을 때 영향을 주는 제약조건을 의미한다.

따라서, **interior method**는 feasible region의 boundary가 아닌 interior에서 문제를 풀어보자는 접근 방법이다.

## Background of interior method
General problem에 대한 **interior method**는 1960년대에 Anthony V. Fiacco과 Garth P. McCormick이  제안했다. Interior method는 제안 당시 인기있었던 sequential quadratic programming나 active set method에 밀려서 주목을 받지 못하다가 1980년대에 이르러서야 주목을 받기 시작했다.

Active set method의 경우 최적화 결과에 영향을 주는 constraints가 무엇인지 결정하는 이론이다. Active set method에서는 constraint가 0이면 active로 판단하며 이런 constraints들을 active set이라고 한다. 그런데, active set을 구하려면 feasible region의 boundary를 계산해야 하며 constraint 수가 많이질 수록 계산량이 많아지는 문제가 있다.

이런 방식의 문제점을 파악하고 boudnary가 아닌 interior에서 문제를 풀어보자는 접근한 방식이 바로 Interior point method라고 할 수 있다. 예를 들어 LP에서 constrant수가 $$m$$개라면 boundary를 계산하기 위해 총 $$O(m^2)$$의 계산이 필요한데 interior method의 경우 $$m$$이 아주 커지더라도 newton step 20~30번 내에서 해를 찾는다. 성능에 대한 자세한 사항은 뒷부분에서 다시 다룰 예정이다.

* 참고 : [Interior point method](https://en.wikipedia.org/wiki/Interior-point_method)
* 참고 : [Active set method](https://en.wikipedia.org/wiki/Active_set_method)

## Reducing equality constrained minimization problem
위의 문제는 $$C := \{x : h_i(x) \le 0, i = 1, \cdots , m \}$$라고 하면 다음과 같이 다시 작성해 볼 수 있다. Inequality constraints는 Indicator function 형태로 objective function에 포함시킬 수 있다.

>
\begin{align}
\min_{x} & \quad f(x) + I_C(x) \\\
\end{align}
\begin{align}
\text{subject to } & \quad Ax = b \\\
\end{align}

이와 같이 문제를 equality constrained minimization problem으로 변환할 수 있다. 하지만, Indicator function의 경우 여전히 boundary를 포함하고 있기 때문에 원래 문제의 boundary 계산의 어려움을 여전히 갖고 있으며 differentiable하지 않기 때문에 newton's method를 적용하기는 어렵다.

indicator function $$I_C$$를 **barrier function**으로 근사하면 어떨까? 그럴 경우 boundary는 포함하지 않게 되며 differentiable하기 때문에 newton's method를 적용할 수 있게 된다. 

이와 같이 barrier function으로 재정의한 문제를 푸는 방법을 barrier method라고 하는데 다음 절에서 자세히 소개하고 있다.