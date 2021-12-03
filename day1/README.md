# AOC day 1

## Puzzle 1

### (1) Information

- The submarine makes a sonar sweep of the sea floor, which is the input of the puzzle
- With the sonar sweep it can measure the depth of the sea floor
- The depth is the data we use for the first puzzle
- We want to know **how many measurements are deeper than the previous measurement**

### (1) Question

_How many measurements are larger than the previous measurement?_

### (1) Example data

```text
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
```

Here you can see that there are 7 measurements deeper/larger than the previous.

### (1) Data

- The data is plain text containing 2000 data points, without the increased/decreased information
- It can be found on <https://adventofcode.com/2021/day/1/input>
- In the project it's saved in the `day1_data.txt` file

### (1) Strategy

- Create a simple Python script that reads the data
- Loop over the data and determine if the current measurement is higher than the previous
- The script can be found in `puzzle1.py`

### (1) Answer

- The number of measurements that are larger than the previous: 1448

---

## Puzzle 2

### (2) Information

- The single measurements weren't very useful due to noise
- Changing towards a three-measurement sliding window
- Take 3 measurements and compare them to the next (partially overlapping) 3 measurements

### (2) Question

_Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?_

### (2) Example data

```text
199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
```

### (2) Data

- The same as puzzle 1

### (2) Strategy

- First calculate all the 3 measurement windows and make a new list
- Then compare the new list like in puzzle 1
- The script can be found in `puzzle2.py`

### (2) Answer

- The number of sums larger than the previous sum: 1471
