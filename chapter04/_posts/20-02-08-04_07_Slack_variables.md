---
layout: post
title: Slack variables
chapter: "04"
order: 7
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Slack variable $s$를 사용하여 inequality constraint를 equality constraint로 변환하는 방법에 대해 알아보자.

>$$
>\begin{aligned}
>    &\text{min}\_{x} &{f(x)} \\\\
>    &\text{subject to } &{g_{i}(x) \leq 0, i = 1, .., m} \\\\
>    & &{Ax = b}. \\\\
>\end{aligned}
>$$

위의 convex problem은 다음의 문제와 동일하다.

>$$
>\begin{aligned}
>    &\text{min}\_{x, s} &{f(x)} \\\\
>    &\text{subject to } &{s\_{i} \geq 0, i = 1, .., m} \\\\
>    & &{g\_{i}(x) + s\_{i} = 0, i = 1,...m}\\\\
>    & &{Ax = b}. \\\\
>\end{aligned}
>$$

주의해야 할 점은 $g\_i, i = 1, \dotsc, m$이 affine이 아니라면 위의 문제는 더이상 convex problem이 아니라는 것이다.
