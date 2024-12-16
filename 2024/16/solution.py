import sys
import bisect 

D = open(sys.argv[1]).read().strip().split('\n')
M = {(i+j*1j): c for j,r in enumerate(D) for i,c in enumerate(r)}
h = len(D)
w = len(D[0])

for p,v in M.items():
    if v == 'S':
        start = p
        break
d = 1

def djikstra(p,d,c):
    Q = [(p,d,c)]
    visiting = {}
    processed = set()
    iter = 0
    while len(Q) > 0:
        p,d,c = Q.pop(0)
        if (p,d) in processed:
            continue
        processed.add((p,d))

        if M[p] == 'E': return c

        # keep walking
        if p+d in M and M[p+d] != '#':
            if (p+d,d,c+1) not in visiting or visiting[(p+d, d)] > c+1: 
                visiting[(p+d, d)] = c+1
                bisect.insort_left(Q, (p+d,d,c+1), key=lambda x: x[2])
        # turn and move one step
        for dd in [d*1j, d*-1j]:
            if p+dd in M and M[p+dd] != '#':
                if (p+dd,dd,c+1001) not in visiting or visiting[(p+dd, dd)] > c+1001: 
                    visiting[(p+dd, dd)] = c+1001
                    bisect.insort_left(Q, (p+dd,dd,c+1001), key=lambda x: x[2])

        # print(p,d,c, '\t', len(Q), Q[:5])
        iter += 1
        if iter % 1000 == 0:
            print(iter, len(Q), len(visiting), len(processed))

res = djikstra(p,d,0)
print(res)