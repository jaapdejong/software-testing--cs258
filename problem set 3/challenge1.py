#!/usr/bin/python

# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

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

def findFreeLocation(grid):
	for row in range(0, SIZE):
		for column in range(0, SIZE):
			value = grid[row][column]
			if value == 0:
				return row, column
	return None, None

def show(grid):
	for row in range(0, SIZE):
		for column in range(0, SIZE):
			value = grid[row][column]
			print(value),
		print

def solve(grid):
	row, column = findFreeLocation(grid)
	if row == None:
#		show(grid)
		return grid
	for value in range(1, SIZE+1):
		grid[row][column] = value
		if check_sudoku(grid) and solve(grid):
			return grid
	grid[row][column] = 0
	return False

def solve_sudoku(grid):
	ok = check_sudoku(grid)
	if ok:
		return solve(grid)
	else:
		return ok
	
print "Try invalid"
print solve_sudoku(invalid)
print "Try easy"
print solve_sudoku(easy)
print "Try hard"
print solve_sudoku(hard)
print "Done"


