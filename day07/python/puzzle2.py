#!/usr/bin/env python3

from statistics import median
from collections import Counter
from functools import reduce

data_file_name = "../day7_data.txt"

with open(data_file_name, 'r') as file:
    positions = [int(crab) for crab in file.read().split(',')]

def triangular(start, end):
    """ The fuel used from start to end is the nth triangular number where n is the absolute distance """
    n = abs(start-end)
    return int((n + 1) * n / 2)

def calculate_fuel(crabs_per_position, new_position):
    """ Calculate the total fuel for all crabs on the same starting position to a new position """
    return int(reduce((lambda x, key: (x + (triangular(key, new_position) * crabs_per_position[key]))), crabs_per_position, 0))

def solve(positions):
    """ Calculate the total fuel necessary for all possible positions and return the lowest number """
    crabs_per_position = Counter(positions)
    return min([calculate_fuel(crabs_per_position, position) for position in range(min(positions), (max(positions) + 1))])

print(solve(positions))