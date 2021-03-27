import pygame
WIDTH, HEIGHT = 900, 800
# creates the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
SILVER = (192, 192, 192)


def bg_color():
    WIN.fill(SILVER)
    pygame.display.update()

