# https://bigmonty12.github.io/battleship
import random

def welcome_message():
    print("Welcome to Battleship")
    print("=====================")
    play = input("Are you ready to play?: ")
    if play == "yes" or play == "YES" or play == "Yes" or play == "Y" or play == "y":
        print("Let's start!")
    else:
        print("Bye..")
        exit()

# make a 2D list filled with O at a user-decided length/width
def build_board(size):
    return [["O" for count in range(size)] for count in range(size)]

# remove all commas and brackets to make the board 'clean;
def print_board(board):
    for k in board:
        print(*k)

def build_ship(size):
    # ship 1 len is between 2 and len of board
    len_ship = random.randint(2, size)
    orientation = random.randint(0,1)

    # ship 1 is horizontal if orientation is 0, vertical if 1
    if orientation == 0:
        row_ship = [random.randint(0, size - 1)]*len_ship
        col = random.randint(0, size - len_ship)
        col_ship = list(range(col, col + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(0, size-1)]*len_ship
        row = random.randint(0, size-len_ship)
        row_ship = list(range(col, col + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)

# user inputs their guess, function converts their guess to work with the
# 0-based indexing
def user_guess():
    print()
    row = int(input("Enter a row: ")) - 1
    col = int(input("Enter a column: ")) - 1
    return(row, col)

def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print("You already guess that coordinate.")
        board[guess[0]][guess[1]] = "M"
        return board
    guesses.append(guess)
    if guess in ship:
        print("You hit a battleship!")
        board[guess[0]][guess[1]] = "X"
        ship.remove(guess)
        return board
    print("You missed!")
    return board
    
def main():
    welcome_message()
    board = build_board(5)
    ship = build_ship(4)
    guesses = []
    while len(ship) > 0:
        board = update_board(user_guess(), board, ship, guesses)
        print_board(board)
    print("======================")
    print("You sunk a battleship!")
    print("======================")
    again = input("You win, do you want to play again?")
    if again == "yes" or again == "y" or again == "Y" or again == "YES" or again == "Yes":
        return main()
    else:
        print("Bye")
        exit()
    return
