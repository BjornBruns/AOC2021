# AOC day 7

## Puzzle 1

### (1) Information

- Oh no! A giant whale decided to attack the submarine, but luckily there is a swarm of crabs in tiny submarines that wants to help by blasting a giant hole in the ocean floor for our submarine to go into
- All crabs have a horizontal position (number, the puzzle input) and they all have to be aligned at the same position to have enough power to blast a large enough hole for the submarine
- It doesn't matter on which position they align, but they have limited fuel, so they want to position that takes the least number of positions moved

### (1) Question

_Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?_

### (1) Example data

```text
16,1,2,0,4,2,7,1,2,14
```

```text
Move from 16 to 2: 14 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 0 to 2: 2 fuel
Move from 4 to 2: 2 fuel
Move from 2 to 2: 0 fuel
Move from 7 to 2: 5 fuel
Move from 1 to 2: 1 fuel
Move from 2 to 2: 0 fuel
Move from 14 to 2: 12 fuel
```

In this example, the cheapest possible outcome (all to position `2`) costs `37` fuel.

### (1) Data

- The data is plain text containing a single line with X number values
- Each value represents the position of a crab
- It can be found on <https://adventofcode.com/2021/day/7/input>
- In the project it's saved in the `day7_data.txt` file

### (1) Strategy

- Create a Python script that reads in the values as a list of integers
- Determine the median position of all positions
- Calculate the fuel that is required to get each crab to that position
- The script can be found in `python/puzzle1.py`

### (1) Answer

- The least required fuel to all align at the same position is: `339321`

---

## Puzzle 2

### (2) Information

- Instead of 1 fuel per position changed, the fuel used increases with 1 for every additional position change, i.e. fuel for 1 position change is 1, for 2 it's 3, for 3 it's 6, for 4 it's 10

### (2) Question

_Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?_

### (2) Strategy

- The median can't be used as the final location anymore
- The fuel use is a sequence of triangular numbers (1, 3, 6, 10, 15), write function to calculate the fuel use between 2 points
- The chosen position is between the minimum and maximum position of the crabs
- Create a dictionary with the number of crabs of a certain position
- Loop over all possible positions and calculate the fuel necessary to get from all other positions to that possible position, save the fuel necessary
- Take the minimum value of the fuel necessary to reach the possible positions
- The script can be found in `python/puzzle2.py`

### (2) Answer

- The least required fuel to all align at the same position is: `95476244`
