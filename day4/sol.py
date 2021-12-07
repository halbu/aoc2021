d = [l.strip() for l in open("./data", "r") if l != "\n"] 

# shape data
grids = []
numbers = d.pop(0).split(',')
for i in range(int(len(d) / 5)):
  grids.append(d[(i*5):(i*5)+5])
for g in grids:
  for i in range(0, 5):
    g[i] = g[i].split()

def check_win(grid, idx): # checks a given grid for a bingo win if all numbers up to index position idx (inclusive) have been called
  for f in range(len(grid[0])):
    if all(i in numbers[0:idx+1] for i in grid[f]) or all(i in numbers[0:idx+1] for i in [grid[x][f] for x in range(0, 5)]):
      return True

def find_winner(): # returns [index of winning grid, index of final called number]. assumption: there is always a winning grid
  for i in range(1, len(numbers)):
    for j in range(len(grids)):
      if check_win(grids[j], i):
        return [j, i]

def eval_score(grid, idx):
  unmarked_sum = sum([int(grid[i][j]) for i in range(0, 5) for j in range(0, 5) if grid[i][j] not in numbers[0:idx+1]])
  return int(numbers[idx]) * unmarked_sum

# part 1
r = find_winner()
print(eval_score(grids[r[0]], r[1]))

# part 2 
while True:
  result = find_winner()      # this is really inefficient as we start looking for
  if (len(grids) > 1):        # wins from called_number index 0 again after each
    grids.pop(result[0])      # pop, but perf is not bad enough (yet!) for me to care
  else:
    print(eval_score(grids[0], result[1]))
    break