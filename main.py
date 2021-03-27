import pygame

WIDTH, HEIGHT = 900, 500
# creates the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
SILVER = (192, 192, 192)


def bg_color():
    WIN.fill(SILVER)
    pygame.display.update()


def main():
    # game loop, terminates when the game ends
    run = True

    while run:
        # gets a list of all the events and loops through them
        for event in pygame.event.get():
            # if the user exits the window, terminate the game
            if event.type == pygame.QUIT:
                run = False

        bg_color()

    pygame.quit()


if __name__ == "__main__":
    print("Hello World")
    main()
