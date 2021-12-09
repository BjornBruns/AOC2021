#!/usr/bin/env python3

from collections import defaultdict

data_file_name = "../day6_data.txt"

with open(data_file_name, 'r') as file:
    fish_list = [int(fish) for fish in file.read().split(',')]

def tick():
    new_fish = []
    for i, fish in enumerate(fish_list):
        if fish == 0:
            fish_list[i] = 6
            new_fish.append(8)
        else:
            fish_list[i] -= 1
    fish_list.extend(new_fish)

for i in range(80):
    tick()

print(len(fish_list))