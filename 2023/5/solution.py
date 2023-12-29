import sys
import re
D = open(sys.argv[1]).read().strip()

p1 = 0
p2 = 0

chunks = [x.strip() for x in D.split('\n\n')]
p1 = [int(x) for x in chunks[0].split(':')[1].strip().split(' ')]
p2 = [[p1[i], p1[i+1]] for i in range(0, len(p1), 2)]

for i in range(1,len(chunks)):
    active_map = [[int(x) for x in line.strip().split(' ')] for line in chunks[i].split('\n')[1:]]
    for j in range(len(p1)):
        for dst,src,rng in active_map:
            if p1[j] >= src and p1[j] < src + rng:
                p1[j] = dst + (p1[j]-src)
                break

    p2_prime = []
    j = 0
    print(len(p2), sum([x[1] for x in p2]))
    while j < len(p2):
        val, val_r = p2[j]
        processed = False
        for dst,src,rng in active_map:
            if val+val_r > src and val < src+rng:
                # overlapping, but how so?
                if val < src and val + val_r > src + rng:
                    p2_prime.append([dst, rng])
                    p2.append([val, src-val])
                    p2.append([val, (val+val_r) - (src+rng)])
                    assert(src-val + val_r - (src-val) == val_r)
                elif val < src:
                    # print('before range: ', [val, val_r], [dst, src, rng])
                    # print('\t', [dst, val_r - (src-val)])
                    # print('\t and', [val, src-val])
                    p2_prime.append([dst, val_r - (src-val)])
                    p2.append([val, src-val])
                    assert(src-val + val_r - (src-val) == val_r)
                elif val + val_r > src + rng:
                    # print('after range: ', [val, val_r], [dst, src, rng])
                    # print('\t', [dst + (val-src), (src + rng) - val])
                    # print('\t and', [src+rng, (val+val_r) - (src+rng)])
                    p2_prime.append([dst + (val-src), (src + rng) - val])
                    p2.append([src+rng, (val+val_r) - (src+rng)])
                    assert((src + rng) - val + (val+val_r) - (src+rng))
                else:
                    # print('inside range: ', [val, val_r], [dst, src, rng])
                    # print('\t', [dst + (val-src), val_r])
                    p2_prime.append([dst + (val-src), val_r])
                    
                processed = True
                break
        if not processed:
            p2_prime.append([val, val_r])
        j += 1
    p2 = p2_prime

print(min(p1))
print(min([x[0] for x in p2]))
