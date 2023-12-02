data = open('input.txt', 'r').read().strip() 
for k,v in {'one':'o1e','two':'t2o','three':'t3e','four':'f4r','five':'f5e','six':'s6x','seven':'s7n','eight':'e8t','nine':'n9e'}.items():
    data = data.replace(k,v)

digits = [[line[i] for i in range(len(line)) if line[i].isdigit()] for line in data.split('\n')]

print(sum([int(d[0] + d[-1]) for d in digits]))