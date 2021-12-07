#!/usr/bin/env python3

from functools import reduce

data_file_name = "../day1_data.txt"

with open(data_file_name, 'r') as file:
    depths = [int(line.rstrip()) for line in file]

sliding = [(depths[i-2] + depths[i-1] + depths[i]) for i in range(len(depths)) if i > 1]

g = lambda x, i: x + (1 if i >= 0 and sliding[i] > sliding[i - 1] else 0)
print(reduce(g, range(len(sliding)), 0))