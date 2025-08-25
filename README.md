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

## Date 2025.08.21
### Page 341 연습문제
1. 파이게임 문서
   1. [pygame](https://pygame.org)
   2. [pygame doucment](https://pygame.org/docs)
2. 로켓
   1. 화면 중앙에 로켓이 있는 게임을 만드세요. 플레이어는 화살표 키를 써서 상하좌우 이동 시키고 화면 가장자리 벗어 나면 안됨


## Date  2025.08.22
### markdown 내부 인덱스 시험
   . [여기](#1-python-module--using-pygame) 
### Page340 탄환을 쏘기 전 빠른 준비
그 동안의 파일 정리
1. alien_invasion.py
   
    메인 파일인 alien_invasion.py에는 AlienInvasion 클래스가 있습니다.
   이 클래스에는 게임 전체에서 사용되는 다양한 중요 속성이 있습니다. 설정은 settings에 디스펭에이 서피스는 screen에 할당되고 ship인스턴스 역시 이 파일에서 만듭니다. 게임의 메인 루프인 while 루프도 이 모듈에 속합니다. 
   while루프는 _check_events(), ship.update(), _update_screen()을 호출하며 반볼될 때마다 시계를 움직입니다
   _check_events() 메서드는 키입력과 해제 같은 이벤트 담당

2. setting.py
   
   setting.py에는 Settings클래스가 있습니다. 이클래스에서는 게임의 모양, 우주선 속도 관련 속성을 초기화하는 __init__()a메서드만 있습니다. 

3. ship.py
   
   ship.py에는 Sip클래스가 있습니다. Ship클래스에는 __init__()메서드 우주선 위치를 결정하는 update() 메서드, 우주선을 화면에 그리는 blitme()메서드가 있습니다. 
   우주선 이미지는 images폴더의 ship.bmp입니다.

### 탄환 발사하기
플레이어가 "Space"를 누르면 탄환(작은 사각형)이 발사되고 탄한은 화면 위 쪽을 향해 직진하며 화면을 벗어나면 사라짐  **page 342**

1. 탄환설정추가하기
   
   setting.py의 __init__() 마지막에 Bullet클래스에 필요한 값이 들어가도록 setting.py를 업데이트 합니다.
   ```python
   def __init__(self):
      -- 생략 --
      #탄환 설정
      self.bullet_speed = 2.0
      self.bullet_width = 3
      self.bullet_height = 15
      self.bullet_color = (60, 60, 60)
   
   ```

2. Make Bullet class
   
   Bullet클래슬ㄹ 저장할 bullet.py파일을 만듦.
   ```python
   import pygame
   from pygame.sprite import Sprite

   class Bullet(Sprite):
    """ 우주선이 발사하는 탄환을 관리는 클래스 """
    
    def __init__(self, ai_game):
        """ 우주선의 현재 위치에서 탄환 개체를 만듦"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # (0, 0)탄환 사각형을 만들고 위치를 설정
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height) # 1
        self.rect.midtop = ai_game.ship.rect.midtop #2
        
        # 탄환 위치를 부동 소수점 숫자로 저장
        self.y = float(self.rect.y)  #3

   ```
   Sprite를 상속, 스프라이트를 사용하면 게임의 관련 요소를 그룹으로 묶고 그룹의 요소 전체를 한번에 조작할 수 있음
   탄환 인스턴스를 만들기 위해서는 init()이 AlienInvasion의 현재 인스턴스를 받아야 합니다. 또한 Sprite를 상송하기위해서는 super()의 init()을 호출
   화면과 설정 객체, 탄환 색깔에 대한 속성도 초기화

   #1 탄환의 rect속성   
   #2 탄환의 midtop속성을 우주선의 midtop속성으로 맞춤   
   #3 탄환 속도를 세밀히 하기 위해 부동 소숫점 숫자 사용
   ```python
   def update(self):
        """ 탄환이 화면 위 방향으로 이동 """
        # 탄환 위치 업데이트
        self.y -= self.settings.bullet_speed
        # 사각형(rect) 위치 업데이트
        self.rect.y = self.y
   
   def draw_bullet(self):
        """ 화면에 탄환을 그리기 """
        pygame.draw.rect(self.screen, self.color, self.rect)
   ```
3. 탄환을 그룹에 저장하기
   Bullet 클래스를 만들고 필요한 설정을 했으니 플레이어가 스페이스바를 누를때마다 탄환을 발사하는 코드 만들기. 이미 발사한 탄환을 묶어서 관리할 수 있도록 AienInvasion에 그룹을 만듦. 이 그룹은 pygame.Sprite.Group클래스의 인스턴스 이다.

   ```python
   # alien_invasion.py
   from bullet import Bullet

   # __init__()에서는 탄환 그룹을 만든다.
   def __init__(self):
      --생략--
      self.ship = Ship(self)
      self.bullets = pygame.sprite.Group()

   # while 루프를 반복할때마다 탄환위치 업데이트

   def run_game(self):
      -- 생략 --
      self.ship.update()
      self.bullets.update() # 여기 추가
   ```

4. 탄환 발사하기
   ```python
   # alien_invasion.py

   def _check_keydown_events(self, event):
        """ Key를 누를때 응답 처리 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:  # 추가
            self._fire_bullet()

   def _update_screen(self):
        """ 화면 업데이트 """
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites(): # 추가
            bullet.draw_bullet()
            
        self.ship.blitme()
        
        pygame.display.flip()

   def _fire_bullet(self):
        """새 탄환을 만들어 탄환 그룹에 추가 합니다"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)    
   ```

5. 창을 벗어난 탄환 제거하기
   ```python
   # alien_invasion.py
   def run_game(self):
        """ Start the main loop for the game """
        while True:
          - 생략 --
            
            # 사라진 탄환 제거 
            for bullet in self.bullets.copy(): #1
                if bullet.rect.bottom <= 0: #2
                    self.bullets.remove(bullet) #3
                print(len(self.bullets)) #4
   ```
   #1 copy()메서드를 사용해 for loop 만듦, 이렇게 하면 루프안에서 원본그룹이 변하지 않음   
   #2 탄환이 화면을 벗어 나는지 확인 , 벗어났다면 bullet에서 제거(#3)   
   #4 현재 게임에 탄환 몇개 있는지 확인 하는 print()

6. 탄환 수 제한 하기
   ```python
   #settings.py

   def __init__(self):
       -- 생략 --
        self.bullet_color = (60, 60, 60) # 탄환 색상
        self.bullets_allowed = 3 # 화면에 존재할 수 있는 탄환 수 ==> 추가
   # alien_inavasion.py

   def _fire_bullet(self):
        """새 탄환을 만들어 탄환 그룹에 추가 합니다"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)    
   ```
 플레이어가 space를 누르면 먼저 bullets이 길이 확인, len(self.bullets)가 3보다 작으면 새탄환을 만든다. 하지만 새개가 이미 발사된 상태이면 space를 눌러도 아무일도 일ㄷ어 나지 않는다. 

 7. _update_bullets()메서드
   AllienInvasion클래스는 가능한 간결하게 유지 하는게 좋음, 단환을 관리하는 코드를 작성하고 체크했으니 이를 별도의 메서드로 분리, 새 메서드 _update_bullets()를 만들고 이를 _update_screen()바로 앞으로 이동 합니다.
   ```python
   # alien_invasion.py
       def _update_bullets(self):
        """ 탄환 위치를 업데이트하고 사라진 탄환을 제거"""
        self.bullets.update()
        
        # 사라진 탄환 제거
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
   ```
   _update_bullets()코드는 run_game에서 가져옮, 

## Date 2025.08.25
### Page 350  연습문제 in exam
우주선을 화면 왼쪽. 배치 플에이어가 상하, 스페이스 누르면 우주선 탄환 발사 이탄환은 화면을 가로질러 왼쪽에서 오른쪽으로 이동 화면에서 사라진 탄환 제거    

1. 우주선을 화면 왼쪽 중앙에 배치
   ```python
   # ship.py
    def __init__(self, ai_game):
      -- 생략 --
        
        # 우주선 이미지를 불러오고 사각형을 가져 온다
        self.image = pygame.image.load('src/exam/images/ship.bmp') 
        self.image = pygame.transform.rotate(self.image, -90) # image 오른쪽으로 90도 회전
        self.rect = self.image.get_rect()
        --생략 --
        # 우주선의 초기 위치 화면 왼쪽 중앙에 위치
        self.rect.left = self.screen_rect.left
        # self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

      --생략--
   ```
2. 상하 키 이동 
   ```python
   #alien_invasion.py

   def _check_keydown_events(self, event):
        # if event.key == pygame.K_RIGHT:
        #     self.ship.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
   ```
   K_right, K_left 주석 처리 상하만 이동 하도록 함

3. 스페이스 누르면 탄환 발사 화면을 가로 질러 사라진 탄환 제거   
   탄환 관리를 위해 bullet.py파일 생성
   ```python

   # setting.py
    def __init__(self):
        -- 생략 --
        
        # 탄환 설정
        self.bullet_speed = 1.0 # 탄환 속도 설정
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

   # bullet.py

   import pygame
   from pygame.sprite import Sprite

   class Bullet(Sprite):
    def __init__(self, ai_game):
        """ 우주선의 현재 위치에서 탄환 개체를 만듦"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # (0, 0)탄환 사각형을 만들고 위치를 설정
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)
        self.rect.right = ai_game.ship.rect.centerx
        
        # 탄환 위치를 부동 소수점 숫자로 저장
        self.x = float(self.rect.x)

    def update(self):
        """탄환을 왼쪽에서 오른쪽으로 이동"""
        self.x += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """화면에 탄환을 그리기"""
        pygame.draw.rect(self.screen, self.color, self.rect)
   ```