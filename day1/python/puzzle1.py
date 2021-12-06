#!/usr/bin/env python3

data_file_name = "../day1_data.txt"

with open(data_file_name, 'r') as file:
    depth_measurements = [int(line.rstrip()) for line in file]

deeper_count = 0
for i, measurement in enumerate(depth_measurements):
    if i < 1:
        continue

    if measurement > depth_measurements[i - 1]:
        deeper_count += 1

print(deeper_count)