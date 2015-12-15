#!/usr/bin/python

# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]
easySolved = [[2,9,4,5,6,3,1,7,8],
              [3,1,6,7,2,8,4,9,5],
              [8,5,7,1,4,9,6,3,2],
              [6,2,9,4,3,1,5,8,7],
              [5,7,3,6,8,2,9,1,4],
              [1,4,8,9,5,7,2,6,3],
              [7,6,5,3,9,4,8,2,1],
              [9,8,1,2,7,5,3,4,6],
              [4,3,2,8,1,6,7,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]
hardSolved = [[1,6,2,8,5,7,4,9,3],
              [5,3,4,1,2,9,6,7,8],
              [7,8,9,6,4,3,5,2,1],
              [4,7,5,3,1,2,9,8,6],
              [9,1,3,5,8,6,7,4,2],
              [6,2,8,7,9,4,1,3,5],
              [3,5,6,4,7,8,2,1,9],
              [2,4,1,9,3,5,8,6,7],
              [8,9,7,2,6,1,3,5,4]]

SIZE = 9
ROOTSIZE = 3

def isLegal(grid):
	if grid == None:
		return False
	if len(grid) != SIZE:
		return False
	for row in range(0, SIZE):
		if len(grid[row]) != SIZE:
			return False
	return True

def allLegalRows(grid):
	for row in range(0, SIZE):
		usedValues = [];
		for column in range(0, SIZE):
			value = grid[row][column]
			if value == 0:
				continue
			if value < 0 or value > SIZE:
				return False
			if value in usedValues:
				return False
			usedValues.append(value)
	return True						

def allLegalColumns(grid):
	for column in range(0, SIZE):
		usedValues = [];
		for row in range(0, SIZE):
			value = grid[row][column]
			if value == 0:
				continue
			if value < 0 or value > SIZE:
				return False
			if value in usedValues:
				return False
			usedValues.append(value)
	return True						

def allLegalSub(grid, startRow, startColumn):
	usedValues = [];
	for row in range(startRow, startRow + ROOTSIZE):
		for column in range(startColumn, startColumn + ROOTSIZE):
			value = grid[row][column]
			if value == 0:
				continue
			if value < 0 or value > SIZE:
				return False
			if value in usedValues:
				return False
			usedValues.append(value)
	return True
	
def allLegalSubs(grid):
	for row in range(0, SIZE, ROOTSIZE):
		for column in range(0, SIZE, ROOTSIZE):
			if not allLegalSub(grid, row, column):
				return False
	return True			

def check_sudoku(grid):
	if not isLegal(grid):
		return None
	if not allLegalRows(grid):
		return False
	if not allLegalColumns(grid):
		return False
	if not allLegalSubs(grid):
		return False
	return True

assert check_sudoku(ill_formed) == None
assert check_sudoku(valid) == True
assert check_sudoku(invalid) == False
assert check_sudoku(easy) == True
assert check_sudoku(hard) == True
assert check_sudoku(easySolved) == True
assert check_sudoku(hardSolved) == True
print "OK"

