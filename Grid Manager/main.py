import tkinter

empty_grid = []


#Generates a grid full of 0's with a specified area
def generate_grid(grid,area):
    for i in range(area):
        for j in range(area):
            grid.insert(j,0)
    return grid

#UNFINISHED - prints the grid in box form
def print_grid(grid):
    length = len(grid)
    len_side = length/2
    for i in grid:
        pass
            

grid = generate_grid(empty_grid,4)
print(grid)

