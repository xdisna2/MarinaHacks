import pygame
import display


pygame.init()
display.bg_color()
display.grid()


# 0 = O's turn | 1 = X's turn
def main():
    # game loop, terminates when the game ends
    run = True
    player_state = 0


    while run:
        display.display_turn(player_state)
        # print(mouse)
        # gets a list of all the events and loops through them
        for event in pygame.event.get():

            # if the user exits the window, terminate the game
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 0 < mouse[0] < 300 and 87 < mouse[1] < 310:
                    print("in box 1")
                    if player_state == 0:
                        display.display_o(75, 130)
                        player_state = 1

                    else:
                        display.display_x(75, 130)
                        player_state = 0
            # code

        display.hud()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
