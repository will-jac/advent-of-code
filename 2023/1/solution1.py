
data = open('input.txt').read().split('\n')


digits = []
for l in data:
    # many options here. easiest to just scan through the whole string
    first_num, last_num = 0,0
    for i in range(len(l)):
        if l[i].isdigit():
            first_num = l[i]
            break
    for i in range(len(l)-1,-1,-1):
        if l[i].isdigit():
            last_num = l[i]
            break
    d = int(first_num + last_num)

    digits.append(d)
print(sum(digits))