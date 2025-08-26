import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """함 대에 외계인 하나를 나타내는 클래스"""
    def __init__(self, ai_game):
        """ 외계인 추기화하고 시작 위치 설정"""
        super().__init__()
        self.screen = ai_game.screen

        # 외계인 이미지 불러움    