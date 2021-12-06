# AOC day 4

## Puzzle 1

### (1) Information

- The submarine is almost 1.5km below the sea surface, where there's no more sunlight
- But, there is a giant squid outside the submarine that wants to play bingo.
- Bingo is played on a 5x5 grid of numbers, numbers are randomly called and markde
- A fully marked row or column means you win
- The score of the board is calculated by taking the sum of the unmarked numbers times the last called number

### (1) Question

_To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?_

### (1) Example data

```text
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
```

Here at the first position the most common bit is 1, in the second position it's 0. All positions combined is `10110`, or `22` in decimal. That is the `gamma rate`. The epsilon rate is `01001`, or `9` is decimal. This results in a power consumption of `198`.

### (1) Data

- The data is plain text with the first row containing the number called and below there are boards
- It can be found on <https://adventofcode.com/2021/day/4/input>
- In the project it's saved in the `day4_data.txt` file

### (1) Strategy

- Create a Python script that reads in all data as a string
- Take the first line, split on each `,` and that are the numbers called
- Create a class to contain a board with a list of lists containing tuples of numbers and a boolean (marked: true/false)
- The data set can be split on double newlines `\n\n` to only have single board inputs
- Split the board input per line, split on whitespace(s) and you have a list of numbers that can be mapped to tuples
- Write three methods for the board objects `call_number(number)`, `is_finished() -> bool`, and `calculate_score() -> int`
- Make board objects for all the input
- Iterate over the called numbers, call the number for each board and determine whether is board is finished, if so, calculate the score
- The script can be found in `python/puzzles.py`

### (1) Answer

- The score of the winning board is: `5685`

---

## Puzzle 2

### (2) Information

- You don't want to win, but you want to let the giant squid win
- Therefore, you need to know which board wins last

### (2) Question

_Figure out which board will win last. Once it wins, what would its final score be?_

### (2) Strategy

- Do the same as for the first puzzle, but keep track of the boards that haven't been finished yet
- When a board finishes, print its score
- The last board to finish, has the score as the answer
- The script can be found in `python/puzzles.py`

### (2) Answer

- The score of the losing board is: `21070`
