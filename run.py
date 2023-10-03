# Import to get randomized numbers
from random import randint

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
    print("Welcome to the Battleship Game!")
    print(f"You have {number_ships} ships to find on the board.")
    print(f"Boardsize: {size}x{size}.")
    print(f"Available options are row: 1-{size} and column: 1-{size}.")
    print("^" * 40)
    player_name = input("What is your name? ")
    print("Nice to meet you " + player_name + ", let's play a game!")
    print("^" * 40)


def random_player_values(size):
    """
    Creates random positions for the player's board.
    """
    global player_row
    global player_column
    player_row, player_column = randint(0, size - 1), randint(0, size - 1)


def random_computer_values(size):
    """
    Creates random positions for the computer's board.
    """
    global computer_row
    global computer_column
    computer_row, computer_column = randint(0, size - 1), randint(0, size - 1)


def build_board(size):
    """
    Structure for the game board.
    """
    return [["O" for count in range(size)] for count in range(size)]


def print_player_board(board, ship_row, ship_column):
    """
    Prints out the player's name and board.
    """
    print(f"{player_name}'s board:")
    for i in board:
        print(*i)
    print(f"{player_name}'s guess: {player_row}, {player_column}")


def print_computer_board(board, ship_row, ship_column):
    """
    Prints out the computer's board.
    """
    print("\nComputer's board:")
    for i in board:
        print(*i)
    print(f"Computer's guess: {computer_row}, {computer_column}")


def main():
    """
    Includes all the game functions to make it easy to read and
    keeps it all together.
    """
    new_game()
    board = build_board(size)
    random_player_values(size)
    random_computer_values(size)
    print_player_board(board, player_row, player_column)
    print_computer_board(board, computer_row, computer_column)


main()
    """
    Function with all the game functions in it.
    """
