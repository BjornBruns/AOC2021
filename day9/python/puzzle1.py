#!/usr/bin/env python3

data_file_name = "../day9_data.txt"

with open(data_file_name, 'r') as file:
    lines = [line.rstrip("\n") for line in file]
    matrix = [list(map(lambda x: int(x), list(line))) for line in lines]

def solve(matrix):
    N = len(matrix)
    K = len(matrix[0])

    minima = []
    for row in range(N):
        for col in range(K):
            current = matrix[row][col]
            neighbors = []

            if row-1 >= 0: neighbors.append(matrix[row-1][col])
            if col+1 < K: neighbors.append(matrix[row][col+1])
            if row+1 < N: neighbors.append(matrix[row+1][col])
            if col-1 >= 0: neighbors.append(matrix[row][col-1])

            if current < min(neighbors):
                minima.append(current)
    return len(minima) + sum(minima)

print(solve(matrix))