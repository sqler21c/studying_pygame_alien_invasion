import pygame

class Ship:
    """우주선 관리 클래스"""
    
    def __init__(self, ai_game):
        """우주선 초기화 하고 시작 위치 설정"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings    
        self.screen_rect = ai_game.screen.get_rect()
        
        # 우주선 이미지를 불러오고 사각형을 가져 온다
        self.image = pygame.image.load('src/exam/images/ship.bmp') 
        self.image = pygame.transform.rotate(self.image, -90) # image 오른쪽으로 90도 회전
        self.rect = self.image.get_rect()
        
        # 우주선의 초기 위치는 화면 하단 중앙
        # self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.center = self.screen_rect.center  # 화면 중앙으로 위치 조정
        # 우주선의 초기 위치 화면 왼쪽 중앙에 위치
        self.rect.left = self.screen_rect.left
        # self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치 업데이트 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            
        # x, y 좌표를 통해 rect객체를 업데이트 합니다.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """우주선을 현재 위치에 그림"""
        self.screen.blit(self.image, self.rect)