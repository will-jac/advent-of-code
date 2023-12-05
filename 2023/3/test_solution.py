
o = open('1.out').read().split('\n')
t = open('2.out').read().split('\n')

def get_dict(lines):
    nums = {}
    for l in lines:
        if l == "": continue
        i,j,n = l.split(' ')
        if (i,j) in nums: print("error:", i,j,n)
        nums[(i,j)] = n
    return nums

o_nums = get_dict(o)
t_nums = get_dict(t)

for k in o_nums:
    if k not in t_nums or o_nums[k] != t_nums[k]: print(k, o_nums[k], t_nums[k])
print('--------')
for k in t_nums:
    if k not in o_nums or o_nums[k] != t_nums[k]: print(k, o_nums[k], t_nums[k])