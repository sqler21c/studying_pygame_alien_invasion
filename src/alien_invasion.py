import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""
    
    def __init__(self):
        """ Initialize game and make game's resource """
        pygame.init() # pygame 초기화
        self.clock = pygame.time.Clock() # 게임 속도 조절을 위한 시계 객체 생성
        
        # self.screen = pygame.display.set_mode((1200, 800))을 
        # Settings 사용하여  클래스 인스턴스 생성
        self.settings = Settings()
        
        # 전체화면으로 실행
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # self.screen = pygame.display.set_mode((self.settings.screen_width, 
        #                                        self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion") # 게임 제목 설정
        
        self.ship = Ship(self)  # 우주선 인스턴스 생성
        self.bullets = pygame.sprite.Group()  # 탄환 그룹 생성
        
        # self.bg_color = (230, 230, 230)  # 밝은 회색
        # 배경색 설정
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events() # helper method 추가
            ###########################################
            # helper method로 이동 def _check_events()
            # """ keyboard and mouse event 처리 """
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            ###########################################
            self.ship.update()
            # self.bullets.update()  # Update bullets
            self._update_screen() # 화면 업데이트
            
            # 사라진 탄환 제거 
            self._update_bullets()
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         self.bullets.remove(bullet)
            #     print(len(self.bullets))
            
            #################################################
            # helper method로 이동 def _update_screen()
            # # 루프를 반복할때마다 화면을 다시 그립니다. 
            # # self.screen.fill(self.bg_color)를 아래와 같이 settings 클래스 사용
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme() # 우주선 그리기                
            # # 가장 최근 그린 화면을 표시
            # pygame.display.flip() # 화면 업데이트
            #################################################
            self.clock.tick(60) # frame 속도
            
    def _check_events(self):
        """ keyboard and mouse event 처리 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = False
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False
            
    def _update_bullets(self):
        """ 탄환 위치를 업데이트하고 사라진 탄환을 제거"""
        self.bullets.update()
        
        # 사라진 탄환 제거
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """ 화면 업데이트 """
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        
        pygame.display.flip()
        
    def _check_keydown_events(self, event):
        """ Key를 누를때 응답 처리 """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        """키에서 땔때 응답 처리"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """새 탄환을 만들어 탄환 그룹에 추가 합니다"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)    

if __name__ == '__main__':
    # make intance of AlienInvasion
    ai = AlienInvasion()
    ai.run_game()