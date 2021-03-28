import pygame
import numpy as np

# Initiation of matrix
matrix = [[None, None, None], [None, None, None], [None, None, None]]
mat1 = np.array(matrix)


# This function basically takes in the coordinate from Front-End and current player
# Sets the player's "symbol" into a matrix
def playerInput(turn_count, x, y):
    try:
        if mat1[x, y] is not None:
            # print("\n", mat1, "\n")
            raise IndexError()

        # This determines whether its player 1 or 2 turn
        if turn_count % 2 == 0:
            # Sets the index location based on player
            mat1[x, y] = 0
        else:
            mat1[x, y] = 1

        # Immediately print the updated matrix with the player's choice
        # print("\n", mat1, "\n")

    # If there is an error on the user input, then do this code based on the error.
    except ValueError:
        # print("You need to enter an integer. Please try again")
        pass
    except IndexError:
        # print("Invalid index. You need to enter between 0-2 and make sure the space is not already occupied")
        pass


# Checks the Horizontal or Rows through the center column
def checkHorizontal():
    # Indexes the row, starts at row 0
    for row in range(3):
        # If that center column location does not have None or Nothing, then do this.
        if mat1[row, 1] is not None:
            # Compare the left and right index to see if they match the center index
            if (mat1[row, 0]) == mat1[row, 1] and (mat1[row, 2]) == mat1[row, 1]:
                return True
        else:
            return False

# This function checks the rows basically
def checkVertical():
    for col in range(3):
        if mat1[1, col] is not None:
            if (mat1[0, col]) == mat1[1, col] and (mat1[2, col]) == mat1[1, col]:
                return True
        else:
            return False

# This function checks the diagonal based on the center of the 3x3 matrix
def checkDiagonal():
    # If the center is not empty, then do this.
    if mat1[1, 1] is not None:
        # Check the diagonal that goes from left to right
        if mat1[0, 0] == mat1[1, 1] and mat1[2, 2] == mat1[1, 1]:
            return True
        # Check the diagonal that goes from right to left
        elif mat1[2, 0] == mat1[1, 1] and mat1[0, 2] == mat1[1, 1]:
            return True
    else:
        return False

# This basically checks to see if there are 3 in a row based on the
# Row, Column, or Diagonal
def checkWinCondition():
    if checkHorizontal() or checkVertical() or checkDiagonal():
        return True

    return False

# # This is the main function that will run the overall game
# def main():
#     # Run variable to control the while loop
#     run = True
#     # Initialize the turn_counter that will determine player and round
#     turn_counter = 0
#
#     while run:
#         # Start with round 1 or after re-iteration, update round
#         turn_counter += 1
#
#         # Text indication of player's turn
#         if turn_counter % 2 == 0:
#             print("Player 2's turn!")
#         else:
#             print("Player 1's turn!")
#
#         # Ask for that player's input and pass the round turn
#         playerInput(turn_counter)
#
#         # Once we get to the 5th round, player 1 has the chance to win
#         # Since they are the one's that get to place 3 marks on the matrix
#         if turn_counter >= 5:
#             # Check the Win Condition and if it is not(False) or there is no win ---> True
#             # If there is a win condition then exit the while loop
#             run = not(checkWinCondition())
#             if turn_counter % 2 == 0:
#                 print("Player 2 wins!")
#             else:
#                 print("Player 1 wins!")
#
#
# if __name__ == "__main__":
#     main()
