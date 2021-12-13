d, g = [l.strip("\n") for l in open("./data", "r") if l != '\n'], []
points = [[int(p.split(',')[0]), int(p.split(',')[1])] for p in d if p[0:4] != 'fold']
folds = [f.strip('fold along') for f in d if f[0:4] == 'fold']

def merge_y(j, k): # merge row j into row k
  for i in range(len(g)):
    if g[i][j] == '#': g[i][k] = '#'

def merge_x(j, k): # merge column j into column k
  for i in range(len(g[0])):
    if g[j][i] == '#': g[k][i] = '#'

def fold(axis, ix):
  if axis == 'y':
    [merge_y(ix + i, ix - i) for i in range(1, len(g[0]) - ix)]
    for i in range(len(g)):
      g[i] = g[i][:ix]
  
  if axis == 'x':
    [merge_x(ix + i, ix - i) for i in range(1, len(g) - ix)]
    [g.pop() for i in range(ix, len(g))] # python doesn't like `g = g[:ix]` here

# part 1
g = [['.' for y in range(max([p[1] for p in points]) + 1)] for x in range(max([p[0] for p in points]) + 1)]
for p in points:
  g[p[0]][p[1]] = '#'

[fold(f.split('=')[0], int(f.split('=')[1])) for f in folds[0:1]]  
print(sum([1 for x in range(len(g)) for y in range(len(g[0])) if g[x][y] == '#']))

# part 2
[fold(f.split('=')[0], int(f.split('=')[1])) for f in folds[1:]]

for y in range(len(g[0])):
  [print(g[x][y], end="", flush=True) for x in range(len(g))]    
  print()