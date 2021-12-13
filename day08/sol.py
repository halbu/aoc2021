# shape data
inputs = []
outputs = []
for l in [l.split(' | ') for l in open("./data", "r")]:
  inputs.append(l[0].strip('\n').split())
  outputs.append(l[1].strip('\n').split())

# part 1
print(sum(1 for o in [j for i in outputs for j in i] if len(o) in [2, 3, 4, 7]))

# part 2 verbose first pass at naive solution, doubtless could be streamlined a lot
output_values = []

for e in range(len(inputs)):
  ci = inputs[e]                # current input
  co = outputs[e]               # current output
  sig = ['' for i in range(10)] # list of signals where index = number signal represents

  sig[1] = [i for i in ci if len(i) == 2][0]
  sig[4] = [i for i in ci if len(i) == 4][0]
  sig[7] = [i for i in ci if len(i) == 3][0]
  sig[8] = [i for i in ci if len(i) == 7][0]

  sig[5] = [i for i in ci if len(i) == 5]
  possible_d_wires = set(sig[5][0])
  for s in sig[5][1:]:
    possible_d_wires.intersection_update(s)
  wD = [w for w in possible_d_wires if w in list(sig[4])][0]
  
  # figure out unknown signals based on length, comparison to known signals & state of the d wire segment
  sig[0] = [i for i in ci if len(i) == 6 and wD not in list(i)][0]
  sig[9] = [i for i in ci if len(i) == 6 and set(sig[1]).issubset(i) and wD in list(i)][0]
  sig[6] = [i for i in ci if len(i) == 6 if (i != sig[0] and i != sig[9])][0]
  sig[3] = [i for i in ci if len(i) == 5 and set(sig[1]).issubset(i)][0]
  sig[5] = [i for i in ci if len(i) == 5 and set(i).issubset(sig[6])][0]
  sig[2] = [i for i in ci if i not in sig][0]

  result = ''
  for o in co:
    for i in range(10):
      if set(o) == set(sig[i]):
        result += str(i)
  output_values.append(int(result))

print(sum(output_values))
