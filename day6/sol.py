def advance_one_day():
  timers.append(timers.pop(0))
  timers[6] += timers[8]
    
# part 1
timers = [0 for x in range(0, 9)]
for f in [int(x) for x in [l for l in open("./data", "r")][0].split(',')]:
  timers[f] += 1
[advance_one_day() for i in range(80)]  
print(sum(timers))

# part 2
[advance_one_day() for i in range(176)]  
print(sum(timers))