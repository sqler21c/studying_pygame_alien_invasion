import sys
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # 게임 통계 인스턴스 생성
        self.stats = GameStats(self)

        
        self.ship = Ship(self)  # 우주선 인스턴스 생성
        self.bullets = pygame.sprite.Group()  # 탄환 그룹 생성
        self.aliens = pygame.sprite.Group()   # 외계인 그룹 생성

        self._create_fleet()  # 외계인 무리 생성
        
        # self.bg_color = (230, 230, 230)  # 밝은 회색
        # 배경색 설정
        self.bg_color = self.settings.bg_color

        # 게임을 활성 상태로 시작
        self.game_active = True

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
            if self.game_active:
                self.ship.update() # 우주선 위치 업데이트
                self._update_bullets() # 탄환 위치 업데이트
                self._update_aliens() # 외계인 위치 업데이트
                
            # self.ship.update()
            # self.bullets.update()  # Update bullets
            self._update_screen() # 화면 업데이트
            
            # 사라진 탄환 제거 
            # self._update_bullets()
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         self.bullets.remove(bullet)
            #     print(len(self.bullets))
            # self._update_aliens()

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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """탄환과 외계인의 충돌을 처리"""
        # 외계인을 맞힌 탄환이 있는지 확인
        # 맞힌 탄환이 있으면 외계인 제거
        collisions = pygame.sprite.groupcollide(self.bullets, 
                                                self.aliens, 
                                                True, 
                                                True)
        if not self.aliens:
            # 남아 있는 탄환을 제거하고 함대를 새로 만듦
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """함대에 속한 외계인의 위치를 모두 업데이트 함"""
        """_summary_
        함대가 경계에 도달했는지 확인 하고 위치 업데이트
        """
        self._check_fleet_edges()
        self.aliens.update()

        # 우주선과 외계인 충돌 확인
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("ship hit!!!")
            self._ship_hit()

        # 화면 아래에 도달한 외계인 확인
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """ 외계인이 화면 아래에 도달했는지 확인"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 우주선이 외계인과 충돌한 것과 같은 처리
                self._ship_hit()
                break


    def _ship_hit(self):
        """우주선이 외계인과 충돌했을 때 처리"""
        if self.stats.ships_left > 0:
                
            # ships_left에서 1 감소
            self.stats.ships_left -= 1

            # 남아 있는 탄환과 외계인을 모두 제거
            self.aliens.empty()
            self.bullets.empty()

            # 새로운 함대를 만들고 우주선을 화면 중앙에 배치
            self._create_fleet()
            self.ship.center_ship()

            # 잠시 대기
            sleep(0.5)
        else:
            self.game_active = False

    def _create_fleet(self):
        """ 외계인 함대를 만듦"""
        # 외계인 하나를 만들어서 그 너비와 높이를 구함 공간이 없을때까지 계속 추가
        # 외계인 사이의 공간으 ㄴ외계인의 너비와 높이와 같음
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size #1

        current_x, current_y = alien_width, alien_height #2
                # current_x = alien_width
        while current_y < (self.settings.screen_height - 3 * alien_height):#3
            while current_x <(self.settings.screen_width -2 * alien_width):
                # new_alien = Alien(self)
                # new_alien.x = current_x
                # new_alien.rect.x = new_alien.x
                # self.aliens.add(new_alien)
                # self._create_alien(current_x)
                self._create_alien(current_x, current_y) #4
                current_x += 2 * alien_width
            
                # self.aliens.add(alien)
            
            #한줄이 끝났으니 x값은 초기화 y값은 늘린다.
            current_x = alien_width #5
            current_y += 2 * alien_height #5

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """함대가 화면의 가장자리에 도달했는지 확인"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ 함대 전체를 한 줄 내리고 좌우 방향 변경"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """ 화면 업데이트 """
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        self.aliens.draw(self.screen) # 외계인 그리기
        
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