# Import to get randomized numbers
from random import randint
import random

# Sets the size for the boards and the amount of ships.
size = 6
number_ships = 5


def new_game():
    """
    Starts a new game.
    Informs about how the game works and asks the player for its name.
    """
    global player_name
    print("^" * 40)
    print("\nWelcome to the Battleship Game!\n")
    print(f"You have {number_ships} ships to find on the board.")
    print(f"Boardsize: {size}x{size}.")
    print(f"Available options are row: 0-{size - 1} & column: 0-{size - 1}.\n")
    print("^" * 40)
    player_name = input("\nWhat is your name? ")
    print("Nice to meet you " + player_name + ", let's play a game!\n")
    print("^" * 40)


def build_board(size):
    """
    Structure for the game board.
    """
    return [["O" for count in range(size)] for count in range(size)]


def print_player_board(board):
    """
    Prints out the player's name and board.
    """
    print(f"{player_name}'s board:")
    for i in board:
        print(*i)


def print_computer_board(board):
    """
    Prints out the computer's board.
    """
    print("\nComputer's board:")
    for i in board:
        print(*i)


def hidden_player_board(board):
    """
    Board that has the hidden ships.
    """
    for i in board:
        return (*i)


def hidden_computer_board(board):
    """
    Board that has the hidden ships.
    """
    for i in board:
        return (*i)


def player_guess():
    while True:
        row = int(input("\nChoose a row: "))
        if validate_row(row, size):
            print("Fantastic! That value is valid!\n")
            break

    while True:
        column = int(input("Choose a column: "))
        if validate_column(column, size):
            print("Perfect, that value is accepted!\n")
            break

    print(f"You guessed row: {row}, column: {column}\n")
    guess = row, column
    return guess


def random_values(size):
    """
    Creates random guess from computer.
    """
    random_list = []
    c_row, c_column = randint(0, size - 1), randint(0, size - 1)
    random_list.append(c_row)
    random_list.append(c_column)
    print(f"Computer guessed row: {c_row} column: {c_column}.")
    print(random_list)


def validate_row(row, size):
    try:
        if row < 0 or row > 5:
            raise ValueError(
                f"Only 0-{size - 1} is accepted here. You entered {row}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False

    return True


def validate_column(column, size):
    try:
        if column < 0 or column > 5:
            raise ValueError(
                f"Only 0-{size - 1} is accepted here. You entered {column}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False

    return True


def build_ships(size, ship, board, number_ships):
    for ship in range(number_ships):
        row_ship, col_ship = randint(0, size - 1), randint(0, size - 1)
        while board[row_ship][col_ship] == "X":
            row_ship, col_ship = player_guess()
        board[row_ship][col_ship] = "X"


def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print("Sorry, you have already guessed that I'm afraid")
        return board
    guesses.append(guess)
    if guess in ship:
        print("Oh no! You hit my battleship!")
        board[guess[0]][guess[1]] = 'X'
        ship.remove(guess)
        return board
    print("You missed!")
    return board


def main():
    """
    Includes all the game functions to make it easy to read and
    keeps it all together.
    """
    new_game()
    board = build_board(size)
    ship = build_ships(size)
    print_player_board(board)
    print_computer_board(board)
    guesses = []
    p_guess = player_guess()
    while len(ship) > 0:
        board = update_board(p_guess, board, ship, guesses)
        print_player_board(board)
        print_computer_board(board)
    # random_values(size)
    print("You sank my ship!")
    return


main()

