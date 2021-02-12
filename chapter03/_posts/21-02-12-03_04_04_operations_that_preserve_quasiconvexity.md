---
layout: post
title: 03-04-04 Operations that preserve quasiconvexity
chapter: "03"
order: 9
owner: "Minjoo Lee"
---
이 절에서는 quasiconvexity를 유지하는 연산에 대해 살펴본다.

## Nonnegative weighted maximum

$$f$$가 quasiconvex function일 때, nonnegative weighted maximum $$f$$는 quasiconvex 이다.
>$$f = max$${$$w_1f_1, ... ,w_mf_m$$} with $$w_i \geq 0$$ is quasiconvex


이 개념은 다음과 같이 확장될 수 있다.
>$$f(x) = sup_{y \in C}(w(y)g(x,y))$$ with $$w(y) \geq 0$$, 
>where $$g(x,y)$$ is quasiconvex in $$x$$ for each $$y$$.<br>

<br>

## Composition

만약 $$g : R^n \rightarrow R$$가 quasiconvex이고, $$h : R \rightarrow R$$이 nondecreasing이면, 합성곱 f는 quasiconvex를 만족한다.
> $$f = h \circ g$$ is quasiconvex if h is non-decreasing, g is quasiconvex.
 
Quasiconvex function과 affine 또는 linear-fractional 변환을 합성하면 quasiconvex function이 된다.
만약 $$f$$가 quasiconvex라면, $$g(x) = f(Ax + b)$$ 역시 quasiconvex가 되고, $$\tilde{g}(x) = f((Ax + b)/(c^Tx + d))$$도 set {$$x \mid c^Tx + d > 0, (Ax + b)/(c^Tx + d) \in dom$$ $$f$$}에서 quasiconvex가 된다.

<br>

## Minimization

만약 $$f(x, y)$$가 quasiconvex를 만족하고, $$C$$가 convex set일 때, 다음 조건이 성립한다.
> $$g(x) = inf_{y \in C} f(x,y)$$ is quasiconvex if f is quasiconvex in x, y, and C is convex set.

<br>

## Representation via family of convex functions

Quasiconvex function f의 sublevel set을 convex function의 부등식으로 표현할 수 있다. Convex function의 family는 $$t \in R$$에 대해 $$\phi_t : R^n \rightarrow R$$이고, 다음과 같이 정의된다.
>$$f(x) \leq t \Longleftrightarrow \phi_t(x) \leq 0$$

즉, quasiconvex function $$f(x)$$의 t-sublevel set은 convex function $$\phi_t$$의 0-sublevel set이 된다. 이 때, t는 convex function $$\phi$$ 의 index를 나타낸다. 그리고, 모든 $$x \in R^n$$에 대해 다음을 만족한다.
>$$\phi_t(x) \leq 0 \Longrightarrow \phi_s(x) \leq 0$$, for $$s \geq t$$

