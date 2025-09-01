import sys, os

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """별을 나타내는 클래스

    Args:
        Sprite (pygame.sprite.Sprite): Pygame의 스프라이트 클래스  
    """

    def __init__(self, stars_game):
        """별 객체 초기화

        Args:
            stars_game (StarGame): 현재 게임 인스턴스
        """
        super().__init__()
        self.screen = stars_game.screen
        
        # 별 이미지 로드
        
        print("=================================================")
        # print(os.path.abspath(__file__))
        print(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "star.png")

        # rint(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
        # self.image = pygame.image.load("src/exam/exam_chapter13/images/star.png")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


