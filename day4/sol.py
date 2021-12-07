d = [l.strip() for l in open("./data", "r") if l != "\n"] 

# shape data
grids = []
numbers = d.pop(0).split(',')
for i in range(int(len(d) / 5)):
  grids.append(d[(i*5):(i*5)+5])
for g in grids:
  for i in range(0, 5):
    g[i] = g[i].split()

# part 1
def check_win(grid, idx): # checks a given grid for a bingo win if all numbers up to position idx have been called
  for f in range(len(grid[0])):
    if all(i in numbers[0:idx] for i in grid[f]) or all(i in numbers[0:idx] for i in [grid[x][f] for x in range(0, 5)]):
      return True

def find_winner(): # returns [winning grid, index of final called number]. assumption: there is always a winning grid
  for i in range(1, len(numbers)):
    for j in range(len(grids)):
      if check_win(grids[j], i):
        return [grids[j], i]

r = find_winner()
wgrid = r[0] # winning grid
cnum = numbers[0:r[1]] # list of all numbers that were called
unmarked_sum = sum([int(wgrid[i][j]) for i in range(0, 5) for j in range(0, 5) if wgrid[i][j] not in cnum]) # hail satan
print(str(int(cnum[len(cnum)-1]) * unmarked_sum))