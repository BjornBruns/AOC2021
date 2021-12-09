#!/usr/bin/env python3

import re
from collections import defaultdict

data_file_name = "../day5_data.txt"

# Helper functions
def bresenham(x0, y0, x1, y1):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.

    FROM: https://github.com/encukou/bresenham/blob/master/bresenham.py
    """
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

# Main content
with open(data_file_name, 'r') as file:
    lines = []
    for line in file:
        numbers = re.findall(r"\d+", line) # Get the numbers on a single line of the file
        lines.append(list(bresenham(int(numbers[0]), numbers[1], numbers[2], numbers[3]))) # Determine all the points between the first and last point

def is_straight_line(line):
    """ Considers first and list point of the line. Either the x values or the y values are the same."""
    first = line[0]
    last = line[-1]
    return True if first[0] == last[0] or first[1] == last[1] else False

def get_overlapping_lines_count(include_diagonals = False):
    """ Adds all points of a line to a dictionary and counts the number of times the point was added
        If a point has been added more than once, there is an overlap between lines"""
    points_dict = defaultdict(lambda: 0)

    for line in lines:
        if include_diagonals or is_straight_line(line):
            for point in line:
                points_dict[point] += 1

    return sum(map(lambda x: x>1, list(points_dict.values())))

print(get_overlapping_lines_count())
print(get_overlapping_lines_count(True))
