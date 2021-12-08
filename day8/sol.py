d = [l for l in open("./data", "r")]

# shape data
inputs = []
outputs = []
for l in d:
  t = l.split(' | ')
  inputs.append(t[0].strip('\n').split())
  outputs.append(t[1].strip('\n').split())

# part 1
print(sum(1 for o in [j for i in outputs for j in i] if len(o) in [2, 3, 4, 7]))

# part 2 verbose first pass, doubtless could be streamlined a lot
output_values = []

for i in range(len(inputs)):
  ii = inputs[i]
  oo = outputs[i]
  sig = ['' for i in range(10)]

  # identify the obvious signals first
  sig[1] = [i for i in ii if len(i) == 2][0]
  sig[4] = [i for i in ii if len(i) == 4][0]
  sig[7] = [i for i in ii if len(i) == 3][0]
  sig[8] = [i for i in ii if len(i) == 7][0]

  # all signals with 5 wires contain the D segment, so obtain a list of those possibilities
  sig[5] = [i for i in ii if len(i) == 5]
  possible_d_wires = set(sig[5][0])
  for s in sig[5][1:]:
    possible_d_wires.intersection_update(s)

  # the true D wire is the wire in the possibility list that's also present in the 4 signal
  wD = [w for w in possible_d_wires if w in list(sig[4])][0]

  # the 0 signal is the one with 6 wires that does not contain the D wire
  sig[0] = [i for i in ii if len(i) == 6 and wD not in list(i)][0]

  # the 9 signal is the one with 6 wires that contains both wires of the 1 signal and contains the D wire
  sig[9] = [i for i in ii if len(i) == 6 and sig[1][0] in list(i) and sig[1][1] in list(i) and wD in list(i)][0]

  # the 6 signal is the one with 6 wires that is not the 0 or 9 signal
  sig[6] = [i for i in ii if len(i) == 6 if (i != sig[0] and i != sig[9])][0]

  # the 3 signal is the one with 5 wires that contains all wires of the 1 signal
  sig[3] = [i for i in ii if len(i) == 5 and sig[1][0] in list(i) and sig[1][1] in list(i)][0]

  # the 5 signal is the one with 5 wires that is fully a subset of the 6 signal
  sig[5] = [i for i in ii if len(i) == 5 and set(i).issubset(sig[6])][0]

  # finally, the 2 signal is the one that's not any of the other ones!
  sig[2] = [i for i in ii if i not in sig][0]

  # convert output signals to digits and append the final number to the values list
  result = ''
  for o in oo:
    for i in range(10):
      if all(item in list(o) for item in list(sig[i])) and len(o) == len(sig[i]):
        result += str(i)
  output_values.append(int(result))

print(sum(output_values))
