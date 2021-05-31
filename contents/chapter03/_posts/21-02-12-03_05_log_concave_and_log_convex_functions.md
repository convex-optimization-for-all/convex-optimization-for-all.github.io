---
layout: post
title: 03-05 Log-concave and log-convex functions
chapter: "03"
order: "01"3
owner: "Minjoo Lee"
---
Log-concave & log-convex function에 대해 알아보자.

## Definition

Log-concave와 log-convex의 정의는 다음과 같다.

#### $$f : R^n \rightarrow R$$ is Logarithmically concave or log-concave
만약 모든 $$x \in dom$$ $$f$$에 대해서 $$f(x) > 0$$이고, $$log f$$가 concave라면, $$f : R^n \rightarrow R$$는 logarithmically concave 혹은 log-concave라고 부른다.
> $$f$$ is log-concave for $$f(x) > 0$$ for all x $$\in dom$$ $$f$$ : <br>
>$$f(\theta x + (1 - \theta) y) \geq f(x)^\theta f(y)^{1-\theta}$$ for $$0 \leq \theta \leq 1$$.

#### $$f : R^n \rightarrow R$$ is Logarithmically convex or log-convex
만약 모든 $$x \in dom$$ $$f$$에 대해서 $$f(x) > 0$$이고, $$log f$$가 convex라면, $$f : R^n \rightarrow R$$는 logarithmically convex 혹은 log-convex라고 부른다. 따라서 $$f$$가 log-convex라면, $$1/f$$는 log-concave가 된다.
> $$f$$ is log-convex for $$f(x) > 0$$ for all x $$\in dom$$ $$f$$ $$\Longleftrightarrow \frac{1}{f}$$ is log-concave.

$$f$$값이 0이 되도록 허용하는 것이 편리할 때가 있는데, 이 경우 $$log f(x) = -\infty$$가 된다. 이런 경우, extended-value function $$log f$$가 concave라면, $$f$$는 log-concave라고 부를 수 있다.

**Log-convex function과 log-concave function은 각각 quasiconvex, quasiconcave가 된다. logarithm은 단조 증가하기 때문이다.**

## Examples
#### Affine function
$$f$$가 다음과 같이 정의되면, log-concave이다.
>$$f(x) = a^Tx + b$$ on {$$x \mid a^Tx + b > 0$$}

#### Powers
$$f(x) = x^a$$는 $$R_{++}$$에서 $$a \leq 0$$일 때 log-convex이고, $$a \geq 0$$일 때 log-concave이다.

#### Exponentials
$$f(x) = e^{ax}$$는 log-convex이자 log-concave이다.

#### The cumulative distribution function of a Gaussian density
$$\Phi(x) = \frac{1}{ \sqrt{2 \pi } }  \int_ {-\infty} ^x e^{-u^2/2} du $$ 는 log-concave이다.

#### Gamma function
$$\Gamma (x) = \int_0^\infty u^{x-1}e^{-u} du $$
는 $$x \geq 1$$에서 log-convex이다.

#### Determinant
$$det X$$는 $$S^n_{++}$$에서 log concave이다.

#### Determinant over trace
$$det X$$ / $$tr X$$는 $$S^n_{++}$$에서 log concave이다.

<br>
## Properties

#### Twice differentiable log-convex / concave functions
$$f$$가 두번 미분 가능하고, $$dom$$ $$f$$가 convex하다면, 다음 식이 성립한다.<br>
>$$\nabla ^2logf(x) = \frac{1}{f(x)} \nabla ^2f(x) - \frac{1}{f(x)^2}\nabla f(x) \nabla f(x)^T$$

$$f$$가 log-convex $$\Longleftrightarrow$$ 모든 $$x \in dom$$ $$f$$에 대해 $$f(x) \nabla ^2 f(x) \succeq \nabla f(x)\nabla f(x)^T$$ 이고, <br>
$$f$$가 log-concave $$\Longleftrightarrow$$ 모든 $$x \in dom$$ $$f$$에 대해 $$f(x) \nabla ^2 f(x) \preceq \nabla f(x)\nabla f(x)^T$$이다.

<br>
#### Multiplication
Log-convexity와 log-concavity는 곱셈(multiplication)과 양의 배수(positive scaling)를 곱하는 것에서 닫혀있다(closed). 만약, $$f$$와 $$g$$가 log-concave라면, pointwise product $$h(x) = f(x)g(x)$$ 역시 log-concave하다. 왜냐하면, $$log h(x) = log f(x) + log g(x)$$이고, 각각의 $$log f(x)$$와 $$log g(x)$$는 concave function이기 때문이다.

#### Addition and Integration
일반적으로, log-concave function의 합은 log-concave가 되지 않는다. 하지만, log-convexity는 합에 의해서는 보존된다. 예를 들어, $$f$$와 $$g$$를 log-convex function, 즉, $$F = log f$$ 그리고 $$G = log g$$가 convex하다고 하자. convex function의 합성 법칙(composition rules)에 의해, 다음을 만족한다.<br>
>$$log(exp F + exp G) = log(f + g)$$

이는 convex가 된다. (좌변이 convex인 이유는 1. log-convex는 convex이고 2. convex에 지수함수를 적용해도 convex이며 3. convex의 합과 4. convex의 log도 convex이다. 따라서, 전체 결과는 convex이다.) 결론적으로, 두 log-convex function의 합은 log-convex이다. 

이를 일반화하면 각 $$y \in C$$에 대해 $$f(x, y)$$가 log-convex이면 $$g(x)$$는 log-convex이다.
>$$g(x) = \int_C^{} f(x,y) dy $$ 

#### Integration of log-concave functions
특정 경우에 log-concavity 또한 integration에 의해 보존된다. 만약, $$f : R^n \times R^m \longrightarrow R$$가 log-concave이면, $$g(x)$$ 는 $$x \in R^n$$에서 log-concave function이다.
>$$f : R^n \rightarrow R$$ is log-concave $$\Longrightarrow$$ $$g(x) = \int_{}^{} f(x,y) dy$$ is log-concave , $$x \in R^n$$ for each $$y \in C$$.

이를 토대로, log-concave probability density의 marginal distribution이 log-concave라는 것을 확인할 수 있다.<br>

Convolution 연산에서도 log-concavity는 닫혀있다(closed). 만약, $$f$$와 $$g$$가 $$R^n$$상에서 log-concave하다면, convolution 역시 log-concave이다. 
>$$f$$, $$g$$ are log-concave on $$R^n$$ $$\Longrightarrow$$ $$(f \ast g)(x) = \int_{}^{} f(x-y)g(y) dy $$ is log-concave.<br>
