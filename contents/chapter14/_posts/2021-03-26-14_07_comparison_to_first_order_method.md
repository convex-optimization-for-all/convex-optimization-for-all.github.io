---
layout: post
title: 14-07 Comparison to first-order method
chapter: "14"
order: 13
owner: "Minjoo Lee"
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

이 장에서는 개괄적인 관점에서 Newton's method와 gradient descent를 비교해본다. 정의역의 dimension은 $$n$$이라 하자.

| 항목 | Newton's method | Gradient descent |
| -------- | -------- | -------- |
| Memory     | $$O(n^{2})$$($$n \times n$$의 hessian matrix) storage     | $$O(n)$$($$n$$-dimensional gradient) storage |
| Computation     | $$O(n^{3})$$ flops($$n \times n$$의 선형시스템 계산)     | $$O(n)$$ flops($$n$$-dimensional vector의 선형 결합)     |
| Backtracking     | $$O(n)$$ | $$O(n)$$  |
| Conditioning     | Affine invariant 등, conditioning에 크게 영향받지 않음  | 큰 영향을 받을 가능성 존재 |
| Fragility     | bugs나 numerical errors에 민감 | newton's method보다 비교적 강건 |

## Example

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd(1).jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Logistic regression [3]</figcaption>
</p>
</figure>

위의 figure 1은 앞서 [14-04]({% post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})에서 다룬 logistic regression 예시이다. x축을 실제로 연산에 걸린 시간으로 바꿔서 보면 다음과 같다. 
Convergence analysis에서 다룬 바와 같이 Newton's method는 두가지 phase를 가진다. 그래프에서도 일정 시간 후, 빠른 수렴(quadratic convergence)을 보이는 것을 확인할 수 있다. iteration 초반부인 Newton's method의 damped phase에서는 gradient descent와 동일한 scale의 수렴속도를 보인다. 하지만, $$O(n^{3})$$의 연산을 수행해야하기 떄문에 실제 연산시간 상에선 더 느린 수렴을 보인다. 이 후 backtracking line search가 더 이상 필요하지 않은 iteration에 도달하면, quadratic convergence의 속도를 보이며 매우 빠르게 수렴함을 확인할 수 있다.