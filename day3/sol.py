d = [l.strip() for l in open("./data", "r") if l != "\n"] 

# part 1
bits = [[] for i in range(len(d[0]))]
gamma = ''

for i in d:
  for j in range(len(i)):
    if i[j] == '1':
      bits[j].append(1)
    else:
      bits[j].append(0)

for i in bits:
  if i.count(1) > i.count(0):
    gamma += '1'
  else:
    gamma += '0'

epsilon = ''.join(['1' if e == '0' else '0' for e in list(gamma)])

print(int(gamma, base=2) * int(epsilon, base=2))