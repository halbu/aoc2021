d = [l.strip() for l in open("./data", "r") if l != "\n"] 

# part 1
bits = [[] for i in range(len(d[0]))]
[bits[j].append(int(i[j])) for i in d for j in range(len(i))]
g = ''.join(['1' if i.count(1) > i.count(0) else '0' for i in bits]) # gamma
e = ''.join(['1' if e == '0' else '0' for e in list(g)]) # flip bits to get epsilon
print(int(g, base=2) * int(e, base=2)) # convert binary strs to decimal & multiply

# part 2
def filter_by_bit_criteria(l, i, most_common):
  less_zeroes = sum([1 for e in l if e[i] == '1']) >= sum([1 for e in l if e[i] == '0'])
  target_bit = (1 if less_zeroes else 0) if most_common else 1 - (1 if less_zeroes else 0)
  return [e for e in l if int(e[i]) == target_bit]

def find_rating(l, most_common):
  i = 0
  while len(l) > 1:
    l = filter_by_bit_criteria(l, i, most_common)
    i += 1
  return l[0]
  
print(int(find_rating(d, True), base=2) * int(find_rating(d, False), base=2))