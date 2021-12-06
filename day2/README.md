# AOC day 2

## Puzzle 1

### (1) Information

- The submarine can be controller via series of commands `forward 1`, `down 2`, or `up 3`
- These increase/decrease the horizontal position or depth by X units
- We want to know **how many measurements are deeper than the previous measurement**

### (1) Question

_What do you get if you multiply your final horizontal position by your final depth?_

### (1) Example data

```text
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

Here you can see that the total horizontal position is 15 and the total depth is 10, multipplied this is 150.

### (1) Data

- The data is plain text containing 1000 data points
- It can be found on <https://adventofcode.com/2021/day/2/input>
- In the project it's saved in the `day2_data.txt` file

### (1) Strategy

- Create a simple Python script that reads the data
- Create 3 counters (or a dict) that stores the count of each of the directions
- Read the string and then the integer in each data point to assign the count
- The script can be found in `python/puzzle1.py`

### (1) Answer

- The number forward count is `1970` and the down minus up count is `916`, multiplied this is: `1804520`

---

## Puzzle 2

### (2) Information

- The directions make no sense, apparently they are a biy more complicated than this
- There is a third direction called `aim`
- Also, `down` increases your aim, `up` decreases your aim, and `forward` increases the horizontal position and increases the depth by your `aim` multiplied by `X`

### (2) Question

_What do you get if you multiply your final horizontal position by your final depth?_

### (2) Example

```text
forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
```

### (2) Strategy

- Loop over the data
- Create three counters: `aim`, `horizontal` and `depth`
- Multiply the horizontal position with the depth
- The script can be found in `python/puzzle2.py`

### (2) Answer

- The new horizontal count is `1970` and the depth count is `1000556`, multiplied this is: `1971095320`
