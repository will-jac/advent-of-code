import sys

D = open(sys.argv[1]).read().strip().split('\n')

p1 = 0
p2 = 0

for l in D:
    row = [[int(r) for r in l.split(' ')]]
    i = 0
    while True:
        row.append([])
        
        for j in range(1,len(row[i])):
            row[-1].append(row[i][j] - row[i][j-1])

        if all([d == 0 for d in row[-1]]):
            # row = row[:-1] # pop the last row of all 0s off
            break

        i += 1

    for i in range(len(row)-1,0,-1):
        # print(row[i])
        row[i-1].append(row[i-1][-1] + row[i][-1])
    
    # print(row)
    p1 += row[0][-1]

print(p1)