d = [l.strip() for l in open("./data", "r") if l != "\n"] 

# part 1
bits = [[] for i in range(len(d[0]))]
[bits[j].append(int(i[j])) for i in d for j in range(len(i))]
g = ''.join(['1' if i.count(1) > i.count(0) else '0' for i in bits]) # gamma
e = ''.join(['1' if e == '0' else '0' for e in list(g)]) # flip bits to get epsilon
print(int(g, base=2) * int(e, base=2)) # convert binary strs to decimal & multiply

# part 2
def filter_by_bit_criteria(my_list, pos, most_common):
  b1 = sum([1 for e in my_list if e[pos] == '1']) # count of 1 bits
  b0 = sum([1 for e in my_list if e[pos] == '0']) # count of 0 bits
  bt = (1 if b1 >= b0 else 0) if most_common else 1 - (1 if b1 >= b0 else 0) # target bit
  return [e for e in my_list if int(e[pos]) == bt]

def find_rating(my_list, most_common):
  pos = 0
  while len(my_list) > 1:
    my_list = filter_by_bit_criteria(my_list, pos, most_common)
    pos += 1
  return my_list[0]
  
print(int(find_rating(d, True), base=2) * int(find_rating(d, False), base=2))