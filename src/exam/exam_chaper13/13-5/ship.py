import os
import pygame
from current_path import current_path as curpath


class Ship:
    """ A class to manage the ship. """
    def __init__(self, ss_game):
        """ Initaialize the ship and set its starting position. """
        self.screen = ss_game.screen
        self.setting = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # # Load the ship image and get its rect.
        # print("====this is file execuiting folder=========")
        # # print(os.path.abspath(__file__))
        # print(os.path.dirname(os.path.abspath(__file__)))
        # print("===========================================")
        image_path = curpath("images", "rocket_small.png")
                
        self.image = pygame.image.load(image_path)
        # self.image = pygame.image.load('images/rocket_small.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the left center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)
        
        # Movement Flag
        self.moving_up = False
        self.moving_down = False

    
    def update(self):
        """ update the ship's position based on movement flag. """
        
        # update the ship's y value, not the rect
        
        if self.moving_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)