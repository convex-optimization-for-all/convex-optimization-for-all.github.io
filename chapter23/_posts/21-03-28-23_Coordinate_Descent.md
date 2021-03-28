---
layout: post
title: "23 Coordinate Descent"
chapter: "23"
order: 1
owner: "YoungJae Choung"
---

Coordinate descent는 반복적으로 각 좌표축을 따라 움직이며 목적함수의 최솟값을 찾는 최적화 알고리즘이다. 각 반복(iteration)에서 좌표 선택 규칙(coordinate selection rule)에 따라 좌표축(coordinate) 또는 좌표축 블록(coordinate block)을 결정한 뒤, 선택되지 않은 좌표축 또는 좌표축 블록은 고정한 채로 축의 방향을 따라 함수를 최소화시킨다 (exact or inexactly). Coordinate descent는 gradient를 이용하는 방식뿐 아니라 gradient를 이용하지 않는 방식으로도 활용할 수 있다. 또한, 경우에 따라 각 축에 대해 적합한 step size를 결정하기 위하여 line search를 이용할 수 있다 [16].

Coordinate descent는 매우 간단하여 구현하기가 쉽고, 적합한 문제에 대해 주의깊게 구현될 경우 아주 좋은 성능을 보인다.

**Examples:** lasso regression, lasso GLMs (under proximal Newton), SVMs, group lasso, graphical lasso (applied to the dual), additive modeling, matrix completion, regression with nonconvex penalties

## References and Further readings

**최적화에서의 초기 coordinate descent:**

* D. Bertsekas and J. Tsitsiklis (1989), “Parallel and distributed domputation: numerical methods”
* Z. Luo and P. Tseng (1992), “On the convergence of the coordinate descent method for convex differentiable minimization”
* J. Ortega and W. Rheinboldt (1970), “Iterative solution of nonlinear equations in several variables”
* P. Tseng (2001), “Convergence of a block coordinate descent method for nondifferentiable minimization”
35 Early coordinate descent references in statistics and ML:
* I. Daubechies and M. Defrise and C. De Mol (2004), “An iterative thresholding algorithm for linear inverse problems with a sparsity constraint”
* J. Friedman and T. Hastie and H. Hoefling and R. Tibshirani (2007), “Pathwise coordinate optimization”
* W. Fu (1998), “Penalized regressions: the bridge versus the lasso”
* T. Wu and K. Lange (2008), “Coordinate descent algorithms for lasso penalized regression”
* A. van der Kooij (2007), “Prediction accuracy and stability of regresssion with optimal scaling transformations”

**Coordinate descent의 응용:**

* O. Banerjee and L. Ghaoui and A. d’Aspremont (2007), “Model selection through sparse maximum likelihood estimation”
* J. Friedman and T. Hastie and R. Tibshirani (2007), “Sparse inverse covariance estimation with the graphical lasso”
* J. Friedman and T. Hastie and R. Tibshirani (2009), “Regularization paths for generalized linear models via coordinate descent”
* C.J. Hsiesh and K.W. Chang and C.J. Lin and S. Keerthi and S. Sundararajan (2008), “A dual coordinate descent method for large-scale linear SVM”
* R. Mazumder and J. Friedman and T. Hastie (2011), “SparseNet: coordinate descent with non-convex penalties”
* J. Platt (1998), “Sequential minimal optimization: a fast algorithm for training support vector machines”
37 Recent theory for coordinate descent:
* A. Beck and L. Tetruashvili (2013), “On the convergence of block coordinate descent type methods”
* Y. Nesterov (2010), “Efficiency of coordinate descent methods on huge-scale optimization problems”
* J. Nutini, M. Schmidt, I. Laradji, M. Friedlander, H. Koepke (2015), “Coordinate descent converges faster with the Gauss- Southwell rule than random selection”
* A. Ramdas (2014), “Rows vs columns for linear systems of equations—randomized Kaczmarz or coordinate descent?”
* P. Richtarik and M. Takac (2011), “Iteration complexity of randomized block-coordinate descent methods for minimizing a composite function”
* A. Saha and A. Tewari (2013), “On the nonasymptotic convergence of cyclic coordinate descent methods”
* S. Wright (2015), “Coordinate descent algorithms”
38 Screening rules and graphical lasso references:
* L. El Ghaoui and V. Viallon and T. Rabbani (2010), “Safe feature elimination in sparse supervised learning”
* R. Tibshirani, J. Bien, J. Friedman, T. Hastie, N. Simon, J. Taylor, and R. J. Tibshirani (2011), “Strong rules for discarding predictors in lasso-type problems”
* R. Mazumder and T. Hastie (2011), “The graphical lasso: new insights and alternatives”
* R. Mazumder and T. Hastie (2011), “Exact covariance thresholding into connected components for large-scale graphical lasso”
* J. Wang, P. Wonka, and J. Ye (2015), “Lasso screening rules via dual polytope projection”
* D. Witten and J. Friedman and N. Simon (2011), “New insights and faster computations for the graphical lasso”

**Convergence analysis:**<br>
Coordinate descent의 convergence analysis에 대한 연구 흐름을 간략히 소개하겠다.

* Convergence of coordinatewise minimization for solving linear systems, the Gauss-Seidel method, is a classic topic. E.g., see Golub and van Loan (1996), or Ramdas (2014) for a modern twist that looks at randomized coordinate descent
* Nesterov (2010) considers randomized coordinate descent for smooth functions and shows that it achieves a rate O(1/ε) under a Lipschitz gradient condition, and a rate O(log(1/ε)) under strong convexity
* Richtarik and Takac (2011) extend and simplify these results, considering smooth plus separable functions, where now each coordinate descent update applies a prox operation
* Saha and Tewari (2013) consider minimizing l1 regularized functions of the form g(β) + λ∥β∥1, for smooth g, and study both cyclic coordinate descent and cyclic coordinatewise min. Under (very strange) conditions on g, they show both methods dominate proximal gradient descent in iteration progress
* Beck and Tetruashvili (2013) study cyclic coordinate descent for smooth functions in general. They show that it achieves a rate O(1/ε) under a Lipschitz gradient condition, and a rate O(log(1/ε)) under strong convexity. They also extend these results to a constrained setting with projections
* Nutini et al. (2015) analyze greedy coordinate descent (called Gauss-Southwell rule), and show it achieves a faster rate than randomized coordinate descent for certain problems
* Wright (2015) provides some unification and a great summary. Also covers parallel versions (even asynchronous ones)
* General theory is still not complete; still unanswered questions (e.g., are descent and minimization strategies the same?)