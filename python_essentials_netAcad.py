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


# display_board([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    board0 = []
    for row in board0:
        board0 + row

    # Requiring the move from the user , and validating it
    while True:
        try:
            i = int(input("Enter your move [1 - 9] :"))
        except:
            print("Enter an integer [1 - 9] for your move :")
            continue
        if i not in range(1, 10):
            continue
        if i in board0:
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


# display_board(enter_move([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]))


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


# print(make_list_of_free_fields(([
#     ["X", 2, 3],
#     [4, "O", "X"],
#     [7, "O", 9]
# ])))


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if sign not in ["O", "X"]:
        print("Sign should be one of 'O' and 'X' , but got :", sign)
        return None

    lst = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                lst.append((i + 1, j + 1,))

    if len(lst) < 3:
        print("Player using :", sign, "'s hasn't won the game!")
        return False

    # Parsing the list of sign's position and determine whether player using sign has won
    has_won = True
    if lst[0][0] == lst[0][1]:
        for i in range(2):
            if lst[i + 1][0] != lst[i + 1][1] and lst[i + 1][0] + lst[i + 1][1] != 4:
                has_won = False
                break
    else:
        for i in range(2):
            if lst[i + 1][0] != lst[0][0] and lst[i + 1][1] != lst[0][1]:
                has_won = False
                break

    # Returning the result
    return has_won


o = victory_for(
    [["X", 2, "O"],
     [4, "X", "O"],
     [7, 9, "O"]], "O"
)
print(o)


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass
