d = [l.strip() for l in open("./data", "r") if l != "\n"][0]
ix = 0

def B(hex): return bin(int(hex, 16))[2:].zfill(4)
def get_bits(bstr): return ''.join([B(i) for i in list(bstr)])
binary = get_bits(d)

def parse_literal(bstr):
  literal_length_in_bits = 0
  while True:
    literal_length_in_bits += 5
    if (bstr[0] == '1'):
      bstr = bstr[5:]
    else: return literal_length_in_bits

def parse_transmission(vsum):
  global ix
  if not any([True for i in list(binary[ix:]) if i == '1']):
    print(str(vsum))
    exit()

  version = int(binary[ix:ix+3], 2)   # read in version and
  typeid = int(binary[ix+3:ix+6], 2)  # type ID from header
  ix += 6

  if typeid == 4: # it's a literal packet
    ix += parse_literal(binary[ix:])
    parse_transmission(vsum + version)
  else: # it's an operator packet
    ix += 16 if binary[ix] == '0' else 12
    parse_transmission(vsum + version)

parse_transmission(0)