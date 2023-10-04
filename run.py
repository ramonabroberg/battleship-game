# Import to get randomized numbers
from random import randint
import random

# Sets the size for the boards and the amount of ships.
size = 4
number_ships = 1


def new_game():
    """
    Starts a new game.
    Informs about how the game works and asks the player for its name.
    """
    global player_name
    print("^" * 40)
    print("\nWelcome to the Battleship Game!\n")
    print(f"You have {number_ships} ship(s) to find on the board.")
    print(f"Boardsize: {size}x{size}.")
    print(f"Available options are row: 0-{size - 1} & column: 0-{size - 1}.\n")
    print("^" * 40)
    player_name = input("\nWhat is your name? ")
    print("Nice to meet you " + player_name + ", let's play a game!\n")
    print("^" * 40)


def player_guess():
    """
    Here the user will enter their values about row and column.
    """
    global guess
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


def ship(size):
    """
    Creates a random value for the ship.
    """
    global random_value
    global ship_row
    global ship_column
    ship_row, ship_column = randint(0, size - 1), randint(0, size - 1)
    random_value = ship_row, ship_column


def validate_row(row, size):
    """
    Validates the row value.
    """
    try:
        if row < 0 or row > size - 1:
            raise ValueError(
                f"Only 0-{size - 1} is accepted here. You entered {row}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False

    return True


def validate_column(column, size):
    """
    Validates the column value.
    """
    try:
        if column < 0 or column > size - 1:
            raise ValueError(
                f"Only 0-{size - 1} is accepted here. You entered {column}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False

    return True


def result(guess, random_value):
    """
    Gives the result of the guess.
    """
    if guess == random_value:
        print("Well look at that! You sank the battleship!")
        print(f"The ship was located on {random_value}.")
        return
    else:
        while guess != random_value:
            print(f"You missed! {random_value} was correct.")
            return


def main():
    """
    Includes all the game functions to make it easy to read and
    keeps it all together.
    """
    new_game()
    guess = player_guess()
    ship(size)
    result(guess, random_value)
    return


main()
