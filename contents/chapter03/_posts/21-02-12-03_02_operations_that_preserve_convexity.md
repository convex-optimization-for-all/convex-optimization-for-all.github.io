---
layout: post
title: 03-02 Operations that preserve convexity
chapter: "03"
order: "06"
owner: "Minjoo Lee"
---
이 절에서는 convex function 의 convexity를 유지하는 연산에 대해 살펴본다. 
Convex fnuction의 Convexity를 유지하는 연산에는 다음과 같은 것들이 있다.

* Nonnegative linear combination
* Composition (Affine/General/Vector) 
* Pointwise maximum and supremum
* Minimization function
* Perspective function


## Nonnegative linear combination
Convex 함수는 상수곱과 덧셈에 대하여 아래와 같은 성질을 가진다.<br>

• Convex 함수 $$f$$가 존재할 때, 여기에 음수가 아닌 임의의 수를 곱하여도 여전히 함수 $$f$$는 Convex 이다.<br>
>$$f$$ is convex $$\Rightarrow \alpha f$$ is convex

• Convex인 두 함수($$f_1, f_2$$)이 존재할 때, 이 두 함수를 합하여도 그 결과는 여전히 convex 이다.<br>
>$$f_1, f_2$$ are convex $$\Rightarrow f_1 + f_2$$ is convex

• Convex $$f_1, ..., f_m$$에 음수가 아닌 $$\alpha $$에 대한 선형 조합 $$\alpha_1f_1 + ... + \alpha_nf_n $$은 convex 이다.<br>
>$$f_1, ..., f_n$$ are convex $$\Rightarrow \alpha_1f_1 + ... + \alpha_nf_n$$ is convex, $$\alpha_1, ..., \alpha_n \ge 0$$


## Composition
### 1. Affine composition<br>
함수 $$f$$가 convex 이면 $$f(Ax + b)$$ 또한 convex 이다.
> $$f$$ is convex $$\Rightarrow f(Ax + b)$$ is convex


### 2. General composition <br>
$$n$$차원에서 1차원으로 매핑하는 함수 $$g$$와 1차원에서 1차원으로 매핑하는 함수 $$h$$가 있다고 가정하자. <br>
이 두 함수의 합성함수 $$f(x)=h(g(x))$$는 다음의 경우 convex이거나 concave 이다.

> composition of $$g:\mathbb{R}^n→\mathbb{R}$$ and $$h:\mathbb{R}→\mathbb{R}$$: <br>
> $$f(x)=h(g(x))$$

• $$g$$가 convex이고 $$h$$가 convex이며 $$h$$가 감소하지 않으면 (nondecreasing) $$f$$는 convex 이다. <br>
• $$g$$가 concave이고 $$h$$가 convex이며 $$h$$가 증가하지 않으면 (nonincreasing) $$f$$는 convex 이다. <br>
• $$g$$가 concave이고 $$h$$가 concave이며 $$h$$가 감소하지 않으면 (nondecreasing) $$f$$는 concave 이다. <br>
• $$g$$가 convex이고 $$h$$가 concave이며 $$h$$가 증가하지 않으면 (nonincreasing) $$f$$는 concave 이다. <br>


#### Proof
• for $$n=1$$ diﬀerentiable $$g,h$$
>$$f''(x)=h''(g(x))g'(x)^2+h'(g(x))g''(x)$$

#### [note]
extended-value extension $${h}$$에 대한 단조성(monotonicity)은 반드시 유지되어야 한다. 

#### Example
• $$g$$가 convex이면, $$\exp g(x)$$는 convex 이다. <br>
• $$g$$가 concave이고 positive 하면, $$1/g(x)$$는 convex 이다.
<br><br> 

### 3. Vector composition <br>
$$n$$차원에서 $$k$$ 차원으로 매핑하는 함수 $$g$$와 다시 $$k$$차원에서 1차원으로 매핑하는 함수 $$h$$가 있다고 가정하자. <br>
그러면 이 두 함수의 합성함수 $$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$는 다음의 경우 convex 이거나 concave 이다.

>composition of $$g:\mathbb{R}^n→\mathbb{R}^k$$ and $$h:\mathbb{R}^k→\mathbb{R}$$: <br>
>$$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$<br>

