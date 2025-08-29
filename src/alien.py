import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """함 대에 외계인 하나를 나타내는 클래스"""
    def __init__(self, ai_game):
        """ 외계인 추기화하고 시작 위치 설정"""
        super().__init__()
        self.screen = ai_game.screen

        # 외계인 이미지 불러와  rect 속성 설정
        self.image = pygame.image.loade('src/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 외계인은 좌면 좌측 상단 근처에 만듦
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 외계인의 정확한 가로 위치 저장
        self.x = float(self.rect.x)
        