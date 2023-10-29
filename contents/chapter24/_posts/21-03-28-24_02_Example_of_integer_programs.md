---
layout: post
title: "24-02 Examples of integer programs"
chapter: "24"
order: 3
owner: "YoungJae Choung"
---

이번 절에서는 Integer program에 해당하는 다양한 예시들을 살펴보면서 어떻게 활용되는지 감을 익혀보자.

## Knapsack problem
배낭 문제(Knapsack problem)은 배낭에 넣을 수 있는 부피가 한정되어 있어 배낭 안에 들어갈 item의 총 크기가 제약되어 있을 때, 최대의 가치(value)를 가지는 item들을 선택하도록 문제를 푸는 전통적인 조합 최적화 문제이다. 이 문제는 binary variable $$x$$로 표현이 가능한데, $$j$$번째 item을 선택했는 지 아닌지에 따라 $$x_{j}$$가 0 혹은 1의 값을 가지게 된다.

> $$
> \begin{align}
> &\max_{x} && c^\intercal x \\\\
> &\text{subject to } && a^\intercal x \leq b \\\\
> &&&x_{j} \in {0, 1}, j = 1, \dotsc , n
> \end{align}
> $$

$$c_{j}, a_{j}$$ 는 각각 $$j$$번째 item의 가치(value) 와 크기(volume) 를 나타낸다.

## Assignment problem
$$n$$명의 사람들과 $$n$$개의 업무가 있다고 가정하자. 그리고 각각의 사람은 정확히 한가지의 업무에만 배당 가능하다. 여기서  $$c_{ij}$$는 사람 $$i$$가 업무 $$j$$를 수행하는 데 소요되는 비용을 의미하는데, Assignment problem은 가장 적은 비용으로 $$n$$명의 사람들을 $$n$$개의 업무를 할당하는 것을 목표로 한다. 이 때의 조건을 최적화 하기 위하여 수식으로 표현하면 다음과 같다.

> $$
> \begin{align}
> &\min_{x} &&\sum_{i = 1}^{n} \sum_{j = 1}^{n} c_{ij} x_{ij} \\\\
> &\text{subject to } &&\sum_{i = 1}^{n} x_{ij} = 1, j = 1 \dotsc n \\\\
> &&&\sum_{j = 1}^{n} x_{ij} = 1, i = 1 \dotsc n \\\\
> &&&x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc n, \quad j = 1 \dotsc n
> \end{align}
> $$


## Facility location problem
Facility location problem은 특정 시설로부터 고객까지 운송 비용을 최소화하는 것을 목표로 하는 문제이다.<br>

$$N = \lbrace 1, \dotsc, n \rbrace$$ 의 창고(depot)가 존재하고, $$M = \lbrace 1, \dotsc, m \rbrace$$ 의 고객이 있다고 가정하자.<br>
고정된 비용 $$f_{j}$$는 창고 $$j$$의 사용과 연관되어 있다.
운송 비용 $$c_{ij}$$는 고객 $$i$$에게 배송되는 물품이 창고 $$j$$로 부터 운송될 때 발생하는 비용이다.<br>

여기서 결정해야 하는 사항은 어떤 창고가 운용가능하며 어떤 고객이 각각의 창고로부터 배송을 받을 수 있는지에 대한 것으로, 고정 비용과 운송 비용을 최소화하는 쪽으로 수식을 유도해 푸는 것이다.

