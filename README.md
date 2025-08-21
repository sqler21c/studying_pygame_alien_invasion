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


## Date 2025.08.18
### alien_invasion.py
1. frame 속도 제어
   > self.clock = pygame.time.Clock()
   > self.clock.tick)(60)
2. 배경색 설정
   > 배경색 설정
   > self.bg_clolor = (230, 230, 230)
   > 루프 반복때마다 화면을 다시 그림
   > self.screen.fill(self.bg_color)

### settings.py 추가
1. alien_invasion.py에서 인스턴스를 만들어 설정에 접근 함

### images 폴더를 만들고 ship.bmp 추가
1. ship 클래스 만들기


## Date 2025.08.20
### 화면에 우주선 그리기 in alien_invasion.py
1. import
   ```python
   from ship import Ship
   ```
2. in __init__
   ```python
   self.ship = Ship(self)
   ```
3. run_game
   ```python
   self.ship.blitme()
   ```

### 리팩터링 : _check_events(), _update_screen() method
## run_game()를 보조 메서드 두개로  나눔
> 보조 메서드(helper method)란 클래스 내부에서 사용하며 클래서 외부에서는사용하지 않는 메서드
> 파이썬에서는 보조 메서드임을 나타내기 위해 맨 앞에 언더바 하나를 붙인다.

1. _check_events()
   ```python
    self._check_events()

    def _check_events)(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
    ```
2. _update_screen()
   ```python
   self._update.screen()

   def _update_screen():
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()

      pygame.display.flip()
   ```
### 우주선 조종하기
1. 키 입력에 응답하기
   1. 파이게임이 KEYDOWN이벤트를 감지 할때마다 우리가 원하는 키인지 확인
   2. 가령 오른쪽 화살표를 누르면 우주선의 rect.x값을 증가시켜 우주선을 오른쪽으로 이동
   3. 왼쪽이동은 rect.x값을 감소 시켜 왼쪽으로 이동함
2. 우주선 속도 조정
   1. Settings 클래스에 ship_speed속청 추가해서 속도 조절
3. 우주선 이동범위 정하기
   1. ship의 update()메소드 수정
4. _check_events() 리펙토링
   1. KEYDOWN이벤트 처리, KEYUP이벤트 처리 메서드 두개 분리
5. 전체 화면 모드 PALY추가 in alien_invasion.py