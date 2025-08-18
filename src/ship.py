import pygame

class Ship:
    """우주선 관리 클래스"""
    
    def __init__(self, ai_game):
        """우주선 초기화 하고 시작 위치 설정"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # 우주선 이미지를 불러오고 사각형을 가져 온다
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        
        # 우주선의 초기 위치는 화면 하단 중앙
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """우주선을 현재 위치에 그림"""
        self.screen.blit(self.image, self.rect)