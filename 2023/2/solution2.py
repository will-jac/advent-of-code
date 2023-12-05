data = open('input.txt').read().strip().split('\n')



tot = 0
for line in data:
    game = line.split(':')
    id = int(game[0].split(' ')[1])

    m_red = []
    m_green = []
    m_blue = []
    
    sets = game[1].split('; ')
    game_possible = True
    for s in sets:
        for ballstr in s.split(', '):
            nballs = ballstr.strip().split(' ')
            n = int(nballs[0])
            c = nballs[1]
            if c == 'red': m_red.append(n)
            if c == 'blue': m_blue.append(n)
            if c == 'green': m_green.append(n)

    c_red = max(m_red)
    c_blue = max(m_blue)
    c_green = max(m_green)
        
    tot += c_red*c_blue*c_green
print(tot)
