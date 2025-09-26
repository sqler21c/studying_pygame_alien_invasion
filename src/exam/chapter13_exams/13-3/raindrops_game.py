import sys

import pygame
from settings import Settings
from raindrop import Raindrop

class RaindropGame:

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Raindrop Game")
        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        while True:
            self._check_events()
            self.raindrops.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_drops(self):
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height

        while current_y < (self.settings.screen_height - 2 * drop_height):
            while current_x < (self.settings.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width

            current_x = drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        new_drop = Raindrop(self)
        new_drop.y = y_position

        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.raindrops.add(new_drop)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    rd_game = RaindropGame()
    rd_game.run_game()
