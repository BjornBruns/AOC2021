#!/usr/bin/env python3

from functools import reduce

data_file_name = "../day8_data.txt"

with open(data_file_name, 'r') as file:
    entries = [(set(line.split("|")[0].split()), line.split("|")[1].split()) for line in file]

def solve_entry(entry):
    digits = [set(list(word)) for word in entry[0]]
    output_digits = [set(list(word)) for word in entry[1]]

    # Known digits by number of segments
    one = set(list(filter(lambda x: len(x) == 2 , entry[0]))[0]) 
    four = set(list(filter(lambda x: len(x) == 4 , entry[0]))[0]) 
    seven = set(list(filter(lambda x: len(x) == 3 , entry[0]))[0]) 
    eight = set(list(filter(lambda x: len(x) == 7 , entry[0]))[0])

    # Digits with 6 segments
    zero = [digit for digit in digits if (not (four - one).issubset(digit)) and len(digit) == 6][0]
    nine = [digit for digit in digits if (four | seven).issubset(digit) and len(digit) == 6][0]
    six =  [digit for digit in digits if (digit != zero) and (digit != nine) and len(digit) == 6][0]

    # All the segments separately
    a = seven - one
    b = (four - one) - (eight - zero)
    c = eight - six
    d = eight - zero
    e = eight - nine
    f = one - (eight - six)
    g = eight - four - seven - (eight - nine)

    # Digits with 5 segments
    two = (a | c | d | e | g)
    three = (a | c | d | f | g)
    five = (a | b | d | f | g)

    all = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    return int(''.join([str((all.index(digit))) for digit in output_digits]))

def solve(entries):
    return sum([solve_entry(entry) for entry in entries])

print(solve(entries))