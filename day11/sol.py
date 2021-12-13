d = [[int(x) for x in list(l.strip("\n"))] for l in open("./data", "r")]
q = [] # queue for flashes this step
def valid(x, y): return x >= 0 and x < len(d) and y >= 0 and y < len(d[0])
def val(p): return d[p[0]][p[1]]

def get_ns(x, y): # get neighbouring nodes that are within the grid
  return [[x + d[0], y + d[1]] for d in [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]] if valid(x + d[0], y + d[1])]

def proc():
  flashes = 0
  for y in range(len(d[0])):
    for x in range(len(d)):
      d[x][y] += 1
      if (d[x][y] > 9):
        d[x][y] = 0
        q.append([x, y])

  while len(q) > 0:
    c = q.pop()
    flashes += 1
    d[c[0]][c[1]] = 0
    ns = get_ns(c[0], c[1])
    for n in ns:
      if val(n) == 0: continue
      d[n[0]][n[1]] += 1
      if val(n) > 9:
        d[n[0]][n[1]] = 0
        q.append(n)

  return flashes

total = 0
for i in range(1, 99999):
  flashes = proc()
  if flashes == 100: # part 2
    print('Pt 2 answer: ' + str(i))
    exit() # end part 2
  total += flashes
  if i == 100: print('Pt 1 answer: ' + str(total)) # part 1