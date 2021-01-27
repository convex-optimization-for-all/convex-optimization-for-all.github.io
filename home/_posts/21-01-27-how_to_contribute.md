---
layout: post
title: "How to contribute Open Source Project"
---

## 컨텐츠를 직접 수정하는 방법

1. 처음이라면 [Blog Repository](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io>)를 Clone하고, README의 `시작하기`에 따라 로컬 호스팅 환경을 구축한다.
2. 새로운 브랜치를 생성한다. 브랜치 명은 `chapter01/[수정하는_이유]`로 한다.
3. 직접 수정한다. 생성 및 수정하고자 하는 컨텐츠에 대한 사항은 README의 `Directory Convention`와 `Posting Convention`을 한다.
4. Push한다.
5. Pull Request를 생성한다.

---

## 컨텐츠 수정을 요청하는 방법

1. Github Repository에 Issue를 생성한다.
2. Blog에 댓글을 남긴다.

---

## 직접 수정하기 위해 읽으면 좋은 글

### Jekyll

본 Repository의 컨텐츠들은 Jekyll을 사용하여 [Github Blog](<https://convex-optimization-for-all.github.io/>)로 호스팅됩니다. 따라서 기존 내용을 편집하거나 새로운 내용을 작성하기 위해서는 Jekyll의 디렉토리 구조 및 컨텐츠 작성 규약을 준수하여 작성해야 합니다. 아래 기본적인 작성 규칙을 참고하시거나 [Jekyll 공식 문서](<https://jekyllrb-ko.github.io/>)를 확인하시기 바랍니다. 이와 관련하여 작성에 어려움이 있으신 분들께서는 아래 메일로 문의주시면 도와드리겠습니다.

(우경민, wgm0601@gmail.com)

#### 시작하기

- [Repository Clone](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io>): 먼저 본 Repository를 로컬 환경에 클론합니다.
- [루비 설치하기](<https://jekyllrb-ko.github.io/docs/installation/>): Jekyll은 루비로 제작되어있습니다. 따라서 Jekyll을 사용하기 위해서는 루비를 설치해야 합니다.
- [Jekyll 설치하기](<https://jekyllrb-ko.github.io/docs/>): 루비를 설치했다면 클론한 Repository에 들어가 Jekyll을 설치합니다.
- [Bundle Gem 설치하기](<https://jekyllrb-ko.github.io/docs/>): 호스팅에 필요한 루비 패키지들을 추가적으로 설치해야 해주어야 합니다. Repository의 프로젝트 디렉토리에서 다음 명령어를 실행합니다.
- `$ bundle install`

#### 로컬 호스팅

- 컨텐츠를 수정했다면 Push하기 전 로컬에서 수정 내용이 잘 반영되었는지 먼저 확인해야 합니다. Jekyll에서 요구하는 규약을 지키지 않은 경우 Blog가 정상적으로 동작하지 않을 수 있고, 이러한 내용을 Push한다면 실제 웹에서 호스팅되는 Blog가 동작하지 않을 수 있습니다.
- 설치가 완료되었다면 프로젝트 디렉토리에서 다음 명령어를 실행하여 Local Server에 띄울 수 있습니다.

```
$ jekyll serve
```

- 호스팅이 되지 않는다면 다음 명령어로도 시도해 볼 수 있습니다.

```
$ bundle exec jekyll serve
```

- 두 명령어 모두 되지 않는다면 Jekyll 환경이 제대로 설치되지 않은 것입니다.

#### Directory Convention

- 주요 컨텐츠는 `chapter`로 시작하는 디렉토리에 포함되어 있습니다. 또한 컨텐츠에 필요한 이미지는 `image` 디렉토리에 들어 있습니다.
- `chapter`의 내부 디렉토리는 다음과 같습니다.

```
chapter01
| - _posts
  | - 20-01-08-text.md
| - index.html
```

- Jekyll에서는 `_posts` 디렉토리 내에 있는 Markdown 또는 html 파일을 블로그의 Posting으로 인식합니다. 따라서 새로운 포스팅을 작성하고자 한다면 각 디렉토리의 `_posts`에 새로 파일을 추가하시면 됩니다.
- Jekyll의 Posting 파일들은 모두 아래와 같은 Naming Convention을 따라야 합니다.
    - `yy-mm-dd-new_posting_name.md`
- `chapter`와 `image` 디렉토리 외의 내용들은 모두 Blog의 설정과 관련된 것들입니다. 안정적인 운영을 위해 설정과 관련된 부분들에 대해서는 직접 편집보다는 이슈로 작성해주시면 처리하겠습니다(관련 내용 수정 시 PR Merge가 어려울 수 있습니다).

#### Posting Convention

- 모든 Posting 파일들은 다음 예시와 같은 Header를 가지고 있어야 합니다.

```
---
layout: post
title: Quasi-Newton Methods
chapter: "18"
---
```

- layout은 `post`여야 합니다.
- title은 내용에 맞게 임의의 String으로 설정할 수 있습니다.
- chapter는 상위 카테고리의 마지막 두 숫자를 String으로 표기합니다. 다만 한 자리수인 경우 "01"과 같이 0을 붙여줘야 합니다.
- 이외의 내용들은 모두 Markdown 작성 방법에 맞춰 작성해주시면 됩니다.

### Github Convnention

작성 내용에 질문이 있거나 수정 사항을 발견하신 경우 다음 두 방법 중 하나로 남겨주시면 됩니다.

- 댓글 작성하기
- Repogitory에 이슈 생성하기

새로운 내용을 추가하거나 직접 편집하시고 싶으신 경우에는 새로운 Branch를 생성하여 먼저 수정하신 후 `Pull Request`를 생성해주시면 됩니다. 신규 작성 및 기존 내용 수정은 누구나 가능합니다.

#### Branch Naming Convention

브랜치 이름은 다음 컨벤션에 맞춰 작성해주시면 됩니다.

- `chapter01/[내용]` : Posting 관련 수정 사항
- `setting/[내용]` : Blog 설정 관련 수정 사항