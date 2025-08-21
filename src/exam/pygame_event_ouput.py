import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Pygame Event Output")
myFont = pygame.font.SysFont(None, 48)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            text = f"Key Down: {pygame.key.name(event.key)}"
            surface = myFont.render(text, True, (0, 0, 0))
            screen.fill((255, 255, 255))
            screen.blit(surface, (50, 50))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            text = f"Mouse Button Down: {event.button} at {event.pos}"
            surface = myFont.render(text, True, (0, 0, 0))
            screen.fill((255, 255, 255))
            screen.blit(surface, (50, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()