> $$
> \begin{align}
> &\min_{x, y} && \sum_{i = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\
> &\text{subject to } && \sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1 \dotsc m \\
> &&& x_{ij} \leq y_{j},  \quad i = 1 \dotsc m,  \quad j = 1 \dotsc n \\
> &&& x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc m, \quad j = 1 \dotsc n \\
> &&& y_{j} \in \lbrace 0, 1\rbrace \quad j = 1 \dotsc n \\
> \end{align}
> $$

첫번째 제약조건은, 각각의 고객은 하나의 창고로부터 물품을 배송받을 수 있음을 의미한다. 두번째 제약조건은 창고  $$j$$가 운영되고 있어야 고객 $$i$$가 그 곳으로 부터 물품을 배송받을 수 있다는 것을 말한다. 이 때, $$x_{ij}$$와 $$y_{j}$$가 모두 binary 이기 때문에 $$mn$$ constranint 를 생각할 수 있다. 이는 "marginalized" 형식으로 다음과 같이 제약조건으로 표현할 수도 있다.

> $$ \sum_{i = 1}^{n} x_{ij} \leq m y_{j}, \quad j = 1 \dotsc n $$

이를 반영하여 다음과 같은 수식으로 대체할 수 있다.

> $$
> \begin{align}
> &\min_{x, y} &&\sum_{i = 1}^{n} f_{j} y_{j} + \sum_{i = 1}^{m} \sum_{j = 1}^{n} c_{ij} x_{ij} \\
> &\text{subject to } &&\sum_{j = 1}^{n} x_{ij} = 1,  \quad i = 1 \dotsc n \\
> &&& \sum_{i = 1}^{n} x_{ij} \leq m y_{j}, \quad j = 1 \dotsc n \\
> &&& x_{ij} \in \lbrace 0, 1\rbrace \quad i = 1 \dotsc n, \quad j = 1 \dotsc n \\
> &&& y_{j} \in \lbrace 0, 1\rbrace \quad j = 1 \dotsc n \\
> \end{align}
> $$


## K-means and K-medoids clustering
군집(clustering)은 데이터를 유사한 그룹으로 나누는 것으로, K-means 알고리즘은 군집 내의 데이터 포인트들 간의 거리를 평균으로 $$K$$개의 중심값(centroid)을 찾아 K개의 군집을 찾는 문제로,  partition $$S_{1} \cup \dotsc \cup S_{K} = \lbrace 1, \dotsc, n \rbrace$$ 를 주어진 데이터에서 찾는 것을 목표로 한다. 이 때 다음 수식을 최소화 한다.

$$ \sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - \mu^{(i)} \|^{2} $$

where $$ \mu^{(i)} :  = \frac{1}{| S_{i} |} \sum_{j \in S_{i}} x^{(i)} $$,
$$ \mu^{(i)} $$ 는 cluster $$i$$의 centroid를 의미한다.

평균을 계산해서 centroid를 구하는 것 (K-means) 보다 좀 더 Outlier에 Robust한 방법은 K개의 군집의 중심값을 산술평균으로 구하는 대신 군집의 중심에 가장 가까운 하나의 데이터 포인트를 중심값으로 정하는 방법 (K-medoids clustering) 이다.
즉, 각각의 data point ($$y^{(i)}$$)를 중심점으로 생각하고 이를 계산하였을 때 최소값이 나올 수 있는 data point를 centroid로 지정하는 방법 (K-medoids clustering) 이다.

>$$\sum_{i = 1}^{K} \sum_{j \in S_{i}} \| x^{(j)} - y^{(i)} \|^{2} $$
>$$\text{where } y^{(i)} \in \lbrace x^{(j)} : j \in S_{i} \rbrace $$

<br>
이 문제는 integer program으로 변형하여 나타내어 질 수 있다.
먼저,  $$ d_{ij} = \| x^{(i)} - x^{(j)} \|^2 $$ 를 정의하고, 다음 두 가지의 binary variable을 정의 한다.

$$\begin{align}
&w_{i} =\begin{cases}1 && \text{if choose } x^{(i)} \text{ as a centroid} \\\\
0 && \text{otherwise.} \end{cases}\\\\
&z_{ji} =\begin{cases}1 && \text{if } x^{(j)} \text{ in the cluster with centroid } x^{(i)} \\\\
0 && \text{otherwise.} \end{cases}
\end{align}$$

<br>

K-medoids 문제는 optimization problem으로 정의하면 다음과 같다.

> $$
> \begin{align}
> &\min_{w, z} && \sum_{i = 1}^{n} \sum_{j = 1}^{n} d_{ij} z_{ji} \\\\
> &\text{subject to } && z_{ji} \leq w_{i} \\\\
> &&& \sum_{i = 1}^{n} w_{i} = k \\\\
> &&& w_{ij} \in 0, 1 \quad i = 1 \dotsc n \\\\
> &&& z_{ji} \in 0, 1 \quad j, i = 1 \dotsc n
> \end{align}
> $$

첫번째 제약조건은 centroid가 먼저 정해지고 난 후, $x_{i}$에 대한 $x_{j}$가 있는 지 없는 지 판별하겠다는 것을 의미한다.

## Best subset selection
$$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}, \quad y \in \mathbb{R}^{n}$$ 조건이 주어졌을 때, Best subset selection 문제는 다음과 같다.

> $$
> \begin{align}
> &\min_{\beta} &&\frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } &&\| \beta \| \leq k\\\\
> \end{align}$$
> $$\begin{align}
> \text{where}  \| \beta \|_{0}  :  = \text{ the number of nonzero entries of } \beta.
> \end{align}
> $$

$$ \| \beta \|_{0} $$는 Non-convex constraint 이기 때문에 Integer programing 으로 변형해서 문제를 풀면 좀 더 수월하게 풀 수 있다.

> $$
> \begin{align}
> &\min_{\beta, z} && \frac{1}{2} \| y - X\beta \|^{2} \\\\
> &\text{subject to } && | \beta_{i} | \leq Mz_{i} \quad i = 1 \dotsc n \\\\
> &&&z_{ji} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc n \\\\
> &&&\sum_{i = 1}^{p} z_{i} \leq k
> \end{align}
> $$

## Least median of squares regression
$$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}, \quad y \in \mathbb{R}^{n}$$, 그리고 $$\beta \in \mathbb{R}^{p} $$ 조건이 주어졌을 때, $$r : = y - X\beta $$ 로 정의하면, Least median of squares regression 문제는 다음과 같다.

> $$\beta_{LMS} : = \arg\min_{\beta} (median | r_{i} | ).$$
