import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

# Check for empty places on board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

# Select a random place for the computer
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

# Check if a player has won in any row
def row_win(board, player):
    for x in range(len(board)):
        if all(board[x, y] == player for y in range(len(board))):
            return True
    return False

# Check if a player has won in any column
def col_win(board, player):
    for x in range(len(board)):
        if all(board[y, x] == player for y in range(len(board))):
            return True
    return False

# Check if a player has won in either diagonal
def diag_win(board, player):
    # Check main diagonal
    if all(board[i, i] == player for i in range(len(board))):
        return True
    # Check anti-diagonal
    if all(board[i, len(board) - 1 - i] == player for i in range(len(board))):
        return True
    return False

# Evaluate the board for a winner or a tie
def evaluate(board):
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    if np.all(board != 0):
        return -1  # Tie
    return 0  # No winner yet

# Print the board
def print_board(board):
    print('\n'.join([' '.join(map(str, row)) for row in board]))

# Main function to start the game
def play_game():
    board = create_board()
    winner = 0
    counter = 1
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    sleep(2)

    while winner == 0:
        # User's turn
        print("Your turn (Player 1). Enter row and column (0, 1, or 2):")
        try:
            row, col = map(int, input("Enter row and column separated by a space: ").split())
            if board[row, col] != 0:
                print("That spot is already taken. Try again.")
                continue
            board[row, col] = 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers from 0 to 2.")
            continue

        print("Board after move:")
        print_board(board)
        sleep(2)
        winner = evaluate(board)
        if winner != 0:
            break

        # Computer's turn
        board = random_place(board, 2)
        print("Board after computer's move:")
        print_board(board)
        sleep(2)
        winner = evaluate(board)

    if winner == 1:
        print("Congratulations! You won!")
    elif winner == 2:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie!")

# Driver code
if __name__ == '__main__':
    play_game()
