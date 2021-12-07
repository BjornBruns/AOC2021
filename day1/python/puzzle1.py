#!/usr/bin/env python3

from functools import reduce

data_file_name = "../day1_data.txt"

with open(data_file_name, 'r') as file:
    depths = [int(line.rstrip()) for line in file]

g = lambda x, i: x + (1 if i >= 0 and depths[i] > depths[i - 1] else 0)
print(reduce(g, range(len(depths)), 0))