d = [int(x) for x in [l for l in open("./data", "r")][0].split(',')]
  
# part 1. let's do it naively first. i'm sure part 2 will call for some optimisation
def cost_to(target):
  return sum([abs(target - pos) for pos in d])

print(min([cost_to(x) for x in range(0, max(d))]))
  
# part 2 - well ok then i guess it doesn't!
def sum_of_n_ints(dist):
  return int((dist * (dist + 1)) / 2)

def new_cost_to(target):
  return sum([sum_of_n_ints(abs(target - pos)) for pos in d])

print(min([new_cost_to(x) for x in range(0, max(d))]))