dt = [list(l.strip('\n')) for l in open("./data", "r")]
b = [['.' for y in dt[0]] for x in dt] # equally sized grid to hold basin indices
q = [] # queue nodes

# part 1
def valid(x, y): # check if a position is valid i.e. it exists in grid space
  return (x >= 0 and x < len(dt) and y >= 0 and y < len(dt[0]))

def lower_n(x, y): # returns True if any neighbouring number is equal or lower
  for d in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
    if valid(x + d[0], y + d[1]) and dt[x + d[0]][y + d[1]] <= dt[x][y]:
        return True

print(sum([int(dt[x][y]) + 1 for x in range(len(dt)) for y in range(len(dt[0])) if not lower_n(x, y)]))

# part 2. let's start with a couple more convenience functions
def val(p):
  return dt[p[0]][p[1]]

def get_ns(x, y): # get neighbouring nodes that are within the grid
  return [[x + d[0], y + d[1]] for d in [[0, -1], [1, 0], [0, 1], [-1, 0]] if valid(x + d[0], y + d[1])]

basin_index = 0 # the main recursive mark and search nodes bit
for p in [[x, y] for x in range(len(dt)) for y in range(len(dt[0])) if not lower_n(x, y)]:
  basin_index += 1
  q.append(p)
  while len(q) > 0:
    c = q.pop()
    b[c[0]][c[1]] = str(basin_index)
    for n in get_ns(c[0], c[1]):
      if val(c) < val(n) and val(n) != '9' and n not in q:
        q.append(n)

sizes = []
for i in range(0, max([int(b[x][y]) for y in range(len(b[0])) for x in range(len(b)) if b[x][y] != '.'])):
  sizes.append(sum([1 for y in range(len(b[0])) for x in range(len(b)) if b[x][y] == str(i)]))

print(eval('*'.join(str(i) for i in sorted(sizes, reverse=True)[:3]))) # bad practise but hey, it's 1 line and that's what counts