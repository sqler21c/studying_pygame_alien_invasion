# This is git play ground.. hahaha __ Just try
## git은 데이터를 추가할 뿐
git은 무얼 하든 git 데이터베이스에 데이터가 추가 된다. 되돌리거나 데이터를 삭제할 방법이 없다. 다른 VCS처럼 git도 커밋하지 않으면 변경 사항을 읽어버릴 수 있다. 하지만 일단 스냅샷을 커밋하고 나면 데이터를 읽어버리기 어렵다

git을 사용하면 프로제트가 심각하게 망가질 걱정 없이 매우 즐겁게 여러가지 실험을 해 볼 수 있다. [되돌리기](#되돌리기)를 보면 git에서 데이터를 어떻게 저장하고 손신을 어떻게 복구하는지 알 수 있다. 

## 세 가지 상태
이  부분은 중요하기에 집중해서 일겅야 한다. git을 공부하기 위해 반드시 짚고 넘어가야 할 부분이다. git은 파일을 **committed**, **modified**, **staged** 이렇게 세가지 상태로 관리한다.
- **committed** : 데이터가 로컬 데이터베이스에 안전하게 저장됐다는 것을 의미
- **modified** : 수정한 파일을 아직 로컬 데이터베이스에 커밋하지 않은 것을 말함
- **staged** : 현재 수정한 파일을 곧 커밋할 것이라고 표시한 상태
이 세가지 상태는 git프로젝트의 세 가지 단계와 연결돼 있다. git 디렉토리, 워킹 트리, staging area이렇게 세가지 단계를 이해 하고 넘어가자

git으로 하는 일은 기본적으로 아래와 같다
1. 워킹 트리에서 파일을 수정한다
2. staging area에 파일을 stage해서 커밋할 스냅샷을 만든다. 모든 파일을 추가할 수도 있고 선택하여 추가할 수도 있다.
3. Staging area에 있는 파일들을 커밋해서 git디렉토리에 영구적인 스냅샷으로 저장

git디렉토리에 있는 파일들든 committed상태. 파일을 수정하고 stage agrea에 추가 했다면 staged이다. 그리고 checkout하고 나서 수정했지만, 아직 staging area에 추가 하지 않으면 modified이다. [git의 기초](#git의-기초)에서 이 상태에 대해 좀더 자세히 다룬다. 특히 staging area를 이용하년 방법부터 아예 생각하는 방법까지도 설명 함

## install git
### linux 설치
```linux
sudo dnf install git-all
```
### mac 설치
[check here](http://git-scm.com/download/mac)

### Window 설치
[check here](http://git-scm.com/download/win)

### 사용자 정보
설치 후 한번 설정후 이후 모든 git에서 사용시 사용된다.
```
git config --global user.name "jon do"
git config --global user.email jon.do@example.com
```
각 저장소마다 다르게 적용, 해당 폴더에 이동후 아래 사용
```
git config --local user.name "local"
git config --local user.email local@example.com
```

둘다 설정이 되어 있다면 lcoal먼저 적용된다.

### 편집기
> git config --global core.editor "경로"

### 설정확인
> git config --list

### 사용자확인
> git config user.name

### 도움말
> git help --> win
> man git  --> linux

예를 들어 git config명령에 대한 도움말
> git help config

## git의 기초
git에서 자주 사용하는 명령어는 모두 여기서. 파일을 추적하거나 추적을 그만 두는 방법, 변경 내용을 stage하고 커밋하는 방법, 파일이나 파일 패넌을 무시하도록 git을 설정하는 방법, 실수를 쉽고 빠르게 만회하는 방법, 프로젝트 히스토리를 조회하고 커밋을 비교하는 방법, 리모트 저장소에 push하고 pull하는 방법

### 저장소 만들기
주로 다음 두 가지 중 한 가지 방법으로 
1. 이직 버전관리를 하지 않는 로컴 디렉토리 하나를 선택 해서 git저장소를 적용하는 방법
2. 다른 어디선가 git저장소를 clone하는 방법

#### 기존 디렉토리를 git저장소로 만들기 
임의 폴더를 만든다 **my_project**로 한다, 이 프로젝트 폴더에서 
> git init

이 명력은 .git이라는 하위 디렉토리를 만든다. .git에는 필요한 Skeleton이 들어 있다. 

git이 파일을 관리하게 하려면 저장소에 파일을 추가하고 커밋해야 한다 git add, git commit   
> git add *.c   
> git add LICENSE   
> git commit -m "initial project version"

위 명령어로 git저장소를 만들고 파일 버전 관리를 시작 한다

### 기존 저장소를 clone하기
git clone <url>명령어로 저장소 clone한다
> git clone https://githum..;..../.../ff   
> git clone https://githum..;..../.../ff   mylib...

### stageing 
> git add file or fold

### unstaging 
> git reset file

### 파일 상태 확인 
> git status   
> git status -s   
> git status--short 

### 파일 무시하기
파일 관리가 필요 없는 것은 ".gitignore"에 
규칙은 다음과 같다.
- 아무것도 없는 라인이나, '#'으로 시작하는 라인은 무시
- 표준 Glob패턴 사용. 이는 프로젝트 전체에 적용
- 슬래시(/)로 시작하면 하위 디렉텍토리에 적용되지 않는다.
- 디랙토리는 슬래시(/)를 끝에 사용하는 것으로 표현 한다
- 느낌표(!)로 시작하는 패턴의 파일은 무시 하지 않는다. 
```
# 확장자가 .a인 파일 무시
*.a

# 윗 라인에서 확장자가 .a인 파일을 무시하게 했지만 lib.a는 무시 하지 않음
!lib.a

# 현재 디렉토리에 있는 todo파일은 무시하고 subdir/todo처럼 하위디렉토리는 무시하지 않음
/todl

# build/ 디렉토리 있느 ㄴ모든 파일 무시
build/

# doc/notes.txt 은 무시, doc/server/arch.txt 무시하지 않음
doc/*txt

# doc디렉토리 아래의 모든 .pdf 파일 무시
doc/**/*.pdf
```

### staged와 unstaged상태의 변경 내용보기
> git status ==> 단순 파일 변경

> git diff   
> git diff --staged ==> staging area에 넣은 파일 비교

변경된 자세한 내용.. Stage한 후 다시 수정 해도 git diff를 사용할 수 있다. 이때는 staged상태인것과 unstaged상태인 것을 비교한다
staged된 파일은 git diff --ceched옵셔능로 확인. --staged, --ceched는 같은 옵션이다.

### 변경사항 커밋
커밋은 staged된 파일에만 적용됨. unstaged는 커밋안됨
커밋 하기전에 git status로 확인 후 
> git commit

