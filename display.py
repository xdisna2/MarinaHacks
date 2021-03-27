import pygame
pygame.init()
WIDTH, HEIGHT = 900, 775
# creates the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)


def bg_color():
    WIN.fill(SILVER)


# method that creates the grid
def grid():

    # [x-pos, y-pos, width, height]
    # creates the top horizontal bar
    pygame.draw.rect(WIN, BLACK, [300, 75, WIDTH / 64, HEIGHT])

    # creates the vertical bars
    pygame.draw.rect(WIN, BLACK, [600, 75, WIDTH / 64, HEIGHT])
    pygame.draw.rect(WIN, BLACK, [0, 75, WIDTH, HEIGHT / 64])

    # creates the horizontal bars
    pygame.draw.rect(WIN, BLACK, [0, 315, WIDTH, HEIGHT / 64])
    pygame.draw.rect(WIN, BLACK, [0, 550, WIDTH, HEIGHT / 64])


# leave on the side for a while
def buttons():
    WHITE = (255, 255, 255)
    pygame.draw.rect(WIN, WHITE, [WIDTH/2, HEIGHT/2, 140, 40])


def hud():
    font = pygame.font.Font('freesansbold.ttf', 48)
    x_text = font.render("X's WINS: ", True, BLACK)
    y_text = font.render("O's WINS: ", True, BLACK)
    WIN.blit(x_text, (10, 15))
    WIN.blit(y_text, (600, 15))
