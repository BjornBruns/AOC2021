#!/usr/bin/env python3

from functools import reduce

data_file_name = "../day9_data.txt"

with open(data_file_name, 'r') as file:
    lines = [line.rstrip("\n") for line in file]
    matrix = [list(map(lambda x: 1 if int(x) < 9 else 0, list(line))) for line in lines] # Instead of 0 till 9, map to 0s and 1s

def findBasin(matrix, row, col, start_x, start_y, visited, size):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or visited[row][col] or not matrix[row][col]:
        return

    size.append(1)
    visited[row][col] = True

    findBasin(matrix, row, col - 1, start_x, start_y, visited, size) # Up  
    findBasin(matrix, row + 1, col, start_x, start_y, visited, size) # Right
    findBasin(matrix, row, col + 1, start_x, start_y, visited, size) # Down
    findBasin(matrix, row - 1, col, start_x, start_y, visited, size) # Left
    
def findDistinctBasins(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    sizes = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] and not visited[i][j]:
                start_x, start_y = i, j
                size = [] # A list instead of simple integer counter because lists are passed as a reference and integer is not

                findBasin(matrix, i, j, start_x, start_y, visited, size)
                sizes.append(size)

    return [sum(size) for size in sizes]

def solve(matrix):
    return reduce((lambda x, y: x * y), sorted(findDistinctBasins(matrix))[-3:])

print(solve(matrix))