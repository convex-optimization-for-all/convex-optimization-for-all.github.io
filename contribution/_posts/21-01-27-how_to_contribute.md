---
layout: post
title: "How to Contribute"
chapter: home
order: 3
owner: kyeongminwoo
---

---

## 1. 컨텐츠를 직접 수정하는 방법

#### (1) 우선 Local의 Repository Directory로 들어갑니다. Local Repository가 없다면 [Initial Settings](<https://convex-optimization-for-all.github.io/contribution/2021/01/27/initial_settings/>)를 참고하시기 바랍니다.

#### (2)  Remote 저장소와의 정보를 동기화합니다.

```
$ git checkout main
$ git pull --all
```

#### (3) 수정 내용을 담는 새로운 브랜치를 생성합니다. 브랜치 명은 `[Prefix]/[챕터명]/[수정하는_이유]`로 하시면 됩니다([Branch Naming Convetion](<https://convex-optimization-for-all.github.io/contribution/2021/02/03/conventions/>)). 예시는 아래와 같습니다.

```bash
$ git checkout -b bugfix/chapter01/fix_type
```

#### (4) 파일을 편집합니다. 생성 또는 수정하고자 하는 컨텐츠는 [Convention](<https://convex-optimization-for-all.github.io/contribution/2021/02/03/conventions/>)을 지켜 작성해야 합니다.

#### (5) Remote로 Push합니다. 예시는 아래와 같습니다.

```
$ git push origin bugfix/chapter01/fix_type
```

#### (6) [Github](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/pulls>)에서 main branch로의 Pull Request를 생성합니다. Pull Request 생성 방법은 아래 GitHub Dosc를 참고하시기 바랍니다.

- [Creating a pull request](<https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request>)

---

## 2. 컨텐츠 수정을 요청하는 방법

- Github Repository에 [Issue](<https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/issues>)를 생성하실 수 있습니다.

---
