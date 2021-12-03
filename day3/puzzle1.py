#!/usr/bin/env python3

data_file_name = "day3_data.txt"

# Helper functions
def split(word):
    return [char for char in word]

def most_frequent(List):
    return max(set(List), key = List.count)

# Main content
with open(data_file_name, 'r') as file:
    bitlist = [split(line.rstrip()) for line in file]

# From shape [1000, 12] to [12, 1000]
transposed_bitlist = list(map(list, zip(*bitlist)))

# From length 12 character list to strings containing the bits and then to integer (base 2)
gamma_bitstring = ''.join([most_frequent(bitstring) for bitstring in transposed_bitlist])
gamma_rate = int(gamma_bitstring, 2)

epsilon_bitstring = bin(int(''.join('1' if x == '0' else '0' for x in gamma_bitstring), 2)) # Flip 1s and 0s
epsilon_rate = int(epsilon_bitstring, 2)

print(gamma_rate * epsilon_rate)