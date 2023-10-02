from random import randint

size = 6
number_ships = 5


def new_game():
    """
    Starts a new game. Sets the size and number of ships for the game.
    Informs about how the game works and asks the player for its name.
    """
    global player_name
    print("^" * 40)
    print("Welcome to the Battleship Game!")
    print(f"You have {number_ships} ships to find on the board.")
    print("Boardsize: {size}x{size}.")
    print(f"Available options are row: 1-{size} and column: 1-{size}.")
    print("^" * 40)
    player_name = input("What is your name? ")
    print("Nice to meet you " + player_name + ", let's play a game!")
    print("^" * 40)


def build_board(size):
    return [["O" for count in range(size)] for count in range(size)]


def print_player_board(board):
    print(f"{player_name}'s board:")
    for i in board:
        print(*i)


def print_computer_board(board):
    print("\nComputer's board:")
    for i in board:
        print(*i)


def random_row(size):
    return randint(0, size - 1)


def random_column(size):
    return randint(0, size - 1)


def build_ships():
    pass


def player_guess():
    pass


def main():
    new_game()
    board = build_board(size)
    print_player_board(board)
    print_computer_board(board)


main()

