---
layout: post
title: 10-01 Lower Bounds in Linear Programs
chapter: "10"
order: 2
owner: "Wontak Ryu"
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

## Example 1 : Constraint에 objective function이 포함된 형태

주어진 convex 문제에 대하여 최적값의 lower bound(하한) 값 B를 찾고자 한다고 하자.

>$$
>\begin{align}
>B \leq \min_{x} f(x).
>\end{align}
>$$

특히 linear program의 lower bound를 생각해보자. 간단한 케이스에서부터 일반화된 형태까지 차례로 살펴본다.
첫 번째로, 가장 간단한 형태의 LP 문제를 예시로 들면

>$$
>\begin{align}
>&\min_{x, y}  
>& &{x+y} \\\\
>&\text{subject to} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

위의 문제는 constraint에 이미 objective function의 lower bound를 포함하므로 쉽게 $$B=2$$임을 알 수 있다.

나아가 constraint에 lower bound가 포함되어 있지 않은 경우를 살펴보자.

## Example 2 : Constraint들의 Linear combination으로 objective function이 표현 가능한 형태(1)

>$$
>\begin{align}
>&\min_{x, y}  
>& & {x+3y} \\\\
>&\text{subject to} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

$$x,\, y$$가 feasible하다면, 세 constraint에 scalar 값을 곱해 더하거나 빼더라도 세 constraint를 그대로 만족한다. 따라서, 위와 같은 LP 문제가 있다면, constraint에 scalar 값을 곱해 더하거나 빼는 과정, 즉 constraint들의 선형 결합(linear combination)으로 objective function에 대한 표현이 가능하고, 그 결과로 $B$를 알 수 있다. 

>$$
>\begin{align}
>& &{x + y \geq 2}\\\\
>&{+} &{0x \geq 0}\\\\
>&{+} &{2y \geq 0}\\\\
>&{=} &{x + 3y \geq 2}\\\\
>\\\\
>& &{\text{Lower bound}\\ B = 2.}
>\end{align}
>$$

좀 더 일반화하여 임의의 변수를 적용하여 objectvie function을 나타내면 다음과 같다.

>$$
>\begin{align}
>&\min_{x, y}  
>& &{px+qy} \\\\
>&\text{subject to} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

두 번째 예시와 동일하게, constraint에 대하여 각각 scalar 값 a, b, c를 곱하면, 이 셋의 선형 결합으로 objective function에 대한 표현이 가능하다.

>$$
>\begin{align}
>& &{a(x+y) \geq 2a} \\\\
>&{+} &{bx \geq 0} \\\\
>&{+} &{cy \geq 0} \\\\
>&{=} &{(a+b)x+(a+c)y \geq 2a} \\\\
>\\\\
>& &{\text{Lower bound} \\ B=2a, \\\\
>\text{for any satisfying a,b,c below}}\\\\
>& &{a + b = p}\\\\
>& &{a + c = q}\\\\
>& &{a,b,c \geq 0.}\\\\
>\end{align}
>$$

lower bound가 위에서처럼 2a임을 만족하기 위해서는, scalar 값을 곱하는 과정에서 부등호가 바뀌어선 성립하지 않기 때문에, $$a, b, c$$가 양수라는 조건과 scalar 값의 합이 obejctive function과 동일하다는 조건인 $$a+b = p$$, $$a+c = q$$라는 조건을 만족해야만 한다.

위와 같이 얻은 lower bound 결과를 최대화하는 것으로 새로운 최적화 문제를 정의할 수 있다. 이때 lower bound를 만족하게 하는 조건들이 이 문제에서의 constraint가 된다. 

>$$
>\begin{align}
>&\max_{a, b, c}  
>& &{2a} \\\\
>&\text{subject to} 
>& &{a + b = p}\\\\
>& & &{a + c = q}\\\\
>& & &{a, b, c \geq 0}\\\\
>\end{align}
>$$

위의 원 LP문제를 primal LP라 부르고, primal LP에서의 lower bound를 최대화하는 것으로 최적화 문제를 재정의한 형태를 dual LP라고 부른다. 이 때, dual 문제의 optimization variable의 개수는 primal 문제에서의 constraint의 개수와 같다는 것을 유념하자.

>$$
>\begin{align}
>\text{Primal LP}\qquad
>&\qquad \min_{x, y}  &{px+qy} \\\\
>&\qquad \text{subject to} &{x + y \geq 2}\\\\
>&\qquad &{x, y \geq 0}\\\\
>\\\\
>\\\\
>\text{Dual LP}\qquad
>&\qquad \max_{a, b, c}  &{2a} \\\\
>&\qquad \text{subject to} &{a + b = p}\\\\
>&\qquad &{a + c = q}\\\\
>&\qquad &{a, b, c \geq 0}\\\\
>\end{align}
>$$

## Example 2 : Constraint들의 Linear combination으로 Objective function이 표현 가능한 형태(2)

마지막 예시로  constraint의 부등호가 반대로 되어있고, 등호가 포함 되어있는 형태를 살펴보자.

>$$
>\begin{align}
>&\min_{x, y}  &{px+qy} \\\\
>&\text{subject to} &{x \geq 0}\\\\
>& &{y \leq 1}\\\\
>& &{3x + y = 2}\\\\
>\\\\
>& &{ax \geq 0}\\\\
>&{+} &{-by \geq -b}\\\\
>&{+} &{3cx + cy = 2c}\\\\
>&{=} &{(a+3c)x+(-b+c)y \geq 2c-b}
>\\\\
>\\\\
>& &{\text{Lower bound} \\ B=2c-b, \\\\
>\text{for any satisfying a,b,c below}}\\\\
>& &{a + 3c = p}\\\\
>& &{-b + c = q}\\\\
>& &{a,b \geq 0}\\\\
>\end{align}
>$$

이때, c는 등호의 양변에 곱해진 scalar 값으로 어떤 값을 곱해도 무방하다.

결과적으로, dual LP를 다음과 같이 정의할 수 있다.

>$$
>\begin{align}
>&\qquad \max_{a, b, c}  &{2c-b} \\\\
>&\qquad \text{subject to} &{a + 3c = p}\\\\
>&\qquad &{-b + c = q}\\\\
>&\qquad &{a, b \geq 0}\\\\
>\end{align}
>$$