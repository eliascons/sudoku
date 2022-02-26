#!/usr/bin/env python
#coding:utf-8
import numpy as np

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"



def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def possible(y,x,n, board) :

    for i in range(0, 9):
        if board[y][i] == n:
            return False
    for i in range(0, 9):
        if board[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == n:
                return False
    return True

def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    # solved_board = board

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n, board) :
                        board[y][x] = n
                        backtracking(board)
                        board[y][x] = 0
                return
    print(np.matrix(board))




if __name__ == '__main__':
    #  Read boards from source.
    # src_filename = 'sudoku_boards.txt'
    # try:
    #     srcfile = open(src_filename, "r")
    #     sudoku_list = srcfile.read()
    # except:
    #     print("Error reading the sudoku file %s" % src_filename)
    #     exit()
    #
    # # Setup output file
    # out_filename = 'output.txt'
    # outfile = open(out_filename, "w")
    #
    # # Solve each board using backtracking
    # for line in sudoku_list.split("\n"):
    #
    #     if len(line) < 9:
    #         continue
    #
    #     # Parse boards to dict representation, scanning board L to R, Up to Down
    #     board = { ROW[r] + COL[c]: int(line[9*r+c])
    #               for r in range(9) for c in range(9)}
    #
    #     # Print starting board. TODO: Comment this out when timing runs.
    #     print_board(board)
    #
    #     # Solve with backtracking
    #     solved_board = backtracking(board)
    #
    #     # Print solved board. TODO: Comment this out when timing runs.
    #     print_board(solved_board)
    #
    #     # Write board to file
    #     outfile.write(board_to_string(solved_board))
    #     outfile.write('\n')
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    backtracking(board)




    print("Finishing all boards in file.")