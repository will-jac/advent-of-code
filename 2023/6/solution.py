import sys
import re
from tqdm import tqdm
import math
D = open(sys.argv[1]).read().strip().split('\n')


times = [int(x.strip()) for x in re.split('\s+', D[0].split(':')[1].strip())]
dists = [int(x.strip()) for x in re.split('\s+', D[1].split(':')[1].strip())]

p1 = 1

for time,dist in zip(times, dists):
    times_can_beat = 0
    for t in range(time):
        d = t*(time-t)
        if d > dist:
            times_can_beat += 1
    p1 *= times_can_beat

time = int(''.join([c for c in D[0] if c.isdigit()]))
dist = int(''.join([c for c in D[1] if c.isdigit()]))
## just brute force it -- it would be much faster to take a MITM approach, or even statically calculate the time required
# p2 = 1
# times_can_beat = 0
# for t in tqdm(range(time)):
#     d = t*(time-t)
#     if d > dist:
#         times_can_beat += 1
# p2 *= times_can_beat

# okay, now that we solved it, let's actually do this properly
# d = t*(time-t) => t^2 - time*t + d = 0
record_time_held = (((time+math.sqrt(time**2 - 4*dist))/-2),((time-math.sqrt(time**2 - 4*dist))/-2))
# can beat it if there's any whole millisecond values inside that gap
p2 = math.floor(record_time_held[1]) - math.ceil(record_time_held[0])

print(p1)
print(p2)