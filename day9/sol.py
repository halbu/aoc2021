d = [list(l.strip('\n')) for l in open("./data", "r")]

# part 1
def lower_n(x, y): # returns True if any neighbouring number is equal or lower
  for dir in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
    if x + dir[0] >= 0 and x + dir[0] < len(d) and y + dir[1] >= 0 and y + dir[1] < len(d[0]):
      if d[x + dir[0]][y + dir[1]] <= d[x][y]:
        return True

print(sum([int(d[x][y]) + 1 for x in range(len(d)) for y in range(len(d[0])) if not lower_n(x, y)]))