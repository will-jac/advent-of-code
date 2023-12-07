import sys
import re
import math
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
# replace the card values so we can sort as strings
D = D.replace('A','E')
D = D.replace('K','D')
D = D.replace('Q','C')
D = D.replace('T','A')
D = D.replace('J','0')
D = D.split('\n')

p1 = {x: [] for x in range(7)}
p2 = {x: [] for x in range(7)}

def get_hand_value(c):
    if len(c.keys()) == 1:
        return(6)
    elif len(c.keys()) == 2:
        if max(c.values()) == 4: 
            return(5)
        else:
            return(4)
    elif max(c.values()) == 3: 
        return(3)
    elif max(c.values()) == 2:
        if sum([x == 2 for x in c.values()]) == 2:
            return(2)
        else:
            return(1)
    else: 
        return(0)
    
for line in D:
    hand, bid = line.split(' ')
    bid = int(bid)
    c = defaultdict(int)
    for x in hand:
        c[x] += 1
    # set jokers to be equal to the highest
    c_j = c.copy()
    if '0' in c_j and hand != '00000':
        n = c_j['0']
        del c_j['0']
        x = max(c_j, key=c_j.get)
        c_j[x] += n
    
    ht = get_hand_value(c)   
    p1[ht].append([hand.replace('0', 'B'),bid,ht])

    ht = get_hand_value(c_j)   
    p2[ht].append([hand,bid,ht])

handorder = []
for i in range(7):
    hands = p1[i]
    hands = sorted(hands, key = lambda hands: hands[0])
    handorder += hands
    # print(f'i = {i}')
    # print([h[0] for h in hands])

# print(handorder)
# print([(i+1,x[1]) for i, x in enumerate(handorder)])
# print([(i+1)*x[1] for i, x in enumerate(handorder)])
print(sum([(i+1)*x[1] for i, x in enumerate(handorder)]))

handorder = []
for i in range(7):
    hands = p2[i]
    hands = sorted(hands, key = lambda hands: hands[0])
    handorder += hands
    # print(f'i = {i}')
    # print([h[0] for h in hands])
print(sum([(i+1)*x[1] for i, x in enumerate(handorder)]))