• $$g$$가 convex이고 $$h$$는 convex 일때, $$h$$가 각 인수에 대해 감소하지 않으면, $$f$$는 convex 이다.<br>
• $$g$$가 convex이고 $$h$$는 concave 일때, $$h$$가 각 인수에 대해 증가하지 않으면, $$f$$는 concave 이다.<br>


#### Proof
• for $$n=1$$ ,diﬀerentiable $$g,h$$<br> 
>$$f''(x)=g'(x)^T∇^2h(g(x))g'(x)+∇h(g(x))^Tg''(x)$$

#### Example
• $$g_i$$가 concave이고 positive 하면, $$\sum_{i=1}^{m} \log g_i(x)$$는 concave 이다.<br>
• $$g_i$$가 convex 이면, $$\log \sum_{i=1}^{m} \exp g_i(x)$$는 convex 이다.


## Pointwise maximum and supremum
함수의 Pointwise maximum은 다음과 같이 정의 되며, 이는 convex이다.
### 1. Pointwise maximum
> $$f_1, f_2$$ are convex functions $$\Rightarrow f(x) = \max \{ f_1(x), f_2(x) \}, dom f = dom f_1 \cap dom $$ $$f_2$$ is convex



### 2. Pointwise supremum<br>
만약 $$f (x, y)$$가 각각의 $$y ∈ A$$ 에 대하여 $$x$$에 볼록하다면, $$g(x) = sup_{y∈A} f(x, y)$$ 는 convex 이다.

>$$f(x, y)$$ is convex in $$x$$ for each $$y ∈ A$$ <br>
>$$\Rightarrow g(x) = \sup_{y∈A} f(x, y)$$ with $$dom$$ $$g = \{x | (x, y) \in dom$$ f for all y $$\in$$ A, sup < &infin; \} is convex in $$x$$

## Minimization
Convex function의 임의의 함수족들의 minimum과 infimum은 convex function 이다.

> $$f$$ is convex in $$(x, y) \Rightarrow g(x)=\inf_{y∈C} f(x,y)$$ with $$dom$$ $$g = \{ x | (x, y) \in dom$$ $$f$$ for some $$y \in C \}$$ is convex in $$x$$<br>
> $$C$$: A convex set

#### Example
>• $$f(x,y)=x^TAx+2x^TBy+y^TCy$$ with<br>

>$$\begin{bmatrix}
>A & B \\\
>B^T & C
>\end{bmatrix} \succeq 0,$$ $$C \succ 0$$

> minimizing over $$y$$ gives $$g(x)=\inf_y f(x,y)=x^T(A−BC^{−1}B^T)x$$
> $$g$$ is convex, hence Schur complement $$A−BC^{−1} B^T \succeq 0$$

>• distance to a set : $$dist(x,S)= \inf_{y ∈ S} \lVert x−y \rVert$$ is convex if $$S$$ is convex

## Perspective
함수 $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ 가 convex $$\Rightarrow$$ the perspective of $$ g: \mathbb{R}^{n+1} → \mathbb{R}$$ 연산은 convexity를 유지 시키는 함수이다.

함수 $$f: \mathbb{R}^n→\mathbb{R}$$의 perspective 함수 $$g: \mathbb{R}^n×\mathbb{R}→\mathbb{R}$$는,
$$g(x,t) = tf({x \over t})$$, $$dom $$ $$g = \{(x,t) | {x \over t} ∈ dom $$ $$f, t>0 \}$$<br>
일때, 함수 $$f$$가 convex 이면 $$g$$또한 convex 이다.

#### Example
•$$t$$가 양수일때, $$g(x,t)=x^Tx/t$$는 convex면, $$f(x)=x^Tx$$는 convex이다.

• Negative logarithm<br>
Relative entropy $$g(x,t) =t\log t − t\log x$$가 $$R_{++}^2$$에서 convex 일때, $$f(x)=−\log x$$는 convex 이다.

• $$f$$가 convex이면, $$g(x)=(cTx+d)f((Ax+b)/(cTx+d))$$는 아래와 같은 조건에서 convex이다. <br>
> $$\{x \vert c^Tx+d>0, (Ax+b)/(c^Tx+d) ∈ dom $$ $$f\}$$