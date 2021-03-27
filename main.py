import pygame
import display

pygame.init()
display.bg_color()
display.grid()
display.clear_rectangle()


# 0 = O's turn | 1 = X's turn
def main():
    # game loop, terminates when the game ends
    run = True
    player_state = 0
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
        display.display_turn(player_state)
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
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(75, 130)
                        player_state = 1
                        box1 = True

                    else:
                        display.display_x(75, 130)
                        player_state = 0
                        box1 = True

            # Box 2
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 314 < mouse[0] < 597 and 87 < mouse[1] < 310 and box2 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(380, 130)
                        player_state = 1
                        box2 = True

                    else:
                        display.display_x(380, 130)
                        player_state = 0
                        box2 = True

            # Box 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 614 < mouse[0] < 898 and 87 < mouse[1] < 310 and box3 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(675, 130)
                        player_state = 1
                        box3 = True

                    else:
                        display.display_x(675, 130)
                        player_state = 0
                        box3 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 298 and 327 < mouse[1] < 549 and box4 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(75, 370)
                        player_state = 1
                        box4 = True

                    else:
                        display.display_x(75, 370)
                        player_state = 0
                        box4 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 314 < mouse[0] < 597 and 327 < mouse[1] < 549 and box5 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(380, 370)
                        player_state = 1
                        box5 = True

                    else:
                        display.display_x(380, 370)
                        player_state = 0
                        box5 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 614 < mouse[0] < 898 and 327 < mouse[1] < 549 and box6 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(675, 370)
                        player_state = 1
                        box6 = True

                    else:
                        display.display_x(675, 370)
                        player_state = 0
                        box6 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 298 and 562 < mouse[1] < 775 and box7 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(75, 600)
                        player_state = 1
                        box7 = True

                    else:
                        display.display_x(75, 600)
                        player_state = 0
                        box7 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 314 < mouse[0] < 597 and 562 < mouse[1] < 775 and box8 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(380, 600)
                        player_state = 1
                        box8 = True

                    else:
                        display.display_x(380, 600)
                        player_state = 0
                        box8 = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 614 < mouse[0] < 898 and 562 < mouse[1] < 775 and box9 is False:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(675, 600)
                        player_state = 1
                        box9 = True

                    else:
                        display.display_x(675, 600)
                        player_state = 0
                        box9 = True

        display.hud()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
