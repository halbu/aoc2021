d = [int(l) for l in open("./data", "r")]

# part 1
print(sum([1 for x in range (1, len(d)) if d[x] > d[x-1]]))

# part 2
print(sum([1 for x in range (3, len(d)) if sum(d[x-2:x+1]) > sum(d[x-3:x])]))