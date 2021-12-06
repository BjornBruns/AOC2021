# AOC day 6

## Puzzle 1

### (1) Information

- The sea floor is getting steeper and suddenly we see many lanternfish, they seem to spawn really quickly, perhaps even exponentially
- Each lanternfish creates a new lanternfish every `7` days
- The fish aren't synced in this behavior, one might have `2` days left before it creates a new one, whereas the other might have `4` days left
- Therefore, each fish can be represented as a single number
- New fish need 2 additional days before they're creating new fish
- Example fish' timer (day by day): `3`, `2`, `1`, `0`, `6` (+ new fish with `8`), `5` (second fish' timer: `7`)
- The submarine produces a list with 100 nearby lanternfish (puzzle input)

### (1) Question

_Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?_

### (1) Example data

```text
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
```

In this example, there are `26` fish after 18 days. After 80 days there would be `5934` fish.

### (1) Data

- The data is plain text containing a single line with 300 number values
- Each value represents the timer of a single fish
- It can be found on <https://adventofcode.com/2021/day/6/input>
- In the project it's saved in the `day6_data.txt` file

### (1) Strategy

- Create a Python script that reads in the values as a list of integers
- Write a function that decrements the timers and adds new fish to the list
- Call the function 80 times and read the length of the list
- The script can be found in `puzzles.py`

### (1) Answer

- The number of fish after 80 days is: `379414`

---

## Puzzle 2

### (2) Information

- Calculate the number of fish after `256` days

### (2) Question

_How many lanternfish would there be after 256 days?_

### (2) Strategy

- The number of days is now too high to use the same approach as for puzzle 1 (approach takes too long to calculate)
- Instead of expanding the list, track the number of fish in each "age category" (in a dictionary)
- Move all the fish to the next category when a day passes
- Make sure that the fish that go past age `0` go back to age `6` and add new fish to age `8`
- The script can be found in `puzzles.py`

### (2) Answer

- The number of fish after 256 days is: `1705008653296`
