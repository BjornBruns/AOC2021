#!/usr/bin/env python3

data_file_name = "puzzle1_data.txt"

with open(data_file_name, 'r') as file:
    depth_measurements = [int(line.rstrip()) for line in file]

sliding_measurements = []

for i, measurement in enumerate(depth_measurements):
    if i < 2: # Guard against index out of bounds
        continue

    minus_2 = depth_measurements[i-2]
    minus_1 = depth_measurements[i-1]

    sliding_measurements.append(measurement + minus_1 + minus_2)

# Same logic as puzzle 1
deeper_count = 0
for i, measurement in enumerate(sliding_measurements):
    if i < 1: # Guard against index out of bounds
        continue

    if measurement > sliding_measurements[i - 1]:
        deeper_count += 1

print(deeper_count)