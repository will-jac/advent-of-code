
data = open('input.txt', 'r').read().split('\n')

nums = ['one','two','three','four','five','six','seven','eight','nine']

digits = []
for l in data:
    # many options here. easiest to just scan through the whole string
    first_num, last_num = 0,0

    # find the first number
    for i in range(len(l)):
        if l[i].isdigit():
            first_num = l[i]
            break
        is_num = [n == l[i:i+len(n)] for n in nums]
        if any(is_num):
            first_num = str(is_num.index(True)+1)
            break
            
    for i in range(len(l)-1,-1,-1):
        if l[i].isdigit():
            last_num = l[i]
            break
        
        is_num = [n == l[i-len(n)+1:i+1] for n in nums]
        if any(is_num):
            last_num = str(is_num.index(True)+1)
            break
            
    d = int(first_num + last_num)

    digits.append(d)
print(sum(digits))