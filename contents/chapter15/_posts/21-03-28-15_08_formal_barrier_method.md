---
layout: post
title: 15-08 Formal barrier method
chapter: "15"
order: "01"4
owner: "Minjoo Lee"
---
Open convex set $$D \subset \mathbb{R}^n$$로 정의되는 convex function $$\phi : D \to \mathbb{R}$$가 다음의 조건을 만족시키면, 그 function은 파라미터 $$\nu$$를 갖는 **self-concordant barrier**이다.

* $$\phi$$는 self-concordant
* 모든 $$x \in D$$에 대해 다음과 같이 상수 $$\nu$$에 bound되는  newton decrement를 갖는다.

> $$\lambda(x)^2 = \nabla \phi(x) (\nabla^2 \phi(x))^{-1} \nabla \phi(x) \le \nu$$

다음 LP 문제를 고려해보자. (여기서 $$\bar{D}$$는 domain $$D$$의 closure이다.)
>$$\begin{align}
\min_{x} & \quad c^Tx \\\
\text{subject to } & \quad x \in \bar{D}  \\\
\end{align}$$

이 문제는 다음과 같은 문제로 근사된다.
>$$\begin{align}
\min_{x} & \quad tc^Tx + \phi(x) \\\
\end{align}$$

여기서, $$\phi_t(x) := tc^Tx + \phi(x)$$라고 하고 이에 해당하는 newton decrement를 $$\lambda_t(x)$$라고 하자.

Key observation : $$t^+ \gt t$$의 경우
>$$\begin{align}
\lambda_t^+(x) \le \quad \frac{t^+}{t}\lambda_t^+(x) + \left ( \frac{t^+}{t} -1 \right ) \sqrt{\nu}  \\\
\end{align}$$

## Theorem

>$$\begin{align}
& \text{if} \quad \lambda_t(x) \le \frac{1}{9} \quad \text{and} \quad \frac{t^+}{t} \le 1 + \frac{1}{8 \sqrt{\nu}} \quad \text{then} \quad \lambda_t^+(x^+) \le \frac{1}{9}  \\\
& \qquad \qquad \text{for} \quad x^+ = x - (\nabla^2 (\phi_{t^+}(x))^{-1} \nabla (\phi_{t^+}(x)
\end{align}$$

결론적으로 $$\lambda_{t^{(0)}}(x^{(0)}) \lt \frac{1}{9}$$가 되도록 $$x^{(0)}, t^{(0)}$$으로 시작하고 $$\mu := 1 + \frac{1}{8 \sqrt(\nu)}$$으로 선택한다면, 각 centering step마다 한 newton step이면 충분하다.
