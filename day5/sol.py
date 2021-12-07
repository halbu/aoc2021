d = [l.strip() for l in open("./data", "r") if l != "\n"] 
lines = grid = []

for l in d:
  points = l.split(" -> ")
  o = points[0].split(',') # origin
  t = points[1].split(',') # target
  lines.append({'x1': int(o[0]), 'y1': int(o[1]), 'x2': int(t[0]), 'y2': int(t[1])})

def plot_line(l):
  step = [0, 0]
  if l['x1'] > l['x2']:
    step[0] = -1
  elif l['x1'] < l['x2']:
    step[0] = 1

  if l['y1'] > l['y2']:
    step[1] = -1
  elif l['y1'] < l['y2']:
    step[1] = 1

  x = l['x1']
  y = l['y1']
  
  while not (x == l['x2'] and y == l['y2']):
    grid[x][y] += 1
    x += step[0]
    y += step[1]
  grid[x][y] += 1

# part 1
grid = [[0 for i in range(1000)] for j in range(1000)]
[plot_line(l) for l in lines if l['x1'] == l['x2'] or l['y1'] == l['y2']]
print(sum([1 for x in range(0, len(grid)) for y in range(0, len(grid[0])) if grid[x][y] > 1]))

# part 2
grid = [[0 for i in range(1000)] for j in range(1000)]
[plot_line(l) for l in lines]
print(sum([1 for x in range(0, len(grid)) for y in range(0, len(grid[0])) if grid[x][y] > 1]))