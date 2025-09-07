import pygame.font

class Button:

    """A class to create a button for the game.
    Attributes:
        screen: The surface on which the button will be drawn.
        screen_rect: The rectangular area of the screen.
        width: The width of the button.
        height: The height of the button.
        button_color: The background color of the button.
        text_color: The color of the text on the button.
        font: The font used for the button text.
        rect: The rectangular area of the button.
        msg_image: The rendered image of the button text.
        msg_image_rect: The rectangular area of the button text image.
    """

    def __init__(self, ai_game, msg):
        """ Initialize button attributes. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # set the button's dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0) 
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 버튼의 rect객체를 만들고 중앙에 배치
        self.rect = pygame.Rect(0, 
                                0, 
                                self.width, 
                                self.height)
        self.rect.center = self.screen_rect.center

        # 버턴에 표시할 메시지
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Prepare the message for the button.

        Args:
            msg (str): The message to be displayed on the button.
        """
        self.msg_image = self.font.render(msg, 
                                          True, 
                                          self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw the button on the screen.
        This method fills the button's rectangle with the button color
        and draws the button text.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)