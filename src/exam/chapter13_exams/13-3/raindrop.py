import os

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """ 빗방울 하나    """

    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        print("=================================================")
        # print(os.path.abspath(__file__))
        print(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "raindrop.png")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # 시작 위치 설정
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 빗방울의 실수 위치 저장
        self.y = float(self.rect.y)


    def update(self):
        """ 빗방울 위치 업데이트 """
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
