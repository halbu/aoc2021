d = [(l.strip('\n')) for l in open("./data", "r")]
o = ['(', '[', '{', '<']
c = [')', ']', '}', '>']
I = {')': '(', ']': '[', '}': '{', '>': '<', '(': ')', '[': ']', '{': '}', '<': '>' }
S1 = {')': 3, ']': 57, '}': 1197, '>': 25137 }
S2 = {')': 1, ']': 2, '}': 3, '>': 4 }

# part 1
def eval_score(l):
  ecc = [] # expected closure characters
  for i in range(len(l)):
    if l[i] in o:
      ecc.append(l[i])
    else:
      if ecc[len(ecc) - 1] != I[l[i]]:
        return S1[l[i]]
      else:
        ecc.pop()

print(sum([eval_score(l) for l in d if eval_score(l) is not None]))

# part 2....
def is_cor(l): # test string for corruption
  return eval_score(l) != None

def is_inc(l): # test string for incompleteness
  os = sum([1 for e in list(l) if e in o])
  cs = sum([1 for e in list(l) if e in c])
  return os != cs

def find_pair(l, i):
  for j in range(i, -1, -1):
    if I[l[i]] == l[j]:
      return [j, i] # [opener, closer]

def gen_comp(l): # generate a completion string for incomplete string `l`
  # while the list has closures in it
  while sum([1 for e in l if e in c]) > 0:
    # walk the list until we find the next closure
    found = False
    for i in range(len(l)):
      if not found:
        if l[i] in c:
          # go backward from there until we hit its opening pair and pop them both
          oc = find_pair(l, i)
          found = True
          l.pop(oc[1])
          l.pop(oc[0])

  return [I[e] for e in [l[x] for x in range(len(l)-1, -1, -1)]]

def get_score(l):
  score = 0
  for i in list(l):
    score = (score * 5) + S2[i]
  return score

scores = [get_score(gen_comp(list(l))) for l in [l for l in d if is_inc(l) and not is_cor(l)]]
scores.sort()
print(scores[int(len(scores) / 2)])