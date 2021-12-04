#!/usr/bin/env python3

from functools import reduce

data_file_name = "day4_data.txt"

class Board:
    def __init__(self, board_string):
        """ Maps the input string to a matrix containing tuples (int, bool) that represent
            the number and whether it has been marked or not"""
        lines = [line.split() for line in board_string.split('\n')]
        self.matrix = [[(int(number), False) for number in line] for line in lines]

    def __str__(self):
        """Give the board a human-readable representation"""
        return f"{self.matrix[0]}\n{self.matrix[1]}\n{self.matrix[2]}\n{self.matrix[3]}\n{self.matrix[4]}"

    def call_number(self, number):
        """Sets the boolean for the called number to True if present"""
        self.matrix = [[(number_tuple[0], True) if number == number_tuple[0] else number_tuple for number_tuple in line] for line in self.matrix]

    @property
    def is_finished(self):
        """Determines whether a row or column is fully marked"""
        transposed_matrix = list(map(list, zip(*self.matrix)))

        for line in self.matrix:
            if all(number_tuple[1] == True for number_tuple in line):
                return True

        for line in transposed_matrix:
            if all(number_tuple[1] == True for number_tuple in line):
                return True
        return False

    def calculate_score(self, last_call):
        """Sums the unmarked numbers times the last called number"""
        flat_matrix = [numer_tuple for line in self.matrix for numer_tuple in line]
        return last_call * reduce((lambda x, y: x + (y[0] if y[1] == False else 0)), flat_matrix, 0)

#####======== Main content ========#####
with open(data_file_name, 'r') as file:
    puzzle_data = file.read()

# Get list of numbers called
numbers_called = list(map(lambda x: int(x), puzzle_data.split('\n', 1)[0].split(',')))

# Discard first two lines to only get the boards
puzzle_data = puzzle_data.split("\n",2)[2] 

# Generate board objects
boards = [Board(board_string) for board_string in puzzle_data.split("\n\n")]
non_finished_boards = boards.copy()

# Iterate over the called numbers
for call in numbers_called:
    for board in boards:
        board.call_number(call)
        if board.is_finished:
            if board in non_finished_boards:
                print("======= BOARD FINISHED =======")
                print(f"-- Score: {board.calculate_score(call)}\n")
                # print(board)

                non_finished_boards.remove(board)
                print(f"\nNon-finished boards remaining: {len(non_finished_boards)}\n")

                if len(non_finished_boards) == 0:
                    exit()