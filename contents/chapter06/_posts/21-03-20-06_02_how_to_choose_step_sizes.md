---
layout: post
title: 06-02 How to choose step sizes
chapter: "06"
order: "03"
owner: "Kyeongmin Woo"
---

# How to choose step sizes

Gradient descent를 반복할 때, **step size**는 $$x$$ 값을 갱신하며 그 값에 따라 optimal로 수렴하는 속도를 달라지게 만들거나 혹은 발산하게 한다. 이 절에서는 step size 값을 적절하게 도출하는 방법을 다음 세가지로 제시하면서 gradient descent 기법 안에서 더 빠르게 optimal 값을 찾을 수 있도록 한다.

- Fixed step size
- Backtracking line search
- Exact line search