# AOC day 3

## Puzzle 1

### (1) Information

- The submarine makes creaking noises, so we'll take a look at the diagnostics report
- The report is a list of binary numbers which can be decoded to the power consumption
- The power consumption is made up out of two binary numbers the `gamma rate` and `epsilon rate`
- The `gamma rate` is determined by looking at the most common bit at each position, this results in a single binary number which can be transformed to a decimal number
- The `epsilon rate` is determined by doing the same but for the least common bit at each position
- The power consumption is determined by multiplying those two decimals
- We want to know **what the power consumption of the submarine is**

### (1) Question

_What is the power consumption of the submarine?_

### (1) Example data

```text
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
```

Here at the first position the most common bit is 1, in the second position it's 0. All positions combined is `10110`, or `22` in decimal. That is the `gamma rate`. The epsilon rate is `01001`, or `9` is decimal. This results in a power consumption of `198`.

### (1) Data

- The data is plain text containing 1000 data points
- It can be found on <https://adventofcode.com/2021/day/3/input>
- In the project it's saved in the `day3_data.txt` file

### (1) Strategy

- Create a simple Python script that reads the data
- Read every line and split into seprate bits (list of characters)
- Transpose the list of lists
- Look at the most common element in each list
- Create a binary string from these elements (and flip 1s and 0s for epsilon) and convert to decimal
- Multiply the decimals
- The script can be found in `puzzle1.py`

### (1) Answer

- The power consumption is: `3958484`

---

## Puzzle 2

### (2) Information

- The next step is to determine the `life support rating` which is the multiplication of the `oxygen generator rating` and the `CO2 scrubber rating`
- These ratings can be found in the same data
- The ratings are determined by filtering out values until a single value remains
- For the `oxygen generator rating`, look at the most common element for the first bit position and only keep the number with that value at the first position. Then do the same for second position, third, fourth, etc.
- Do this until a single binary number remains and convert to decimal
- Do the same for the least common element for the `CO2 scrubber rating`
- If `1` and `0` occurence is equal, use `1` for oxygen and `0` for CO2
- These decimals mulitplied is the `life support rating`

### (2) Question

_What is the life support rating of the submarine?_

### (2) Example data

Same as first puzzle.

### (2) Data

Same as first puzzle.

### (2) Strategy

- Create a simple Python script that reads the data
- Read every line and split into seprate bits (list of characters)
- Transpose the list of lists
- Look at the most and least common element in each list
- Create a binary string from these elements and convert to decimal
- Multiply the decimals
- The script can be found in `puzzle2.py`

### (2) Answer

- The oxygen rating is `2397` and the CO2 rating `673`, multiplied this is: `1613181`
