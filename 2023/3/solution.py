import sys
import re
D = open(sys.argv[1]).read().strip().split('\n')

p1 = 0
p2 = 0

symbols = [c for c in '!@#$%^&*()-_=+[]{};:\'"|\\,<>/?`~']

# find numbers, then look around them for symbols
for i, line in enumerate(D):
    j = 0
    while j < len(line):
        if line[j] == '.': 
            j += 1
            continue
        if line[j].isdigit():
            for k in range(j,len(line)):
                if not line[k].isdigit():
                    k -= 1 # fix off-by-one errors so that k is actually at the end of the number
                    break
                
            # number found --- look around it for symbols
            idx_to_check = \
                [(i-1,jj) for jj in range(j-1,k+2)] + \
                [(i+1,jj) for jj in range(j-1,k+2)] + \
                [(i,j-1), (i,k+1)]
            idx_to_check = [(i,j) for (i,j) in idx_to_check if i >= 0 and i < len(D) and j >= 0 and j < len(line)]

            if any([D[i][j] in symbols for i,j in idx_to_check]):
                print(i,j,line[j:k+1])
                p1 += int(line[j:k+1])
            j = k + 1
        else:
            j += 1
            

# print(p1)
# print(p2)

