data = open('input.txt', 'r').read().strip().split('\n')

digits = [[c for c in line if c.isdigit()] for line in data]

print(sum([int(d[0] + d[-1]) for d in digits]))