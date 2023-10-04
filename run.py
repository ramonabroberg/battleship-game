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


def build_ships(size):
    r_ship = [random.randint(0, size - 1)]
    col = random.randint(0, size - 1)
    c_ship = list(range(col, col + 1))
    coords = tuple(zip(r_ship, c_ship))
    print(list(coords))


def update_board():
    pass


def main():
    """
    Includes all the game functions to make it easy to read and
    keeps it all together.
    """
    new_game()
    board = build_board(size)
    print_player_board(board)
    print_computer_board(board)
    build_ships(size)
    player_guess()
    random_values(size)


main()

