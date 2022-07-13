from random import randrange
from turtle import delay


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    # print("\
    #     +-------+-------+-------+\n, |       |       |       |\n, |   1   |   2   |   3   |\n, |       |       |       |\n, +-------+-------+-------+\n, |       |       |       |\n, |   4   |   X   |   6   |\n, |       |       |       |\n, +-------+-------+-------+\n, |       |       |       |\n, |   7   |   8   |   9   |\n, |       |       |       |\n, +-------+-------+-------+\n\
    #       ")
    for row in board:
        for cell in row:
            print("     ", cell, end=" ")
        print("\n")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    board0 = []
    for row in board:
        board0 = board0 + row

    # Requiring the move from the user , and validating it
    while True:
        try:
            i = int(input("Enter your move [1 - 9] :"))
        except:
            print("Enter an integer [1 - 9] for your move :")
            continue
        if i not in range(1, 10):
            continue
        if i not in board0:
            print(i, " is not an empty cell ! Please enter an other move.")
            continue

        # Updating the board with the user's input
        
        if i == 1 or i == 2 or i == 3:
            board[0][i - 1] = "O"
        elif i == 4 or i == 5 or i == 6:
            board[1][i - 4] = "O"
        else:
            board[2][i - 7] = "O"

        return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    lst = []
    for i in [0, 1, 2]:
        row = board[i]
        for cell in [0, 1, 2]:
            if type(row[cell]) is int:
                lst.append((i + 1, cell + 1))

    return lst


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if sign not in ["O", "X"]:
        return None

    lst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                lst.append((i + 1, j + 1,))

    if len(lst) < 3:
        return False

    # Parsing the list of sign's position and determine whether player using sign has won
    
    for i in range(3) :
        # Checking for the i-th row
        for k in range(3) :
            if board[i][k] == sign:
                continue
            else : break
        else :
            return True
    
        # Checking for the i-th column
        for k in range(3) :
            if board[k][i] == sign :
                continue
            else :
                break
        else :
            return True
    
    # Looking up to the diagonals
    for i in range(3) :
        if board[i][i] != sign :
            break
    else :
        return True
    for i in range(3) :
        if board[i][2 - i] != sign :
            return False
    else :
        return True


def draw_move(board):
    # The function draws the computer's move and updates the board.
    lst = make_list_of_free_fields(board)
    index = randrange(len(lst))
    board[lst[index][0] - 1][lst[index][1] - 1] = "X"

    return board


# Impementing the game live
board0 = [[1, 2, 3],
         [4, "X", 6],
         [7, 8, 9]]
board = board0.copy()
print("Let's play the tic-tac-toe game , we're going to have some fun !")

# delay(1000)
print("     Here is the board :")
display_board(board)

while len(make_list_of_free_fields(board)) :
    
    board = enter_move(board)
    display_board(board)
    if victory_for(board, "O") :
        print("Congratulation ! You've won ...")
        board = board0.copy()
        restart = input("Press enter to start a new party ?")
        restart = restart == ""
        if restart :
            continue
        break
    
    board = draw_move(board)
    print('     It\'s my turn ...\n')
    display_board(board)
    if victory_for(board, "X") :
        print("You lose !")
        board = board0.copy()
        restart = input("Press enter to start a new party ?")
        restart = restart == ""
        if restart :
            continue
        break
    if not len(make_list_of_free_fields(board)) :
        print("Match nul !")
        board = board0.copy()
        restart = input("Would you like to restart ?")
        restart = restart.lower() == 'yes'
        if restart :
            continue
        break
