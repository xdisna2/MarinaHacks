import pygame
import display
import back_end
import numpy as np

import sys
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


asset_url_x = resource_path('assets/x_image_transparent.png')
asset_url_o = resource_path('assets/o_image_transparent.png')

x_image = pygame.image.load(asset_url_x)
o_image = pygame.image.load(asset_url_o)

pygame.init()
display.bg_color()
display.grid()
display.clear_rectangle()


def display_o(x, y):
    display.WIN.blit(o_image, (x, y))


def display_x(x, y):
    display.WIN.blit(x_image, (x, y))


# 0 = O's turn | 1 = X's turn
def main():
    # game loop, terminates when the game ends
    run = True
    turn_counter = 0
    box1 = False
    box2 = False
    box3 = False
    box4 = False
    box5 = False
    box6 = False
    box7 = False
    box8 = False
    box9 = False

    while run:
        display.display_turn(turn_counter % 2)
        # print(mouse)
        # gets a list of all the events and loops through them
        for event in pygame.event.get():

            # if the user exits the window, terminate the game
            if event.type == pygame.QUIT:
                run = False

            # Box 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 300 and 87 < mouse[1] < 310 and box1 is False:
                    if turn_counter % 2 == 0:
                        back_end.playerInput(turn_counter % 2, 0, 0)
                        display_o(75, 130)
                        box1 = True
                        turn_counter += 1
                    else:
                        back_end.playerInput(turn_counter % 2, 0, 0)
                        display_x(75, 130)
                        box1 = True
                        turn_counter += 1

                elif 314 < mouse[0] < 597 and 87 < mouse[1] < 310 and box2 is False:
                    if turn_counter % 2 == 0:
                        back_end.playerInput(turn_counter % 2, 0, 1)
                        display_o(380, 130)
                        box2 = True
                        turn_counter += 1

                    else:
                        back_end.playerInput(turn_counter % 2, 0, 1)
                        display_x(380, 130)
                        box2 = True
                        turn_counter += 1

                elif 614 < mouse[0] < 898 and 87 < mouse[1] < 310 and box3 is False:
                    if turn_counter % 2 == 0:
                        display_o(675, 130)
                        back_end.playerInput(turn_counter % 2, 0, 2)
                        box3 = True
                        turn_counter += 1

                    else:
                        display_x(675, 130)
                        back_end.playerInput(turn_counter % 2, 0, 2)
                        box3 = True
                        turn_counter += 1

                elif 0 < mouse[0] < 298 and 327 < mouse[1] < 549 and box4 is False:
                    if turn_counter % 2 == 0:
                        display_o(75, 370)
                        back_end.playerInput(turn_counter % 2, 1, 0)
                        box4 = True
                        turn_counter += 1

                    else:
                        display_x(75, 370)
                        back_end.playerInput(turn_counter % 2, 1, 0)
                        box4 = True
                        turn_counter += 1

                elif 314 < mouse[0] < 597 and 327 < mouse[1] < 549 and box5 is False:
                    if turn_counter % 2 == 0:
                        display_o(380, 370)
                        back_end.playerInput(turn_counter % 2, 1, 1)
                        box5 = True
                        turn_counter += 1

                    else:
                        display_x(380, 370)
                        back_end.playerInput(turn_counter % 2, 1, 1)
                        box5 = True
                        turn_counter += 1

                elif 614 < mouse[0] < 898 and 327 < mouse[1] < 549 and box6 is False:
                    if turn_counter % 2 == 0:
                        display_o(675, 370)
                        back_end.playerInput(turn_counter % 2, 1, 2)
                        box6 = True
                        turn_counter += 1

                    else:
                        display_x(675, 370)
                        back_end.playerInput(turn_counter % 2, 1, 2)
                        box6 = True
                        turn_counter += 1

                elif 0 < mouse[0] < 298 and 562 < mouse[1] < 775 and box7 is False:
                    if turn_counter % 2 == 0:
                        display_o(75, 600)
                        back_end.playerInput(turn_counter % 2, 2, 0)
                        box7 = True
                        turn_counter += 1

                    else:
                        display_x(75, 600)
                        back_end.playerInput(turn_counter % 2, 2, 0)
                        box7 = True
                        turn_counter += 1

                elif 314 < mouse[0] < 597 and 562 < mouse[1] < 775 and box8 is False:
                    if turn_counter % 2 == 0:
                        display_o(380, 600)
                        back_end.playerInput(turn_counter % 2, 2, 1)
                        box8 = True
                        turn_counter += 1

                    else:
                        display_x(380, 600)
                        back_end.playerInput(turn_counter % 2, 2, 1)
                        box8 = True
                        turn_counter += 1

                elif 614 < mouse[0] < 898 and 562 < mouse[1] < 775 and box9 is False:
                    if turn_counter % 2 == 0:
                        display_o(675, 600)
                        back_end.playerInput(turn_counter % 2, 2, 2)
                        box9 = True
                        turn_counter += 1

                    else:
                        display_x(675, 600)
                        back_end.playerInput(turn_counter % 2, 2, 2)
                        box9 = True
                        turn_counter += 1

        # if turn_counter >= 5:
        # Tie at the last round
        if (turn_counter == 9) and (back_end.checkWinCondition() is False):
            print("Y'all suck, how the heck did no one win?")

            box1 = False
            box2 = False
            box3 = False
            box4 = False
            box5 = False
            box6 = False
            box7 = False
            box8 = False
            box9 = False
            turn_counter = 0
            matrix = [[None, None, None], [None, None, None], [None, None, None]]
            back_end.mat1 = np.array(matrix)
            display.clear_board()

            # Legit win
        elif back_end.checkWinCondition():
            if turn_counter % 2 == 0:
                print("Player 0 wins")
                display.x_score += 1

            else:
                print("Player 1 wins")
                display.o_score += 1

            box1 = False
            box2 = False
            box3 = False
            box4 = False
            box5 = False
            box6 = False
            box7 = False
            box8 = False
            box9 = False
            turn_counter = 0
            matrix = [[None, None, None], [None, None, None], [None, None, None]]
            back_end.mat1 = np.array(matrix)
            display.clear_board()

        display.hud()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
