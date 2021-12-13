d = [{'S':x[0], 'E':x[1]} for x in [l.strip("\n").split("-") for l in open("./data", "r")]]
M, q = {}, []

# part 1
for edge in d: # create a map of all vertices & connecting edges
  if edge['S'] not in M.keys(): M[edge['S']] = []
  if edge['E'] not in M.keys(): M[edge['E']] = []
  M[edge['S']].append(edge['E'])
  M[edge['E']].append(edge['S'])

q.append(['start']) # recursively add valid neighbours & enqueue new lists
count = 0
while len(q) > 0:
  c = q.pop()
  for v in [n for n in M[c[len(c)-1]] if n not in c or n[0].isupper()]:
    if v != 'end': q.append(c + [v])
    else: count = count + 1

print(count)