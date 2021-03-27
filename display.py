import pygame
WIDTH, HEIGHT = 900, 775
# creates the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
SILVER = (192, 192, 192)

x_image = pygame.image.load('x_image_transparent.png')
o_image = pygame.image.load('o_image_transparent.png')


def bg_color():
    WIN.fill(SILVER)


def display_x():
    WIN.blit(x_image, (75, 130))


def display_o():
    WIN.blit(o_image, (380, 130))


# method that creates the grid
def grid():
    BLACK = (0, 0, 0)
    # [x-pos, y-pos, width, height]
    # creates the top horizontal bar
    pygame.draw.rect(WIN, BLACK, [0, 75, WIDTH, HEIGHT / 64])

    # creates the vertical bars
    pygame.draw.rect(WIN, BLACK, [600, 75, WIDTH / 64, HEIGHT])
    pygame.draw.rect(WIN, BLACK, [300, 75, WIDTH / 64, HEIGHT])

    # creates the horizontal bars
    pygame.draw.rect(WIN, BLACK, [0, 315, WIDTH, HEIGHT / 64])
    pygame.draw.rect(WIN, BLACK, [0, 550, WIDTH, HEIGHT / 64])


# leave on the side for a while
def buttons():
    WHITE = (255, 255, 255)
    pygame.draw.rect(WIN, WHITE, [WIDTH/2, HEIGHT/2, 140, 40])


def clear_rectangle():
    # (1, 1)
    pygame.draw.rect(WIN, SILVER, [0, 87, 300, 227])
    # (2, 1)
    pygame.draw.rect(WIN, SILVER, [0, 327, 300, 222])
    # (3, 1)
    pygame.draw.rect(WIN, SILVER, [0, 562, 300, 222])
    # (1, 2)
    pygame.draw.rect(WIN, SILVER, [314, 87, 285, 227])
    # (2, 2)
    pygame.draw.rect(WIN, SILVER, [314, 327, 285, 222])
    # (3, 2)
    pygame.draw.rect(WIN, SILVER, [314, 562, 285, 227])
    # (1, 3)
    pygame.draw.rect(WIN, SILVER, [614, 87, 285, 227])
    # (2, 3)
    pygame.draw.rect(WIN, SILVER, [614, 327, 285, 222])
    # (3, 3)
    pygame.draw.rect(WIN, SILVER, [614, 562, 285, 227])