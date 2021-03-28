import pygame
pygame.init()

# creates the window
WIDTH, HEIGHT = 900, 775
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TIC-TAC-TOE")


# color parameters
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)

font = pygame.font.Font('freesansbold.ttf', 48)

# keeping track of the player's score
x_score = 0
o_score = 0



def bg_color():
    WIN.fill(SILVER)


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


def hud():
    x_text = font.render("X's WINS: " + str(x_score), True, BLACK)
    y_text = font.render("O's WINS: " + str(o_score), True, BLACK)
    WIN.blit(x_text, (10, 15))
    WIN.blit(y_text, (600, 15))


def display_turn(turn_counter):
    if turn_counter == 1:
        pygame.draw.rect(WIN, SILVER, [350, 15, 200, 50])
        text = font.render("X's Turn", True, BLACK)
        WIN.blit(text, (350, 15))

    else:
        pygame.draw.rect(WIN, SILVER, [350, 15, 200, 50])
        text = font.render("O's Turn", True, BLACK)
        WIN.blit(text, (350, 15))


def clear_board():
    # overwrite the board with a new background n grid
    bg_color()
    grid()
    # display the hud after overwriting the board
    hud()



def display_draw():
    pass