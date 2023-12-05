import sys
import re
D = open(sys.argv[1]).read().strip().split('\n')

p1 = 0
p2 = 0

symbols = [c for c in '!@#$%^&*()-_=+[]{};:\'"|\\,<>/?`~']

numbers = []
# find numbers, then look around them for symbols
for lineidx, line in enumerate(D):

    for j in range(len(line)):
        if line[j] == '.': 
            continue

        if line[j] in symbols:
            # print(lineidx,j,line[j])
            # look for adjacent numbers
            window = [(lineidx-1,j) for j in range(j-1,j+2)] + [(lineidx,j-1), (lineidx,j+1)] + [(lineidx+1,j) for j in range(j-1,j+2)]
            window = [(i,j) for (i,j) in window if i >= 0 and i < len(D) and j >= 0 and j < len(line)]
            # print('\t', window)
            matches = [(i,j) for (i,j) in window if D[i][j].isdigit()]
            # print('\t', matches)

            # filter out matches on the same row next to each other -- these are a part of the same number
            # do so by getting a filter, then only accepting False or the first true in a sequence
            overlap = [(i,j-1) in matches or (i,j+1) in matches for i,j in matches]
            unique_matches = []
            in_span = False
            curr_line = -1
            for (ii,jj), o in zip(matches, overlap):
                if not in_span or curr_line != ii: unique_matches.append((ii,jj))
                in_span = o
                curr_line = ii
            # print('\t', unique_matches)
            nums_found = []
            for ii,jj in unique_matches:
                # find the number with that index on that line -- search back to find the start, then forward to find the end
                for start in range(jj,-1,-1):
                    if not D[ii][start].isdigit():
                        start += 1 # re-align start to be the right index
                        break
                for end in range(jj,len(line)):
                    if not D[ii][end].isdigit():
                        end -= 1 # re-align to actually be the end
                        break
                num = int(D[ii][start:end+1])
                if (ii, start) not in numbers:
                    numbers.append((ii,start))
                    # print(ii,start,num)
                    p1 += num
                nums_found.append(num)

            if line[j] == '*' and len(nums_found) == 2:
                p2 += nums_found[0]*nums_found[1]
    
    # if lineidx == 5: break

print(p1)
print(p2)

