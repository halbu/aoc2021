import heapq
d, q = [[int(i) for i in list(l.strip("\n"))] for l in open("./data", "r") if l != '\n'], []
M = {(0, 0): (0, None)} # dict of locs, key = tuple of loc, vals = tuple of best (present) cost and parent

def ok(x, y): return x >= 0 and x < len(d) and y >= 0 and y < len(d[0])
def risk(p): return d[p[0]][p[1]]
def get_ns(n): return [(n[0] + d[0], n[1] + d[1]) for d in [[0, -1], [1, 0], [0, 1], [-1, 0]] if ok(n[0] + d[0], n[1] + d[1])]
def euclid(n): return ((n[0] - goal[0])**2 + (n[1] - goal[1])**2)**.5
def heuristic(loc): return M[loc][0] + euclid(n)
def inc(i, v): return i + v if (i + v) < 10 else ((i + v) - 9)
def is_queued(n): return any([True for e in q if e[1] == n])

if (True): # false leaves the risk grid as-is for part 1, true expands it to produce the answer for part 2
  nd = [[0 for i in range(len(d) * 5)] for j in range(len(d[0])*5)]

  for i in range(5):
    for x in range(len(d)):
      for y in range(len(d)):
        nd[x][len(d)*i + y] = inc(d[x][y], i)

  for i in range(1, 5):
    for x in range(len(d)):
      for y in range(len(nd)):
        nd[len(d)*(i) + x][y] = inc(nd[x][y], i)

  d = nd

goal = (len(d)-1, len(d[0])-1)
heapq.heappush(q, (0, (0, 0)))

while len(q) > 0:
  c_loc = heapq.heappop(q)[1]
  c_cost = M[c_loc][0]

  if (c_loc == goal):
    print(c_cost)
    exit()

  M[c_loc] = (c_cost, c_loc)

  for n in get_ns(c_loc):
    cost_of_this_path = c_cost + risk(n)
    if n in M.keys():
      n_cost = M[n][0]
      if not (n_cost > cost_of_this_path): continue
    M[n] = (cost_of_this_path, c_loc)
    heapq.heappush(q, (heuristic(n), n))