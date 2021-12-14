d = [l.strip("\n") for l in open("./data", "r") if l != '\n']
pol, rules = d.pop(0), d
R, P, C = {}, {}, {}

for i in range(1, len(pol)): # parse polymer pairs into pair map
  P[pol[i-1:i+1]] = 1 if pol[i-1:i+1] not in P else P[pol[i-1:i+1]] + 1

for i in list(pol): # parse polymer chars into char map
  C[i] = 1 if i not in C else C[i] + 1

for rule in rules: # parse pair insertion rules into the rule map
  r = rule.split(' -> ')
  R[r[0]] = {'p1': r[0][0] + r[1], 'p2': r[1] + r[0][1], 'c': r[1]}

def iterate():
  for p in [{'d': x, 'p1': R[x]['p1'], 'p2': R[x]['p2'], 'c': R[x]['c'], 'n': P[x]} for x in list(P.keys())]:
    P[p['p1']] = p['n'] if p['p1'] not in P else P[p['p1']] + p['n']  # update the pairs map
    P[p['p2']] = p['n'] if p['p2'] not in P else P[p['p2']] + p['n']  # to add the two new pairs...
    P[p['d']] -= p['n']                                               # ...and remove the pair that was split
    C[p['c']] = p['n'] if p['c'] not in C else C[p['c']] + p['n']     # add the new char to the chars map

[iterate() for i in range(10)]
print(max(list(C.values())) - min(list(C.values())))

[iterate() for i in range(30)]
print(max(list(C.values())) - min(list(C.values())))