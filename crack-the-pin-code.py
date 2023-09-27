from itertools import product

pincode = ""

numpad = [
    ["1","2","3"],     #  0,0   1,0   2,0
    ["4","5","6"],     #  0,1   1,1   2,1
    ["7","8","9"],     #  0,2   1,2   2,2
    ["*","0","*"],     #  ***   1,3   ***
]

def find_adjactives(num):
    cx = 0
    cy = 0
    for x in range(3):
        for y in range(4):
            if(numpad[y][x] == num):
                cx = x
                cy = y
    poss = []
    xo = 1 if cx < 2 else -1
    poss.append(numpad[cy][cx + xo])
    if cx == 1: poss.append(numpad[cy][cx - 1])

    yo = 1 if cy < 3 else -1
    poss.append(numpad[cy + yo][cx])
    if cy == 1 or cy == 2: poss.append(numpad[cy - 1][cx])

    poss.append(num)
    if("*" in poss):
        for i in range(poss.count("*")):
            poss.remove("*")
    
    return poss

def crack_pincode(p):
    global pincode
    pincode = p
    g = ""
    l_variations = []
    variations = []
    poss_count = 1

    for i in pincode:
        adj = find_adjactives(i)
        l_variations.append(sorted(adj))

        poss_count *= len(adj)

    return [''.join(x) for x in product(*l_variations)]

print(crack_pincode("152"))
    


