import pygame
pygame.init()

# creates the window
WIDTH, HEIGHT = 900, 775
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TIC-TAC-TOE")

x_image = pygame.image.load('x_image.png')
o_image = pygame.image.load('o_image.png')

# color parameters
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)

font = pygame.font.Font('freesansbold.ttf', 48)

# keeping track of the player's score
x_score = 0
o_score = 0


def bg_color():
    WIN.fill(SILVER)


def display_x():
    WIN.blit(x_image, (75, 130))


def display_o():
    WIN.blit(o_image, (380, 130))


# method that creates the grid
def grid():

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


def hud():
    x_text = font.render("X's WINS: " + str(x_score), True, BLACK)
    y_text = font.render("O's WINS: " + str(o_score), True, BLACK)
    WIN.blit(x_text, (10, 15))
    WIN.blit(y_text, (600, 15))


def display_turn(player_state):
    if player_state == 1:
        text = font.render("X's Turn", True, BLACK)
        WIN.blit(text, (350, 15))

    else:
        text = font.render("O's Turn", True, BLACK)
        WIN.blit(text, (350, 15))
