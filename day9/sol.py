d = [list(l.strip('\n')) for l in open("./data", "r")]
b = [['.' for y in d[0]] for x in d] # matching grid to hold basin indices
q = [] # queue nodes

# part 1
def lower_n(x, y): # returns True if any neighbouring number is equal or lower
  for dir in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
    if x + dir[0] >= 0 and x + dir[0] < len(d) and y + dir[1] >= 0 and y + dir[1] < len(d[0]):
      if d[x + dir[0]][y + dir[1]] <= d[x][y]:
        return True

print(sum([int(d[x][y]) + 1 for x in range(len(d)) for y in range(len(d[0])) if not lower_n(x, y)]))

# part 2. let's start with a few convenience functions
def val(p):
  return d[p[0]][p[1]]

def on_grid(x, y):
  return (x >= 0 and x < len(d) and y >= 0 and y < len(d[0]))

def get_ns(x, y):
  return [[x + dir[0], y + dir[1] ] for dir in [[0, -1], [1, 0], [0, 1], [-1, 0]] if on_grid(x + dir[0], y + dir[1])]

basin_index = 0 # the main recursive mark and search nodes bit
for p in [[x, y] for x in range(len(d)) for y in range(len(d[0])) if not lower_n(x, y)]:
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