# AOC day 9

## Puzzle 1

### (1) Information

- The caves we're in are lava tubes, with even some hydrothermal vents producing smoke inside, we want to avoid this to be safer
- The submarine generates a heightmap of the floor of the nearby caves (puzzle input)
- The smoke flows to the lowest point of the area it's in, with each number of the map corresponding to the height of a location
- Low points are location where all adjacent (up, down, left and right) locations are higher
- The risk level of a low point is 1 plus its height

### (1) Question

_Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?_

### (1) Example data

```text
2199943210
3987894921
9856789892
8767896789
9899965678
```

There are four low points here, on the first row (a `1` and `0`), on the thrird row (a `5`), and on the last row (a `5`). The risk levels are `2`, `1`, `6`, and `6`. The sum is `15`.

### (1) Data

- The data is plain text, 100 lines with 100 numbers per line
- It can be found on <https://adventofcode.com/2021/day/9/input>
- In the project it's saved in the `day9_data.txt` file

### (1) Strategy

- Create a Python script that reads in the height map matrix
- Option 1: Loop over all rows and save indices of all local minima in the row (don't consider column)
- Option 1: Loop over all columns and save indices of all local minima in the column (don't consider row)
- Option 1: If index is both row and column minimum, then it's a local minimum
- Option 2: Loop over all the elements, compare against all surrounding elements and add as minimum if it's lower than all
- Sum all the minima + the number of minima
- The script can be found in `python/puzzle1.py`

### (1) Answer

- The sum of the risk levels of all low points on the heightmap is: `423`

---

## Puzzle 2

### (2) Information

- Instead of searching for local minima, the `9` heights are the borders of basins
- Search for the three largest basins (i.e. connected heights between `0` and `8`)
- Multiply the three largest basins

### (2) Question

_What do you get if you multiply together the sizes of the three largest basins?_

### (2) Strategy

- Create a Python script that reads in the height map matrix, map all `9` heights to `0` and all other values to `1`
- Loop over the matrix, and keep track in other "visited" matrix whether that value has already been visited
- When visiting a value, recursively visit the neighbors of that value (keep track in visited matrix) and count how many values are visited (make sure to not count heights that are `0` or already visited values)
- When the visited value has recursively visited all neighbors, return the count of that basin
- Proceed to the next value, but skip already visited values
- When the whole map has been iterated over, return the counts, sort and multiply the three largest
- The script can be found in `python/puzzle2.py`

### (2) Answer

- The product of the three largest basins on the heightmap is: `1198704`
