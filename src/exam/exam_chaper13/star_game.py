import sys
from random import randint

import pygame

from settings import Settings
from star import Star


class StarGame:
    """star game 관리 클래스
    """

    def __init__(self):
        """
        게임 초기화 및 자원 생성
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Star Game")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """
        게임 시작 및 메인 루프
        """
        while True:
            """ 이벤트 처리 및 화면 업데이트
            """
            self._create_events()
            self._update_screen()
            self.clock.tick(60)

    def _create_events(self):
        """ 키보드 및 마우스 이벤트 처리
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """키보드 눌림 이벤트 처리

        Args:
            event (pygame.event.Event): 발생한 이벤트
        """
        if event.key == pygame.K_q:
            sys.exit()


    def _create_stars(self):
        """별 생성

        Args:
            self (StarGame): 현재 게임 인스턴스
        """
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = 2 * star_width, 2 * star_height
        
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width -2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            current_x = 2 * star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """별 생성 및 그룹에 추가

        Args:
            x_position (int): 별의 x 좌표
            y_position (int): 별의 y 좌표
        """
        new_star = Star(self)
        new_star.rect.x = x_position + self._get_star_offset()
        new_star.rect.y = y_position + self._get_star_offset()

        self.stars.add(new_star)
    
    def _get_star_offset(self):
        offset_size = 15
        return randint(-1 * offset_size, offset_size)
    

    def _update_screen(self):
        """화면 업데이트

        Args:
            self (StarGame): 현재 게임 인스턴스
        """
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == "__main__":
    sg = StarGame()
    sg.run_game()