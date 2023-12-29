import sys
import re
import math
from collections import defaultdict
D = open(sys.argv[1]).read().strip().split('\n')

p1 = 0
p2 = 0

inst = D[0]
nw = {}

for line in D[2:]:
    s = line[0:3]
    l = line[7:10]
    r = line[12:15]
    nw[s] = [l,r]

C = [k for k in nw if k[2] == 'A']
p2 = []
for c in C:
    p1 = 0
    while c[2] != 'Z':
        for i in inst:
            if i == 'L':
                c = nw[c][0]
            else:
                c = nw[c][1]
            p1 += 1
            if c[2] == 'Z':
                break
    if c == 'ZZZ':
        print(p1)
    p2.append(p1)

# chinese remainder theorem time
# this only works because we don't have overlapping paths, I think. Not sure that it's guaranteed to
lcm = 1
for x in p2:
    lcm = (x*lcm)//math.gcd(x,lcm)
print(lcm)