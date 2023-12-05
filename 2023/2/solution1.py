data = open('input.txt').read().strip().split('\n')

lim_red = 12
lim_green = 13
lim_blue = 14

ids = []
for line in data:
    game = line.split(':')
    id = int(game[0].split(' ')[1])

    sets = game[1].split('; ')
    game_possible = True
    for s in sets:
        c_red, c_grn, c_blu = 0,0,0
        for ballstr in s.split(', '):
            nballs = ballstr.strip().split(' ')
            n = int(nballs[0])
            c = nballs[1]
            if c == 'red': c_red += n
            if c == 'blue': c_blu += n
            if c == 'green': c_grn += n
        if c_red > lim_red or c_grn > lim_green or c_blu > lim_blue:
            # impossible
            game_possible = False
            break
    print(id, game_possible)
    if game_possible:
        ids.append(id)
print(sum(ids))
