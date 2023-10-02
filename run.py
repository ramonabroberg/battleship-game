from random import randint

def new_game():
    """
    Starts a new game. Sets the size and number of ships for the game.
    """
    size = 6
    number_ships = 5
    print("^" * 30)
    print("Welcome to the Battleship Game!")
    print(f"You have {number_ships} ships to find on the board. The boardsize is {size}x{size}.")
    print(f"Available options are row: 1-{size} and column: 1-{size}.")
    print("^" * 30)
    player_name = input("What is your name?")
    print("Nice to meet you " + player_name + ", let's play a game!")

new_game()

