d = [l.strip() for l in open("./data", "r") if l != "\n"] 

def filter_by_bit_criteria(my_list, pos, most_common):
  ones = zeroes = desired_bit = 0
  for e in my_list:
    if e[pos] == '1':
      ones += 1
    else:
      zeroes += 1

  if (ones >= zeroes):
    desired_bit = 1
  if most_common == False:
    desired_bit = 1 - desired_bit

  return [e for e in my_list if int(e[pos]) == desired_bit]

def find_rating(my_list, most_common):
  pos = 0
  while len(my_list) > 1:
    my_list = filter_by_bit_criteria(my_list, pos, most_common)
    pos += 1
  return my_list[0]

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

epsilon = ''.join(['1' if e == '0' else '0' for e in list(gamma)]) # flip bits to get epsilon
print(int(gamma, base=2) * int(epsilon, base=2)) # convert binary strs to decimal & multiply

# part 2
o2_rating = find_rating(d, True)
co2_rating = find_rating(d, False)
print(int(o2_rating, base=2) * int(co2_rating, base=2))