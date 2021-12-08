# AOC day 8

## Puzzle 1

### (1) Information

- The entrance to the cave we escaped into collapsed. Sensors indicate another exit at much greater depth, so we have to go there
- The four-digit seven-segmented displays in the submarine are damaged. Uh oh. The displays are rendered by turning on/off any of the seven segements named `a` through `g`.

```text
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```

- The problem is that the wires controlling the segments are connected randomly and it differs for each display
- You might know that only `b` and `g` are turned on, the only digit with 2 segments is `1`. Therefore you know that `b` and `g` should actually be `c` and `f`, but you don't know which one is which yet
- For each display you note down the ten unique signal patterns and then write down toe four digit output value (puzzle input)
- Using these signals you should be able to determine which pattern corresponds to which digit

An example entry in the notes might be:

```text
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
```

- Each entry consists out of 10 unique patterns (the digits), a `|` delimiter and the four digit output value.
- Within an entry, the same (random) wire connections are used
- Because `7` is the only digit that uses three segments, `dab` in the above example means that to render a `7`, signal lines `d`, `a`, and `b` are on
- Because `4` is the only digit that uses four segments, `eafb` means that to render a 4, signal lines `e`, `a`, `f`, and `b` are on
- With this information, you should be able to work out the digits and decode the four digit output

### (1) Question

_In the output values, how many times do digits 1, 4, 7, or 8 appear?_

### (1) Example data

```text
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
```

Counting only digits in the output values (the part after `|` on each line), in the above example, there are `26` instances of digits that use a unique number of segments.

### (1) Data

- The data is plain text, with every line containing the 10 digits and 4 output digits
- Every line has different random connections for the 10 digits
- It can be found on <https://adventofcode.com/2021/day/8/input>
- In the project it's saved in the `day8_data.txt` file

### (1) Strategy

- Create a Python script that reads in 4 output digits of each entry in a single list
- `1` is the only digit with 2 segments, `7` is the only one with 3 segments, `4` is the only one with 4 segments and `8` is the only one with 7 segments
- Count the number of signals with 2, 3, 4 and 7 segments in the output digits (look at the length of the string)
- The script can be found in `python/puzzle1.py`

### (1) Answer

- The number of `1`, `4`, `7` and `8` occurences: `284`

---

## Puzzle 2

### (2) Information

- Instead of only using the digits with a unique number of segments, now consider all
- Use deduction to determine where each segment is for an entry
- Determine the output number for each entry and sum them

### (2) Question

_For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?_

### (2) Strategy

- Create a Python script that reads in the 10 digits and the 4 output digits separately
- You know which signal represents the numbers 1, 4, 7, and 8
- Determine the segments one by one by subtracting digits from eachother (i.e. a segment that is in one segment but isn't in the other one)
- When all segments are known, calculate the output number for the entry and continue
- Sum all the output numbers
- The script can be found in `python/puzzle2.py`

### (2) Answer

- The sum of all output digits is: `973499`
