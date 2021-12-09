#!/usr/bin/env python3

from collections import Counter, defaultdict

data_file_name = "../day6_data.txt"

with open(data_file_name, 'r') as file:
    fish_dict = Counter([int(fish) for fish in file.read().split(',')])

def tick(fish_dict):
    new_dict = defaultdict(int)
    for age_group, count in fish_dict.items():
        if age_group == 0:
            new_dict[6] += count
            new_dict[8] += count
        else: 
            new_dict[age_group - 1] += count
    
    return new_dict

for i in range(256):
    fish_dict = tick(fish_dict)

print(sum(fish_dict.values()))