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
        # self.rect.right = ai_game.ship.rect.centerx
        self.rect.midleft = ai_game.ship.rect.midleft
        # 탄환 위치를 부동 소수점 숫자로 저장
        self.x = float(self.rect.x)

    def update(self):
        """탄환을 왼쪽에서 오른쪽으로 이동"""
        self.x += self.settings.bullet_speed
        self.rect.x = float(self.x)

    def draw_bullet(self):
        """화면에 탄환을 그리기"""
        pygame.draw.rect(self.screen, self.color, self.rect)
