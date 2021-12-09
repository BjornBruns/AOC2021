#!/usr/bin/env python3

from functools import reduce

data_file_name = "../day8_data.txt"

with open(data_file_name, 'r') as file:
    outputs = [digit for line in file for digit in line.split("|")[1].split()]

def solve(outputs):
    return len([digit for digit in outputs if len(digit) in (2, 3, 4, 7)])

print(solve(outputs))