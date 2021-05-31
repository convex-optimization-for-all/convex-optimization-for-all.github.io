---
layout: post
title: 18-03 Davidon-Fletcher-Powell (DFP) Update
chapter: "18"
order: "04"
owner: "Hooncheol Shin"
---

DFP update는 rank-2의 symmetric matrix로 $$H (=B^{-1})$$를 업데이트 하는 방법이다.

>$$H^+ = H + auu^T + bvv^T.$$

DFP update를 통해 계산된 $$H^+$$가 secant equation을 만족한다면, $$s-Hy$$은 $$u$$와 $$v$$의 linear combination으로 표현할 수 있다. (참고: secant equation에 의해, $$B^+ s =y \Leftrightarrow H^+ y = s$$)

>$$H^+y = Hy + auu^Ty + bvv^Ty = Hy + (au^Ty)u + (bv^Ty)v = s$$
>
>$$\Rightarrow s - Hy = (au^Ty)u + (bv^Ty)v$$

$$u=s, v=Hy$$로 두고 a와 b에 대해 풀면 $$H$$에 대한 updating formula가 유도된다.
>$$
> H^+ = H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}
>$$

SR1 update에서와 마찬가지로 [Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula)를 이용하여 $$B$$에 대한 updating formula를 유도할 수 있다.

>$$
>\begin{align}
>B^+ &= B + \frac{(y-Bs)y^T}{y^Ts} + \frac{y(y-Bs)^T}{y^Ts} - \frac{(y-Bs)^Ts}{(y^Ts)^2} yy^T\\\\
> &= \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts} 
>\end{align}
>$$

만약 $$B$$가 positive definite이면 $$\big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big)$$는 positive semidefinite이 된다. 이때 $$\frac{yy^T}{y^Ts}$$가 positive definite이면 $$B^+ = \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts}$$는 positive definite임이 보장된다. 이로써 SR1에서 제기 되었던 positive definiteness의 지속성 문제가 해결된다.

## DFP Update - Alternate Derivation

Recall: curvature condition($$y^Ts > 0, y,s \in \mathbb{R}^n$$)을 만족하면 secant equation을 만족하는 symmetric positive definite matrix가 존재한다.

DFP update는 1. symmetry를 만족하고, 2. secant equation을 만족하는 행렬 $$B^+$$와 $$B$$의 weighted Frobenius norm을 최소화 시키는 문제를 푸는 것으로도 유도된다. (각각의 다른 matrix norm은 각각의 다른 Quasi-Newton method와 연결된다. 그 중에서 이 문제의 solution을 구하기 쉽게 하면서도 scale-invariant optimization method로 작동하게끔 하는 norm이 바로 weighted Frobenius norm이다.)

>Solve
>$$
>\begin{align}
>    \min_{B^+} \: \: &{\|W^{1/2} (B^+ - B) W^{1/2} \|_F} \\\\
>    \text{subject to } &{B^+ = (B^+)^T} \\\\
>    &{B^+s = y}  \\\\
>\end{align}\\\\
>\text{where } W \in \mathbb{R}^{n \; \times \;n} \text{ is nonsingular and such that } Wy_k = s_k.
>$$

***참고**:

* Frobenius norm: 행렬 $$A$$에 대한 Frobenius norm은 다음과 같이 정의된다.
$$
\| A \|_{F}  \doteq ( \sum_{i,j} A_{i,j}^2 )^{1/2}
$$

* Weighted Frobenius norm: 가중치 행렬 $$W(W \succ 0)$$에 대한 행렬 $$A$$의 weighted Frobenius norm은 다음과 같이 정의된다. 
$$
\|A\|_W \doteq \| W^{1/2} A W^{1/2} \|_F
$$