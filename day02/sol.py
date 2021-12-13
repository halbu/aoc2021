d = [[e[0], int(e[1])] for e in [l.split() for l in open("./data", "r")]]

# part 1
print(sum([i[1] for i in d if i[0][0] == 'f']) * sum([-i[1] if i[0] == 'up' else i[1] if i[0] == 'down' else 0 for i in d]))

# part 2. let's swallow our pride and use a for loop
aim = depth = position = 0
for e in d:
  if e[0] == 'up':
    aim = aim - e[1]
  if e[0] == 'down':
    aim = aim + e[1]
  if e[0] == 'forward':
    position = position + e[1]
    depth = depth + (aim * e[1])

print(position * depth)
