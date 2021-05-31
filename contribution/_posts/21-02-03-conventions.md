---
layout: post
title: "Conventions"
chapter: home
order: "02"
owner: "Kyeongmin Woo"
---

## 1. Directory Convention

- 주요 컨텐츠는 `contents/chapter`로 시작하는 디렉토리에 포함되어 있습니다. 또한 컨텐츠에 필요한 이미지는 `image` 디렉토리에 들어 있습니다.
- `contents/chapter`의 내부 디렉토리는 다음과 같습니다.

```
contents
├── chapter01
│   ├── _posts
│   │   ├── 21-01-07-01_00_Introduction.md
│   │   ├── 21-01-07-01_01_optimization_problems.md
│   │   ├── 21-01-28-01_02_convex_optimization_problem.md
│   │   ├── 21-01-28-01_03_goals_and_topics.md
│   │   └── 21-01-28-01_04_brief_history_of_convex_optimization.md
│   ├── index.html
...
```

- Jekyll에서는 `_posts` 디렉토리 내에 있는 Markdown 또는 html 파일을 블로그의 Posting으로 인식합니다. 따라서 새로운 포스팅을 작성하고자 한다면 각 디렉토리의 `_posts`에 새로 파일을 추가하시면 됩니다.
- Jekyll의 Posting 파일들은 모두 아래와 같은 Naming Convention을 따라야 합니다.
    - `yy-mm-dd-new_posting_name.md`
- `chapter`와 `image` 디렉토리 외의 내용들은 모두 Blog의 설정과 관련된 것들입니다. 안정적인 운영을 위해 설정과 관련된 부분들에 대해서는 직접 편집보다는 이슈로 작성해주시면 처리하겠습니다(관련 내용 수정 시 PR Merge가 어려울 수 있습니다).

## 2. Posting Convention

### 2.1. Header Field

- 모든 Posting 파일들은 다음 예시와 같은 Header를 가지고 있어야 합니다.

```
---
layout: post
title: Quasi-Newton Methods
chapter: "18"
order: "01"
owner: "Kyeongmin Woo"
---
```

- **layout**은 `post`여야 합니다.
- **title**은 내용에 맞게 임의의 String으로 설정할 수 있습니다.
- **chapter**는 상위 카테고리의 마지막 두 숫자를 String으로 표기합니다. 다만 한 자리수인 경우 "01"과 같이 0을 붙여줘야 합니다.
- **order**는 해당 chapter 내에서의 정렬 순서를 의미합니다.
- **owner**는 해당 post의 관리자를 의미합니다.

### 2.2. Latex

- 수식은 Latex 문법에 따라 표기합니다.
- $$ 와 같이 double dollar sign을 사용하여 수식임을 나타냅니다.

```
$$\theta x_1 + (1-\theta)x_2 \in C$$
```

위 수식은 다음과 같이 표기됩니다.

$$\theta x_1 + (1-\theta)x_2 \in C$$

### 2.3. Image Convention

- Posting 파일에서 이미지를 삽일할 때 아래의 Convention을 따라야합니다.

```
<figure class="image" style="align: center;">
<p align="center">
  <img src="{image_path}" alt="{description of image}" width="{scale_ratio}%" height="{scale_ratio}%">
  <figcaption style="text-align: center;">{figcaption}</figcaption>
</p>
</figure>
```

- figure class는 `image`여야합니다.
- {}에 들어갈 내용을 적절히 넣어야합니다.

### 2.4 Hyperlink Convention

- Blog 내의 Post에 대한 hyperlink는 jekyll post_url을 사용합니다. 첫 번째 Post인 [Optimization problems?]({% post_url contents/chapter01/21-01-07-01_01_optimization_problems %}
)의 hyperlink는 아래와 같이 작성합니다.

```
[Optimization problems?]({% post_url contents/chapter01/21-01-07-01_01_optimization_problems %})
```

- 기타 외부 Url로의 hyperlink는 다음과 같이 작성할 수 있습니다.

```
[Convex Optimization 위키](<https://bit.ly/2PXv736>)
```

## 3. GitHub Convnention

작성 내용에 질문이 있거나 수정 사항을 발견하신 경우 다음 두 방법 중 하나로 남겨주시면 됩니다.

- 댓글 작성하기
- Repogitory에 이슈 생성하기

새로운 내용을 추가하거나 직접 편집하시고 싶으신 경우에는 새로운 Branch를 생성하여 먼저 수정하신 후 `Pull Request`를 생성해주시면 됩니다. 신규 작성 및 기존 내용 수정은 누구나 가능합니다.

### 3.1. Repository Policy

`main` 브랜치로 Merge 되기 위해서는 1명 이상의 Reviewer가 Approve 해야 합니다. CODEOWNERS 시스템이 도입되어 있어 각 Chapter 별 Reviewer가 자동으로 할당됩니다.

### 3.2. Branch Naming Convention

브랜치 이름은 다음 컨벤션에 맞춰 생성해주시면 됩니다.

```
[feature|bugfix]/[chapter**|settings]-변경-사항
```

Prefix는 feature와 bugfix 두 가지를 사용합니다. 각각의 사용 예시는 다음과 같습니다.

- feature
  - Migration 작업
  - 문장/수식/이미지 등이 달라지는 경우
  - 새로운 내용이 추가되는 경우
- bugfix
  - 오타를 수정하는 경우
  - latex view가 깨져 수정하는 경우 

구체적인 예시는 아래와 같습니다.

- `feature/chapter01-migration`: chapter01 Migration
- `feature/chapter01-fix-formula`: chapter01에서 수식 업데이트 
- `feature/settings-update-branch-convention`: Convention 업데이트
- `bugfix/chapter01-fix-typo`: chapter01에서 오타 수정
