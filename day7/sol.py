d = [int(x) for x in [l for l in open("./data", "r")][0].split(',')]
  
# part 1. let's do it naively first. i'm sure part 2 will call for some optimisation
def cost_to(target):
  return sum([abs(target - p) for p in d])
print(min([cost_to(x) for x in range(0, max(d))]))

# part 2 - well ok then i guess it doesn't!
def new_cost_to(target):
  return int(sum([(lambda x:(x*(x+1)/2))(abs(target - p)) for p in d]))
print(min([new_cost_to(x) for x in range(0, max(d))]))