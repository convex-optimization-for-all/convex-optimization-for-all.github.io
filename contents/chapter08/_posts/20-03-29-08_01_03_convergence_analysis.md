---
layout: post
title: 08-01-03 Convergence analysis
chapter: "08"
order: 5
owner: "Kyeongmin Woo"
---

# Convergence analysis

Gradient descent에서는 $$\nabla f$$가 Lipschitz continous하다고 가정하였지만 subgradient method에서는 $$f$$가 Lipschitz continous하다고 가정한다. (Gradient descent의 convergence theorem [06-03-01]({% post_url contents/chapter06/21-03-20-06_03_01_convergence_analysis_and_proof %}) 절을 참조)

$$f$$는 convex이고 dom $$f = R^n$$이며 $$f$$가 Lipschitz condition을 만족한다고 하자.

>\begin{align}
> | f(x) - f(y) | \le G \lVert x - y \rVert_2 \text{ for all } x, y
\end{align}

다음과 같은 가정이 주어지면 fixed step sizes와 diminishing step sizes의 convergence 공식은 각각 다음과 같다. 

## Convergence theorem for fixed step sizes 

Fixed step sizes는 다음과 같은 수렴성을 가진다.
>\begin{align}
> \lim_{k→\infty} f(x^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}

## Convergence theorem for diminishing step sizes 

Diminishing step sizes method는 다음과 같은 수렴성을 가진다.

>\begin{align}
\lim_{k→\infty}f(x^{(k)}_{best}) = f^*
\end{align}

## Proofs

Fixed step-sizes와 diminishing step-sizes의 증명은 각각 다음과 같다.

## Proof of convergence theorem for fixed step sizes

Fixed step size method는 $$\sum_{i=1}^{k}t_{i} = kt$$임을 이용하여 증명한다.  

>$$\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} = \frac{R^{2}+G^{2}k t^{2}}{2kt}  = \frac{R^{2}}{2tk} + \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^*) \le 0 + \frac{G^{2}t}{2} = \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}
$$


## Proof of convergence theorem for diminishing step sizes 

Diminishing step sizes가 만족하는 아래의 성질 (1), (2)를 이용하여 basic inequality에서부터 증명한다. 

>$$
\begin{align}
\text{(1)} \sum_{i=1}^{\infty} t_i = \infty, \quad \text{(2)}  \sum_{i=1}^{\infty} t_i^{2} = \beta < \infty
\end{align}
$$

>$$
\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^* ) \le \frac{R^{2}+G^{2}\beta}{2\infty} = 0 \\
& \lim_{k→\infty}(f^{(k)}_{best}) =  f^* \\
\end{align}
$$