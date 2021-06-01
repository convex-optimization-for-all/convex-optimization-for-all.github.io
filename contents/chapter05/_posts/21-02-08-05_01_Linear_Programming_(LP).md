---
layout: post
title: 05-01 Linear Programming (LP)
chapter: "05"
order: 2
owner: "Hooncheol Shin"
---

목적함수(objective function)와 제약함수(constraint function)가 모두 affine이면 그 최적화 문제는 *linear program* (LP)이라고 불린다. General linear program은 다음과 같은 형태를 띈다.

### General LP

>$$ \begin{align}
>    &\text{minimize}_{x} &{c^T x + d} \\\\
>    &\text{subject to } &{Gx \preceq h} \\\\
>    & &{Ax = b},\\\\
>\end{align} \\
> \text{where } G \in \mathbb{R}^{\text{m x n}} \text{ and } A \in \mathbb{R}^{\text{p x n}}.
$$

* 위 목적함수의 $$ +d $$는 최적화의 과정 및 결과에 영향을 주지 않으므로 생략되어도 무방하다.
* 만약 동일한 형태의 제약 아래 $$c^T x + d$$를 최대화하는 문제가 주어졌을 경우, 이를 $$ -c^T x - d $$를 최소화하는 문제로 바꾸어 풀 수 있다.
* 위 문제는 기하학적으로 polyhedron 형태의 feasible set에 대해 affine function $$ c^T x + d $$를 최소화시키는 $$ x^{*} $$를 찾는 것으로 해석된다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_01_geometric_interpretation_of_LP.png" alt="[Fig1] Geometric interpretation of LP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Geometric interpretation of LP [1]</figcaption>
</p>
</figure>

## LP in Standard form
General LP가 아닌 standard form LP의 형태로 문제정의에 이용할 수 있다. 

### Standard form LP
>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align} $$

모든 general LP는 아래의 과정에 의해 standard form LP로 변형될 수 있다.

### Converting LPs to standard form

**Step1.** Slack variable s를 이용하여 inequality constraint를 equality constraint로 바꿔준다.
> $$ \begin{align}
>     &\text{minimize}_{x, s} &&{c^T x + d} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align} $$

**Step2.** x를 두 개의 nonnegative variables로 치환한다.
$$ x = x^{+}  - x^{-} $$ 이고, $$ x^{+} \text{, } x^{-} \succeq 0. $$

> $$ \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{c^Tx^{+} - c^Tx^{-} + d} \\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, {x^{-} \succeq 0}.
> \end{align} $$

**Step3.** $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, $$ \tilde{A} $$를 정의.

> $$\tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix}, 
> \tilde{c} =
> \begin{bmatrix}
> c \\\\
> -c \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix}
> $$, 
> $$
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I\\\\
> A & -A & O
> \end{bmatrix}
> $$

**Step4.** *Step2*의 문제를 $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, $$ \tilde{A} $$로 치환.

> $$ \begin{align}
>     &\text{minimize}_{\tilde{x}} &&{\tilde{c}^T \tilde{x} + d} \\\\
>     &\text{subject to} &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>     & &&{\tilde{x} \succeq 0}.
> \end{align} $$

### Example 1) Diet program

영양분에 대한 요구사항을 만족하는 가장 싼 음식의 조합을 찾는 문제다.

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{Dx \succeq d} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

* $$ c_j $$: 음식 j에 대한 단위당 가격
* $$ d_i $$: 영양소 i에 대한 최소 권장 섭취량
* $$ D_{ij} $$: 영양소 i가 음식 j에 들어있는 정도
* $$ x_j $$: 식단에 포함된 음식 j의 양

### Example 2)  Basis pursuit

[Undetermined linear system](https://en.wikipedia.org/wiki/Underdetermined_system)은 변수의 갯수가 등식의 갯수보다 많은 선형시스템이다. $$ X\beta = y $$에 대한 the sparsest solution을 찾는 문제는 아래와 같은 non-convex problem으로 정의된다.

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_0} \\\\
>     &\text{subject to } &&{X\beta = y},\\\\
> \end{align} \\
> \text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n.\\\\
$$

* $$ {\| \beta \|_0} = \sum_{j=1}^p 1, \left\{ \beta_j \neq 0 \right\} $$

위의 문제가 non-convex가 되는 이유는 바로 목적함수로 사용되는 $$ L_0 $$ norm 때문이다. $$ L_1 $$ norm이 [sparsity를 높이는 성질에 착안](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/#four)하여 이를 $$ L_0 $$ norm 대신 목적함수로 사용하면 문제를 convex로 만들어 솔루션을 근사할 수 있다. 우리는 이러한 방식을 *basis pursuit*라고 부른다.

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{X\beta = y},\\\\
> \end{align} \\
> \text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n.
$$

또한 basis pursuit는 다음과 같이 linear program으로 변형된다.

> $$ \begin{align}
>     &\text{minimize}_{\beta, z} &&{1^Tz} \\\\
>     &\text{subject to } &&{z \succeq \beta}\\\\
>     & &&{z \succeq -\beta}\\\\
>     & &&{X\beta = y}
> \end{align} $$

* $$ \beta $$의 각 component의 절댓값보다 $$z$$의 각 component가 크거나 같아야한다.
* 최적화를 통해 $$ z $$의 sparsity를 높여가며, $$ \beta $$의 sparsity 또한 높아지도록 한다.

### Example 3)  Dantzig selector

Basis pursuit에서 다룬 문제와 목적이 동일하지만, y에 noise가 있는 경우를 전제해보자 ( $$ X\beta \approx y $$). 이러한 문제를 [Dantzig selector](https://statweb.stanford.edu/~candes/software/l1magic/downloads/papers/DantzigSelector.pdf)라고 한다.

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{\| X^T (y - X \beta) \|_{\infty} \leq \lambda},\\\\
> \end{align} \\
>\text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n. \ \text{Here } \lambda \geq 0 \text{ is a hyper-parameter. }\\\\
$$

* $$ y - X \beta \in \mathbb{R}^n $$은 residual이다.
* $$ \|y - X \beta\|_{\infty} \leq \lambda $$ 는 왜 inequality constraint로 사용되지 않을까? 
  * Residual을 최소의 값으로 만들어주고 싶다고 하자.
  * 이는 min $$ \| y - X\beta\|_2^2 $$과 같이 표현될 수 있으며, 이 목적함수의 미분값이 0이 되는 지점을 찾는 것과 같다.
  * 즉, $$ \frac{d(\| y - X\beta\|_2^2)}{d\beta} = -\frac{1}{2}X^T(y - X \beta) = 0 $$이다.
  * 문제에 정의된 제약함수 $$ X^T(y - X \beta) $$는 이러한 아이디어에서 도출된다.
  * 다르게 말하면 이는 residual이 variable X와 상관관계(correlation)가 없길 바라는 것과 같다. ($$ X^T(y - X \beta) = 0 $$는 residual vector와 X의 column space가 orthogonal함을 의미한다.)

Dantzig selector는 마찬가지로 다음과 같이 linear program으로 변형된다.

> $$
> \begin{align}
>     &\text{minimize}_{\beta, z} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{x_j^T (y - X \beta) \preceq \lambda}, \text{for all } j = 1 \dotsc p\\\\
>     & &&{-x_j^T (y - X \beta) \preceq \lambda}, \text{for all } j = 1 \dotsc p\\\\
>     & && z \succeq -\beta\\\\
>     & && z \succeq \beta,\\\\
> \end{align}\\
> \text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n. \ \text{Here } x_j \text{ is a jth column of } X.\\\\
> $$
