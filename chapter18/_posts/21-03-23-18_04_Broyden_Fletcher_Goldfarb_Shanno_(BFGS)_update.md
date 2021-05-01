---
layout: post
title: 18-04 Broyden-Fletcher-Goldfarb-Shanno (BFGS) update
chapter: "18"
order: 5
owner: "Hooncheol Shin"
---

BFGS의 아이디어는 DFP와 동일하다. 다만, B와 H의 역할이 뒤바뀌는 것만이 차이점이다.

BFGS는 다음 문제를 푸는 것으로 유도된다.

>Solve
>$$
>\begin{align}
>    \min_{H^+} \: \: &{\|W^{1/2} (H^+ - H) W^{1/2} \|_F} \\\\
>    \text{subject to } &{H^+ = (H^+)^T} \\\\
>    &{H^+s = y}  \\\\
>\end{align}\\\\
>\text{where } W \in \mathbb{R}^{n \; \times \;n} \text{ is nonsingular and such that } Ws_k = y_k.
>$$

유도되는 $$H$$와 $$B$$ 에 대한 updating formula는 다음과 같다.

>$$
> B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts}
>$$

and

>$$
>\begin{align}
>H^+ &= H + \frac{(s-Hy)s^T}{y^Ts} + \frac{s(s-Hy)^T}{y^Ts} - \frac{(s-Hy)^Ty}{(y^Ts)^2} ss^T\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts} 
>\end{align}
>$$

BFGS 또한 DFP처럼 positive definiteness를 유지한다. (만약 $$B$$가 positive definite이고 $$s^Ty > 0$$이면 $$B^+$$는 positive definite이다.)

BFGS의 특장점은 self-correcting property를 지니고 있다는 것이다. 만약 행렬 $$H$$가 부정확하게 추정되어 iteration의 속도가 느려지게 되면 Hessian approximation이 단 몇 step 만에 이를 바로잡는 경향성을 보인다. 반면 DFP는 잘못된 Hessian approximation의 추정에 대해 효과적으로 바로잡지 못하므로 실전에서는 보통 BFGS의 성능이 더 좋은 편이다 [14].