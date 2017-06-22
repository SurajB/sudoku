#This is sudoku game built in python3
#learnings - enumerate, list comprehension, deepcopy, recursive function return problem, limiting recurssion

from random import randint, choice
from copy import deepcopy
from time import sleep

print("\nLet us play sudoku\n")

user_choice = input("Enter your choice of difficulty - E for Easy, M for Medium, H for Hard: ").upper()

def print_grid(grid):

	if grid == False:
		print("Hello")
	for index,row in enumerate(grid):
		print(" ".join(row[0:3]) + "|" + " ".join(row[3:6]) + "|" + " ".join(row[6:]))
		if index == 2 or index == 5:
			print("- " * 9)

def make_sudoku(grid, grid_pair, user_choice):

	if user_choice == "E":
		range_val = randint(40, 50)
	elif user_choice == "M":
		range_val = randint(52, 58)
	else:
		range_val = randint(60, 65)

	for i in range(range_val):
		rand_pos = choice(grid_pair)
		row_fill = rand_pos[0]
		col_fill = rand_pos[1]
		(grid[row_fill])[col_fill] = "X"
		grid_pair.remove(rand_pos)

	return grid

def sudoku_gen(grid, i, j, ctr):
	
	val_list = [1,2,3,4,5,6,7,8,9]

	lst_1 = [[i,j] for i in range(3,6) for j in range(6,9)]
	lst_2 = [[i,j] for i in range(6,9) for j in range(0,9)]
	final_leap_list = lst_1 + lst_2

	prev = deepcopy(grid)

	for row in range(i,(i+3)):

		for col in range(j,(j+3)):

			flag = row_col_check(row, col, [1,2,3,4,5,6,7,8,9], i, j, prev)
			if flag == False and [row,col] not in final_leap_list:
				ctr += 1
				"""print("The recurssion has occured " + str(ctr))"""
				flag, ctr = sudoku_gen(prev, i, j, ctr)
				return flag, ctr
			elif flag == False and [row,col] in final_leap_list:
				"""print("Restarting the grid block" + str(ctr))"""
				return False, ctr

	return True, ctr

def row_col_check(row_fill, col_fill, grid_val_list, i, j, prev):

	"""print(row_fill, col_fill)"""

	for row in range(0,row_fill):

		if int((grid[row])[col_fill]) in grid_val_list:
			grid_val_list.remove(int((grid[row])[col_fill]))

	for col in range(0,col_fill):

		if int((grid[row_fill])[col]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill])[col]))

	grid_val_list_final = box_check(row_fill, col_fill, grid_val_list)

	if grid_val_list_final == []:
		return False
	else:
		rand_val = str(choice(grid_val_list_final))
		(grid[row_fill])[col_fill] = rand_val
		"""print(grid_val_list_final, rand_val)"""

def box_check(row_fill, col_fill, grid_val_list):

	if row_fill%3 == 1 and col_fill%3 == 0:

		if int((grid[row_fill-1])[col_fill+1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill+1]))
		if int((grid[row_fill-1])[col_fill+2]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill+2]))

	elif row_fill%3 == 1 and col_fill%3 == 1:
		if int((grid[row_fill-1])[col_fill-1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill-1]))
		if int((grid[row_fill-1])[col_fill+1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill+1]))

	elif row_fill%3 == 1 and col_fill%3 == 2:
		if int((grid[row_fill-1])[col_fill-2]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill-2]))
		if int((grid[row_fill-1])[col_fill-1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill-1]))

	elif row_fill%3 == 2 and col_fill%3 == 0:
		if int((grid[row_fill-2])[col_fill+1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-2])[col_fill+1]))
		if int((grid[row_fill-2])[col_fill+2]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-2])[col_fill+2]))
		if int((grid[row_fill-1])[col_fill+1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill+1]))
		if int((grid[row_fill-1])[col_fill+2]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill+2]))

	elif row_fill%3 == 2 and col_fill%3 == 1:
		if int((grid[row_fill-2])[col_fill-1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-2])[col_fill-1]))
		if int((grid[row_fill-2])[col_fill+1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-2])[col_fill+1]))
		if int((grid[row_fill-1])[col_fill-1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill-1]))
		if int((grid[row_fill-1])[col_fill+1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill+1]))

	elif row_fill%3 == 2 and col_fill%3 == 2:
		if int((grid[row_fill-2])[col_fill-2]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-2])[col_fill-2]))
		if int((grid[row_fill-2])[col_fill-1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-2])[col_fill-1]))
		if int((grid[row_fill-1])[col_fill-2]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill-2]))
		if int((grid[row_fill-1])[col_fill-1]) in grid_val_list:
			grid_val_list.remove(int((grid[row_fill-1])[col_fill-1]))

	else:
		return grid_val_list

	return grid_val_list

def grid_call(ctr):

	ctr += 1
	#print("count is" + str(ctr))

	grid_flag, ctr = sudoku_gen(grid, 0, 0, ctr)
	grid_flag, ctr = sudoku_gen(grid, 0, 3, ctr)
	grid_flag, ctr = sudoku_gen(grid, 0, 6, ctr)

	return grid, ctr

def second_grid(ctr):

	ctr += 1
	#print("The recurssion for second grid " + str(sec_ctr))
	
	grid_flag, ctr = sudoku_gen(grid, 3, 0, ctr)
	#print(ctr)
	grid_flag, ctr = sudoku_gen(grid, 3, 3, ctr)
	#print(ctr)
	grid_flag, ctr = sudoku_gen(grid, 3, 6, ctr)
	#print("Final count: " + str(ctr))

	if grid_flag == False:
		ctr = second_grid(ctr)
		return  ctr

	return grid, ctr


def final_leap(ctr):

	ctr += 1
	#print("The final grid recurssion" + str(fin_ctr))

	grid_flag, ctr = sudoku_gen(grid, 6, 0, ctr)
	#print(ctr)
	if grid_flag == False:
		ctr = final_leap(ctr)
		return ctr

	grid_flag, ctr = sudoku_gen(grid, 6, 3, ctr)
	#print(ctr)
	if grid_flag == False:
		ctr = final_leap(ctr)
		return ctr

	grid_flag, ctr = sudoku_gen(grid, 6, 6, ctr)
	#print("Final count: " + str(ctr))
	if grid_flag == False:
		ctr = final_leap(ctr)
		return ctr
	
	return grid, ctr

grid = []
grid_pair = []
global ctr
ctr = 0
#rec_ctr = 0
#fin_ctr = 0
#sec_ctr = 0

for x in range(9):
		grid.append(["X"] * 9)

for i in range(0,9):
	for j in range(0,9):  
		grid_pair.append([i,j])

grid_1, first_ctr = grid_call(0)
grid_2, sec_ctr = second_grid(ctr)
grid_3, fin_ctr = final_leap(ctr)

#print("No of recurssions in first grid: " + str(first_ctr))
#print("No of recurssions in second grid: " + str(sec_ctr))
#print("No of recurssions in final grid: " + str(fin_ctr))

grid_ans = deepcopy(grid)

grid = make_sudoku(grid, grid_pair, user_choice)

print("Here you go :)\n")
print_grid(grid)

sleep(5)
ans_choice = input("\nWanna see the answer? Hit Y :)\n").upper()

if ans_choice == "Y":
	print_grid(grid_ans)

