import pygame
import numpy as np


matrix = [[None, None, None], [None, None, None], [None, None, None]]
mat1 = np.array(matrix)
# print(mat1)


def playerInput(turn_count):
    loc = False
    while loc is False:
        try:
            x, y = int(input("Enter row:")), int(input("Enter col:"))

            if mat1[x, y] is not None:
                print("\n", mat1, "\n")
                raise IndexError()

            if turn_count % 2 == 0:
                mat1[x, y] = "O"
            else:
                mat1[x, y] = "X"

            print("\n", mat1, "\n")
            loc = True
        except ValueError:
            print("You need to enter an integer. Please try again")
        except IndexError:
            print("Invalid index. You need to enter between 0-2 and make sure the space is not already occupied")


def checkHorizontal():
    for row in range(3):
        if mat1[row, 1] is not None:
            if (mat1[row, 0]) == mat1[row, 1] and (mat1[row, 2]) == mat1[row, 1]:
                return True
        else:
            return False


def checkVertical():
    for col in range(3):
        if mat1[1, col] is not None:
            if (mat1[0, col]) == mat1[1, col] and (mat1[2, col]) == mat1[1, col]:
                return True
        else:
            return False


def checkDiagonal():
    if mat1[1, 1] is not None:
        if mat1[0, 0] == mat1[1, 1] and mat1[2, 2] == mat1[1, 1]:
            return True
        elif mat1[2, 0] == mat1[1, 1] and mat1[0, 2] == mat1[1, 1]:
            return True
    else:
        return False


def checkWinCondition():
    if checkHorizontal() or checkVertical() or checkDiagonal():
        return True

    return False


def main():
    run = True
    turn_counter = 0

    while run:
        turn_counter += 1

        if turn_counter % 2 == 0:
            print("Player 2's turn!")
        else:
            print("Player 1's turn!")

        playerInput(turn_counter)

        if turn_counter >= 5:
            run = not(checkWinCondition())
            if turn_counter % 2 == 0:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")


if __name__ == "__main__":
    main()

