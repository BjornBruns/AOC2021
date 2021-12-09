#!/usr/bin/env python3

from statistics import median
from collections import Counter
from functools import reduce

data_file_name = "../day7_data.txt"

with open(data_file_name, 'r') as file:
    positions = [int(crab) for crab in file.read().split(',')]

def solve(positions):
    location = median(positions)
    crabs_per_position = Counter(positions)
    return int(reduce((lambda x, key: (x + ((abs(key - location)) * crabs_per_position[key]))), crabs_per_position, 0))

print(solve(positions))