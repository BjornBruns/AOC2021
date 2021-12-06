# AOC day 5

## Puzzle 1

### (1) Information

- We find some hydrothermal vents on the ocean floor, producing large opque clouds
- The data contains "lines" (the clouds) represented by two points, the start and end of the cloud, e.g. `9,7 -> 7,7`
- The first question only considers horizontal en vertical clouds, meaning either the `x` or `y` value of the both points is the same (straight line)

### (1) Question

_Consider only horizontal and vertical lines. At how many points do at least two lines overlap?_

### (1) Example data

```text
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
```

This can be mapped (only horizontal and vertical) to the following diagram, where 1 means there's a line, 2 means there are two lines at that location.

```text
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
```

In this example there are `5` points where 2 or more lines overlap.

### (1) Data

- The data is plain text containing 500 lines
- Each line of the file contains a cloud/line
- It can be found on <https://adventofcode.com/2021/day/5/input>
- In the project it's saved in the `day5_data.txt` file

### (1) Strategy

- Create a Python script that reads in the file line by line, gets the start and end point from the line
- Use [Bresenham's line algorithm](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm) to determine all integer points between the two points
- Filter out lines that are not straight
- Count the number of times a point was created by the algorithm (e.g. store in dict)
- Count the number of points that were created more than once
- The script can be found in `python/puzzles.py`

### (1) Answer

- The score of the winning board is: `6397`

---

## Puzzle 2

### (2) Information

- Also consider non-straight lines

### (2) Question

_Consider all of the lines. At how many points do at least two lines overlap?_

### (2) Strategy

- Do the same as for the first puzzle, but remove the filtering of straight lines
- The script can be found in `python/puzzles.py`

### (2) Answer

- The score of the losing board is: `22335`
