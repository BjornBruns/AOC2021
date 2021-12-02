#!/usr/bin/env python3

import re

data_file_name = "puzzle2_data.txt"

with open(data_file_name, 'r') as file:
    directions = [line for line in file]

down_count = 0
up_count = 0
forwards_count = 0

for direction in directions:
    magnitude = int(re.search(r'\d+', direction).group())

    if "down" in direction:
        down_count += magnitude
    elif "up" in direction:
        up_count += magnitude
    elif "forward" in direction:
        forwards_count += magnitude

print(f"Up: {up_count}, down: {down_count}, forward: {forwards_count} = {forwards_count}*({down_count}-{up_count}) = {forwards_count * (down_count-up_count)}")