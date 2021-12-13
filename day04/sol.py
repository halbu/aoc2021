d = [l.strip() for l in open("./data", "r") if l != "\n"] 

# shape data
nums = d.pop(0).split(',') # bingo numbers in the order that they are called
grids = [d[(i * 5):(i * 5) + 5] for i in range(int(len(d) / 5))] # grids as a list of 5x5 char lists
for g in grids:
  for i in range(5):
    g[i] = g[i].split()

def check_win(g, ix): # checks a grid `g` for a win if all numbers up to index `ix` (inclusive) were called
  for f in range(len(g[0])):
    if all(i in nums[0:ix + 1] for i in g[f]) or all(i in nums[0:ix + 1] for i in [g[x][f] for x in range(5)]):
      return True

def find_winner(): # returns [index of winning grid, index of last called number] or None if no such grid exists
  for i in range(1, len(nums)):
    for j in range(len(grids)):
      if check_win(grids[j], i):
        return [j, i]

def eval_score(g, ix): # return a grid's score given the grid `g` and the index `ix` of the last called number
  return sum([int(g[i][j]) for i in range(5) for j in range(5) if g[i][j] not in nums[0:ix + 1]]) * int(nums[ix])

# part 1
r = find_winner()
print(eval_score(grids[r[0]], r[1]))

# part 2 
while True:
  r = find_winner()       # this is really inefficient as we start looking for
  if (len(grids) > 1):    # wins from called_number index 0 again after each
    grids.pop(r[0])       # pop, but perf is not bad enough (yet!) for me to care
  else:
    print(eval_score(grids[0], r[1]))
    break