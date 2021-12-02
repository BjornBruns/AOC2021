#!/usr/bin/env python3

import re

data_file_name = "puzzle2_data.txt"

with open(data_file_name, 'r') as file:
    directions = [line for line in file]

aim_count = 0
horizontal_count = 0
depth_count = 0

for direction in directions:
    magnitude = int(re.search(r'\d+', direction).group())

    if "down" in direction:
        aim_count += magnitude
    elif "up" in direction:
        aim_count -= magnitude
    elif "forward" in direction:
        horizontal_count += magnitude
        depth_count += (aim_count * magnitude)
        

print(f"Aim: {aim_count}, horizontal: {horizontal_count}, depth: {depth_count} = {horizontal_count}*{depth_count} = {horizontal_count * depth_count}")