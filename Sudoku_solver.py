# -*- coding: utf-8 -*-
"""
Sudoku solver

Requires numpy package for matrix display

Using a list of lists (2d array) to represent
a sudoku board, identify candidates for empty
squares (coordinates with a value of 0).

Once a candidate is found, replace the 0 with
that candidate and iterate until the next
empty square is found.  

Continue until:
    no empty squares remain then print the result
or 
    no candidates can be found for the
    current emptry square then back track

"""


# Puzzle template
# mypuzzle = [[, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ],
#             [, , , , , , , , ]]
#
# Puzzles examples
# test_puzzle = [[0, 2, 3, 4, 5, 6, 7, 8, 9],
#                [1, 2, 3, 4, 5, 6, 7, 8, 0],
#                [1, 0, 3, 4, 5, 6, 7, 8, 9],
#                [1, 2, 3, 0, 5, 0, 7, 8, 9],
#                [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                [1, 2, 3, 4, 0, 6, 7, 0, 9],
#                [1, 0, 3, 4, 5, 6, 7, 8, 9],
#                [1, 2, 3, 4, 5, 6, 7, 0, 9]]
#
# easy_puzzle = [[0, 0, 4, 0, 0, 6, 0, 8, 0],
#                [7, 8, 0, 4, 2, 0, 0, 0, 1],
#                [0, 1, 0, 5, 0, 3, 0, 0, 0],
#                [9, 7, 0, 0, 3, 5, 0, 0, 0],
#                [4, 3, 0, 0, 9, 0, 0, 2, 7],
#                [0, 0, 0, 7, 1, 0, 0, 3, 9],
#                [0, 0, 0, 3, 0, 2, 0, 4, 0],
#                [1, 0, 0, 0, 5, 7, 0, 9, 2],
#                [0, 2, 0, 9, 0, 0, 7, 0, 0]]
#
# hard_puzzle = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 3, 6, 0, 0, 0, 0, 0],
#                [0, 7, 0, 0, 9, 0, 2, 0, 0],
#                [0, 5, 0, 0, 0, 7, 0, 0, 0],
#                [0, 0, 0, 0, 4, 5, 7, 0, 0],
#                [0, 0, 0, 1, 0, 0, 0, 3, 0],
#                [0, 0, 1, 0, 0, 0, 0, 6, 8],
#                [0, 0, 8, 5, 0, 0, 0, 1, 0],
#                [0, 9, 0, 0, 0, 0, 4, 0, 0]]


def return_box_coord(puzzle, row_index, col_index):
    
    start_row = (row_index // 3) * 3
    start_col = (col_index // 3) * 3
    
    end_row = start_row + 2
    end_col = start_col + 2
    
    return start_row, start_col, end_row, end_col



def check_row(puzzle, row_index, n):
    
    if n in puzzle[row_index]:
            return True
        
    return False
        

    
def check_col(puzzle, col_index, n):
    
    for row in puzzle:
        if n == row[col_index]:
            return True
        
    return False
    


def check_box(puzzle, row_index, col_index, n):
    
    s_row, s_col, e_row, e_col = return_box_coord(puzzle, row_index, col_index)
    
    for r in range(s_row, e_row + 1):
        for c in range(s_col, e_col + 1):
            if n == puzzle[r][c]:
                return True
            
    return False
    

    
def candidate(puzzle, row, col, n):
    
    if (check_row(puzzle, row, n) == True) or (check_col(puzzle, col, n) == True) or (check_box(puzzle, row, col, n) == True):
           return False
       
    return True

import numpy as np #for solved puzzle formatting

def sudoku_solver(puzzle):
    
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                for n in range(1, 10):
                    if candidate(puzzle, r, c, n) == True:
                        puzzle[r][c] = n
                        sudoku_solver(puzzle)
                        puzzle[r][c] = 0
                return
                        
    print(np.matrix(puzzle))
    return True

