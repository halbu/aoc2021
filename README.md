# aoc2021

### Solutions for Advent of Code 2021

My primary aim is to produce solutions which are correct and as compact as possible while remaining reasonably performant.

To this end some practices are adopted here which would be avoided in other circumstances:

* Variables are given abbreviated or one-character names e.g. the variable holding the data for each day's problem is typically named `d`

* List comprehensions are used solely for side-effects in order to produce shorter solutions in terms of sloc

For example,

`[bits[j].append(int(i[j])) for i in d for j in range(len(i))]`

is preferred over

```
for i in d:
  for j in range(len(i)):
    bits[j].append(int(i[j]))
```
    
* Some crimes against readability and formatting have been committed
