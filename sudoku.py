

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

Y = "ABCDEFGHI"
X = "123456789"
MAX_Y = len(Y)
COUNT = 0


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in Y:
        row = ''
        for j in X:
            row += (str(board[i + j]) + " ")
        print(row)

def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in Y:
        for c in X:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

def possible(board, row, col, n):
    for x in range(0, 9):
        if board[Y[row] + X[x]] == n:
            return False
    for x in range(0, 9):
        if board[Y[x] + X[col]] == n:
            return False
    x0 = (row // 3) * 3
    y0 = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[Y[i + x0] + X[j + y0]] == n:
                return False
    return True

def solve(board, x, y):

    if x == MAX_Y - 1 and y == MAX_Y:
        return True
    if y == MAX_Y:
        x += 1
        y = 0
    # check if there is a number already in the spot
    if board[Y[x] + X[y]] != 0:
        return solve(board, x, y + 1)
    # we check if the number is possible to add if so we put it else we go again
    for n in range(1, 10):
        if possible(board, x, y, n):
            board[Y[x] + X[y]] = n
            if solve(board, x, y + 1):
                return True
        board[Y[x] + X[y]] = 0

    if board[Y[y] + X[x]] == 0:
        return False

    return False


def backtracking(board):
    """Takes a board and returns solved board."""
    global COUNT

    solvedBoard = board
    if solve(solvedBoard, 0, 0):
        COUNT += 1
        print('-----------------')
        print('solved puzzle #' + str(COUNT))

    else:
        print('Unsolved!')
    return solvedBoard


if __name__ == '__main__':
    # Read boards from source.
    src_filename = 'sudoku_boards.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = {Y[r] + X[c]: int(line[9 * r + c])
                 for r in range(9) for c in range(9)}

        # print_board(board)

        # Solve with backtracking
        solved_board = backtracking(board)

        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')



    print("Finishing all boards in file.")
