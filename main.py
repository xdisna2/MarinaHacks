import pygame
import display

pygame.init()


# 0 = O's turn | 1 = X's turn
def main():
    # game loop, terminates when the game ends
    run = True

    while run:
        mouse = pygame.mouse.get_pos()
        # print(mouse)
        # gets a list of all the events and loops through them
        for event in pygame.event.get():
            # if the user exits the window, terminate the game
            if event.type == pygame.QUIT:
                run = False

            # code

        display.bg_color()
        display.grid()
        display.clear_rectangle()
        display.hud()
        display.display_x()
        display.display_o()
        display.display_turn(1)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
