# This is studying note.. 
### 1. python module : using pygame
1. virtual env : python -m venv [virtual env]
2. install 
   1. python -m pip install --user(if global install) pygame


## Date 2025. 08.14
-. make github repo
-. make local repo
-. connect from local repo to remote reop

```
$ git init
$ git status
$ git add . 
$ git commit -m "commit message"
$ git remote add origin ***(copied 주소)
$ git remote -v
$ git push origin master
```

## Date 2025.08.16

### pip로 pytest설치 하기

pip upgrade : ``` python -m pip install --upgrade pip ```

1. pytest install
   > python -m pip install --user pytest


### Module Import 관련 
1. 실행파일 1단계 상위 폴더 구하는 코드
``` os.path.dirname(os.path.abspath(os.path.dirname(__file__))) ```
2. 2단계 상위 폴더
``` os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))) ```
import sys, os는 해야 함