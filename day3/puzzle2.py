#!/usr/bin/env python3

import copy

data_file_name = "day3_data.txt"

### Helper functions ###
def split(word):
    return [char for char in word]

def most_frequent(List):
    if List.count('1') == List.count('0'):
        return '1'
    else:
        return max(set(List), key = List.count)


def least_frequent(List):
    if List.count('1') == List.count('0'):
        return '0'
    else:
        return min(set(List), key = List.count)

### Main content ###

with open(data_file_name, 'r') as file:
    bitlist = [split(line.rstrip()) for line in file]

def calculate_rating(common_function):
    bitlist_copy = copy.deepcopy(bitlist) # Don't overwrite original bitlist

    # From shape [1000, 12] to [12, 1000]
    transposed_bitlist = list(map(list, zip(*bitlist_copy)))

    for i in range(len(transposed_bitlist)):
        if len(transposed_bitlist) == 0:
            break
        common = common_function(transposed_bitlist[i])

        bitlist_copy = list(filter(lambda number: number[i] == common, bitlist_copy))
        transposed_bitlist = list(map(list, zip(*bitlist_copy)))

    return int(''.join(bitlist_copy[0]), 2)

# Oxygen generator rating
oxygen_rating = calculate_rating(most_frequent)
print(oxygen_rating)

# CO2 scrubber rating
co2_rating = calculate_rating(least_frequent)
print(co2_rating)

# Multiplication
print(oxygen_rating * co2_rating)