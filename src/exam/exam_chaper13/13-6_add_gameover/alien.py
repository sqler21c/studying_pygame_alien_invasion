from random import randint
import pygame
from pygame.sprite import Sprite
from current_path import current_path as curpath


class Alien(Sprite):
    """_summary_

    Args:
        Sprite (_type_): _description_
    """
    """ A class to represent a single alien in the fleet. 
    """
    def __init__(self, ss_game):

        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        
        image_path = curpath("images", "alien_ship.png")
        self.image = pygame.image.load(image_path)
        # self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right

        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)
        self.x = float(self.rect.x)

    def update(self):
        """ Move the alien to the left. """
        self.x -= self.settings.alien_speed
        self.rect.x = self.x