---
layout: post
title: 05-02 Quadratic Programming (QP)
chapter: "05"
order: "03"
owner: "Hooncheol Shin"
---

*Quadratic Program*(QP)는 목적함수(objective function)가 이차식(convex quadratic)이고, 제약함수(constraint functions)가 모두 affine인 convex optimization problem이다. General quadratic program은 다음과 같은 형태로 표현될 수 있다.

### Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{\text{m x n}} \text{, and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$

* 위 목적함수의 $$+ r$$는 최적화의 과정 및 결과에 영향을 주지 않으므로 생략되어도 무방하다.
* $$P \in \mathbb{S}_{+}^n$$를 만족하지 않을 경우 위 문제는 더 이상 convex가 아니게 된다.
* Quadratic program에서 직접 명시되어있지 않더라도 $$P \in \mathbb{S}_{+}^n$$임을 가정한다.
* 위 문제는 기하학적으로 polyhedron 형태의 feasible set에서 convex quadratic function(ellipsoid) $$(1/2)x^T P x + q^T x + r$$를 최소화시키는 $$x^{*}$$를 찾는 것으로 해석된다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_02_geometric_interpretation_of_QP.png" alt="[Fig 1] Geometric interpretation of QP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Geometric interpretation of QP [1]</figcaption>
</p>
</figure>

## QP in Standard form
Quadratic program의 standard form은 다음과 같이 표현된다.

### Standard form QP
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align}
>$$

General form의 quadratic program은 아래의 과정으로 standard form QP로 변형될 수 있다.

### Converting QPs to standard form
**Step1.** Slack variable s를 이용하여 inequality constraint를 equality constraint로 바꿔준다.
> $$
> \begin{align}
>     &\text{minimize}_{x, s} &&{(1/2)x^T P x + q^T x + r} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align}
> $$

**Step2.** x를 두 개의 nonnegative variables로 치환한다.
$$x = x^{+}  - x^{-}$$이고, $$x^{+} \text{, } x^{-} \succeq 0.$$

> $$
> \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{(1/2)(x^{+} - x^{-})^T P (x^{+} - x^{-}) + q^T x^{+} - q^T x^{-} + r}\\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, {x^{-} \succeq 0}.
> \end{align}
> $$

**Step3.** 
$$\tilde{x} $$,
$$\tilde{q} $$, 
$$\tilde{b} $$,
$$\tilde{A} $$, 
$$\tilde{P} $$를 정의.

> $$
> \tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix},
> \tilde{q} =
> \begin{bmatrix}
> q \\\\
> -q \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix},
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I \\\\
> A & -A & O
> \end{bmatrix},
> \tilde{P} =
> \begin{bmatrix}
>  P & -P & O \\\\
> -P &  P & O \\\\
>  O &  O & O \\\\
> \end{bmatrix}
> $$

**Step4.** *Step2*의 문제를
$$\tilde{x}, \tilde{q}, \tilde{b}, \tilde{A}, \tilde{P}$$
로 치환.

>$$
>\begin{align}
>    &\text{minimize}_{\tilde{x}} &&{(1/2)\tilde{x}^T \tilde{P} \tilde{x} + \tilde{q}^T \tilde{x} + r} \\\\
>    &\text{subject to } &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>    & &&{\tilde{x} \succeq 0}.
>\end{align}
>$$

## LP and equivalent QP
Quadratic program의 목적함수에서 이차항을 제거하게 되면 linear program의 형태와 동일해짐을 알 수 있다. 즉, LP는 QP의 한가지 특수한 경우에 해당하며, LP $$ \subseteq $$ QP의 관계가 성립한다.

### Recall: General LP
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&G \in \mathbb{R}^{\text{m x n}} \text{ and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$

### Example 1) Portfolio optimization
Financial portfolio를 만듦에 있어 performance와 risk를 적절히 조율(trade-off)하는 문제다. 

>$$
>\begin{align}
>    &\text{maximize}_{x} &&{\mu^T x - \frac{\gamma}{2}x^T P x} \\\\
>    &\text{subject to } &&{1^Tx = 1} \\\\
>    & &&{x \succeq 0}.
>\end{align}
>$$

* $$\mu$$: expected assets' returns.
* $$P$$: covariance matrix of assets' returns.
* $$gamma$$: risk aversion (hyper-parameter).
* $$x$$: portfolio holdings (percentages).

$$\mu$$와 $$P$$는 과거의 데이터를 통해서 얻을 수 있으며, 각 종목에 $$x$$만큼 투자했을 때 그 평균을 $$\mu^T x$$, 분산을 $$x^T P x$$로 표현할 수 있다.

### Example 2)  Support vector machines
[Support vector machines(이하 SVM)](https://ratsgo.github.io/machine%20learning/2017/05/23/SVM/)은 quadratic program의 한 예에 해당한다. 아래는 SVM의 변형인 [C-SVM](https://ratsgo.github.io/machine%20learning/2017/05/29/SVM2/)이다. SVM에 대한 자세한 설명은 본 장의 주제에서 벗어나므로 여기서는 생략하도록 한다.

>$$
>\begin{align}
>    &\text{minimize}_{\beta, \beta_0, \xi} &&{\frac{1}{2} \| \beta \|_2^2 + C \sum_{i=1}^{n} \xi_i} \\
>    &\text{subject to } &&{\xi_i \geq 0, i = 1, \dotsc, n} \\
>    & &&{y_i (x_i^T \beta + \beta_0) \geq 1 - \xi_i, i = 1, \dotsc, n},\\
>    & \text{given} && \text{y} \in \left\{-1, 1\right\}^n, X \in \mathbb{R}^{\text{n x p}} \text{ having rows } x_1, \dotsc, x_n.
>\end{align}\\
>$$

### Example 3)  Least-squares in regression
다음과 같은 convex quadratic function을 최소화하는 문제는 (unconstrained) QP에 해당한다.
> $$\| Ax - b \|_2^2 = x^T A^TA x - 2b^TAx + b^Tb$$
