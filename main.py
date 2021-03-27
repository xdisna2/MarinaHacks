import pygame
import display


def main():
    mouse = pygame.mouse.get_pos()
    # game loop, terminates when the game ends
    run = True

    while run:
        # gets a list of all the events and loops through them
        for event in pygame.event.get():
            # if the user exits the window, terminate the game
            if event.type == pygame.QUIT:
                run = False

        display.bg_color()
        display.grid()
        display.display_x()
        display.display_o()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
