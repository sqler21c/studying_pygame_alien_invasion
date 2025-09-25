import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """우주선 관리 클래스"""
    
    def __init__(self, ai_game):
        """우주선 초기화 하고 시작 위치 설정"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings # 
        self.screen_rect = ai_game.screen.get_rect()
        
        # 우주선 이미지를 불러오고 사각형을 가져 온다
        self.image = pygame.image.load('src/images/ship.bmp') 
        self.rect = self.image.get_rect()
        
        # 우주선의 초기 위치는 화면 하단 중앙
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 우주선의 정확한 가로 위치 설정을 위해 부동소숫점 저장
        self.x = float(self.rect.x)
        
        # 우주선 움직임 플래그는 정리 상태로 시작
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치 업데이트 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            
            # self.rect.x += 1  # 우주선 오른쪽으로 이동
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            # self.rect.x -= 1 # 우주선 왼쪽으로 이동
            self.x -= self.settings.ship_speed
            
        # self.x를 통해 rect객체를 업데이트 합니다.
        self.rect.x = self.x
        
    def blitme(self):
        """우주선을 현재 위치에 그림"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """우주선을 화면 중앙 하단에 위치"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)