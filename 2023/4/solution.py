import sys
import re
D = open(sys.argv[1]).read().strip().split('\n')

p1 = 0
p2 = 0

cards_owned = {i: 1 for i in range(len(D))}

for i, line in enumerate(D):
    [win,mine] = [[int(y) for y in re.split('\s+', x.strip())] for x in line.split(':')[1].split('|')]
    num_win = sum([n in win for n in mine])
    if num_win > 0:
        p1 += 2**(num_win-1)
    for j in range(1,num_win+1):
        cards_owned[i+j] += cards_owned[i]
            

print(p1)
print(sum(cards_owned.values()))

