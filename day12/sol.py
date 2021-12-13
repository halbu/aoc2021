d = [{'S':x[0], 'E':x[1]} for x in [l.strip("\n").split("-") for l in open("./data", "r")]]
M, q = {}, []

def has_no_revisits(l):
  small_caves = [v for v in l if v != 'start' and not v[0].isupper()]
  return len(small_caves) == len(set(small_caves))

def get_valid_neighbours(l):
  if has_no_revisits(l):
    return [n for n in M[c[len(c)-1]] if n != 'start']
  else: return [n for n in M[c[len(c)-1]] if n not in c or n[0].isupper()]

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

# part 2
q.append(['start'])
count = 0
while len(q) > 0:
  c = q.pop()
  for v in get_valid_neighbours(c):
    if v != 'end': q.append(c + [v])
    else: count = count + 1
print(count)