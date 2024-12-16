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

def djikstra(c,p,d):
    Q = [(c,p,d,[p])]
    visiting = {}
    processed = set()
    iter = 0
    best_cost = None
    best_paths = []
    while len(Q) > 0:
        c,p,d,P = Q.pop(0)
        if (p,d) in processed:
            continue
        processed.add((p,d))

        if best_cost is not None and c > best_cost:
            return best_cost, best_paths

        if M[p] == 'E': 
            best_cost = c
            best_paths.append(P)
            continue
        
        # keep walking
        if p+d in M and M[p+d] != '#':
            cc = c+1
            pp = p+d
            dd = d
            if (cc,pp,dd) not in visiting or visiting[(pp, dd)] > cc: 
                PP = P.copy()
                PP.append(pp)
                visiting[(pp, dd)] = cc
                bisect.insort_left(Q, (cc,pp,dd,PP), key=lambda x: x[0])
        # turn and move one step
        for dd in [d*1j, d*-1j]:
            cc = c+1001
            pp = p+dd
            if pp in M and M[pp] != '#':
                if (cc,pp,dd) not in visiting or visiting[(pp, dd)] > cc: 
                    PP = P.copy()
                    PP.append(pp)
                    visiting[(pp, dd)] = cc
                    bisect.insort_left(Q, (cc,pp,dd,PP), key=lambda x: x[0])

        # print(p,d,c, '\t', len(Q), Q[:5])
        iter += 1
        if iter % 1000 == 0:
            print(iter, len(Q), len(visiting), len(processed))

c, P = djikstra(0,p,d)
print(c)
seats = set()
for path in P:
    for p in path:
        seats.add(p)
print(len(seats))