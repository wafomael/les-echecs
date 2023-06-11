import numpy as np

map = np.zeros((8, 8))
nb = 0
for i in range(8):
    for j in range(8):
        nb += 1
        map[i][j] = nb
#print(map)



def positions(x, y):
    px = 74
    py = 74
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50
    return map[y1][x1]

def positions_pieces(x, y):
    px = 90
    py = 85
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50
    return map[y1][x1]

def positions_reine(x, y):
    px = 80
    py = 82
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50
    return map[y1][x1]
def positions_roi(x, y):
    px = 80
    py = 78
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50
    return map[y1][x1]

def choix(x1, y1, x2, y2):
    player = positions(x1, y1)
    pieces = positions_pieces(x2, y2)
    if player == pieces:
        #print("oui")
        return True

def choix_reine(x1, y1, x2, y2):
    player = positions(x1, y1)
    pieces = positions_reine(x2, y2)
    if player == pieces:
        #print("oui")
        return True
def choix_roi(x1, y1, x2, y2):
    player = positions(x1, y1)
    pieces = positions_roi(x2, y2)
    if player == pieces:
        #print("oui")
        return True





def deplacement_pion(x, y, mouvement, first, echiquier, boufer):
    px = 90
    py = 85
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    mouvement.append(map[y1][x1])
    if y1 + 1 <= 7:
        if map[y1 + 1][x1] not in echiquier:
            mouvement.append(map[y1 + 1][x1])

    if y1 + 1 <= 7:
        if x1 + 1 <= 7 and map[y1 + 1][x1 + 1] in echiquier:
            boufer.append(map[y1 + 1][x1 + 1])
        if x1 - 1 >= 0 and map[y1 + 1][x1 - 1] in echiquier:
            boufer.append(map[y1 + 1][x1 - 1])


    #print(mouvement)

    if first:
        mouvement.append(map[y1 + 2][x1])
    #print(mouvement)
    #print(boufer)

def deplacement_pionB(x, y, mouvement, first, echiquier, boufer):
    px = 90
    py = 85
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    mouvement.append(map[y1][x1])
    if y1 - 1 >= 0:
        if map[y1 - 1][x1] not in echiquier:
            mouvement.append(map[y1 - 1][x1])

    # print(mouvement)

    if y1 - 1 >= 0:
        if x1 + 1 <= 7 and map[y1 - 1][x1 + 1] in echiquier:
            boufer.append(map[y1 - 1][x1 + 1])
        if x1 - 1 >= 0 and map[y1 - 1][x1 - 1] in echiquier:
            boufer.append(map[y1 - 1][x1 - 1])

    if first:
        mouvement.append(map[y1 - 2][x1])
    #print(mouvement)
    #print(boufer)


def deplacement_tour(x, y, mouvement, echiquier, boufer):
    px = 90
    py = 85

    #echiquier.sort()

    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    mouvement.append(map[y1][x1])

    for i in range(x1+1, 8):
        if map[y1][i] not in echiquier:
            mouvement.append(map[y1][i])
        elif map[y1][i] in echiquier:
            boufer.append(map[y1][i])
            break
    for i in range(y1+1, 8):
        if map[i][x1] not in echiquier:
            mouvement.append(map[i][x1])
        elif map[i][x1] in echiquier:
            boufer.append(map[i][x1])
            break
    for i in range(y1-1, -1, -1):
        if map[i][x1] not in echiquier:
            mouvement.append(map[i][x1])
        elif map[i][x1] in echiquier:
            boufer.append(map[i][x1])
            break
    for i in range(x1-1, -1, -1):
        if map[y1][i] not in echiquier:
            mouvement.append(map[y1][i])
        elif map[y1][i] in echiquier:
            boufer.append(map[y1][i])
            break






def deplacement_fou(x, y, mouvement, echiquier, boufer):
    px = 90
    py = 85

    # echiquier.sort()

    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    cptx1 = x1+1
    cpty1 = y1+1


    mouvement.append(map[y1][x1])

    while cpty1 < 8 and cptx1 < 8:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 += 1
            cpty1 += 1
            #print(cptx1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    cptx1 = x1 - 1
    cpty1 = y1 + 1

    while cpty1 < 8 and cptx1 >= 0:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 -= 1
            cpty1 += 1
            #print(cpty1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    cptx1 = x1 - 1
    cpty1 = y1 - 1

    while cptx1 >= 0 and cpty1 >= 0:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 -= 1
            cpty1 -= 1
            #print(cpty1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    cptx1 = x1 + 1
    cpty1 = y1 - 1

    while cptx1 < 8 and cpty1 >= 0:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 += 1
            cpty1 -= 1
            #print(cpty1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break








def deplacement_reinne(x, y, mouvement, echiquier, boufer):
    px = 80
    py = 82
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    cptx1 = x1 + 1
    cpty1 = y1 + 1

    mouvement.append(map[y1][x1])

    while cpty1 < 8 and cptx1 < 8:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 += 1
            cpty1 += 1
            # print(cptx1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    cptx1 = x1 - 1
    cpty1 = y1 + 1

    while cpty1 < 8 and cptx1 >= 0:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 -= 1
            cpty1 += 1
            # print(cpty1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    cptx1 = x1 - 1
    cpty1 = y1 - 1

    while cptx1 >= 0 and cpty1 >= 0:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 -= 1
            cpty1 -= 1
            # print(cpty1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    cptx1 = x1 + 1
    cpty1 = y1 - 1

    while cptx1 < 8 and cpty1 >= 0:
        if map[cpty1][cptx1] not in echiquier:
            mouvement.append(map[cpty1][cptx1])
            cptx1 += 1
            cpty1 -= 1
            # print(cpty1)
        elif map[cpty1][cptx1] in echiquier:
            boufer.append(map[cpty1][cptx1])
            break

    for i in range(x1 + 1, 8):
        if map[y1][i] not in echiquier:
            mouvement.append(map[y1][i])
        elif map[y1][i] in echiquier:
            boufer.append(map[y1][i])
            break
    for i in range(y1 + 1, 8):
        if map[i][x1] not in echiquier:
            mouvement.append(map[i][x1])
        elif map[i][x1] in echiquier:
            boufer.append(map[i][x1])
            break
    for i in range(y1 - 1, -1, -1):
        if map[i][x1] not in echiquier:
            mouvement.append(map[i][x1])
        elif map[i][x1] in echiquier:
            boufer.append(map[i][x1])
            break
    for i in range(x1 - 1, -1, -1):
        if map[y1][i] not in echiquier:
            mouvement.append(map[y1][i])
        elif map[y1][i] in echiquier:
            boufer.append(map[y1][i])
            break

def deplacement_rois(x, y, mouvement, echiquier, boufer):
    px = 80
    py = 78
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    mouvement.append(map[y1][x1])
    if y1+1 <= 7:
        if map[y1+1][x1] not in echiquier:
            mouvement.append(map[y1+1][x1])
        else:
            boufer.append(map[y1+1][x1])
    if y1-1 > 0:
        if map[y1-1][x1] not in echiquier:
            mouvement.append(map[y1-1][x1])
        else:
            boufer.append(map[y1-1][x1])
    if x1+1 <= 7:
        if map[y1][x1+1] not in echiquier:
            mouvement.append(map[y1][x1+1])
        else:
            boufer.append(map[y1][x1+1])
    if x1-1 > 0:
        if map[y1][x1-1] not in echiquier:
            mouvement.append(map[y1][x1-1])
        else:
            boufer.append(map[y1][x1-1])

    if x1+1 <= 7 and y1+1 <= 7:
        if map[y1+1][x1+1] not in echiquier:
            mouvement.append(map[y1+1][x1+1])
        else:
            boufer.append(map[y1+1][x1+1])
    if y1-1 > 0 and x1-1 > 0:
        if map[y1-1][x1-1] not in echiquier:
            mouvement.append(map[y1-1][x1-1])
        else:
            boufer.append(map[y1-1][x1-1])
    if y1-1 > 0 and x1+1 <= 7:
        if map[y1-1][x1+1] not in echiquier:
            mouvement.append(map[y1-1][x1+1])
        else:
            boufer.append(map[y1-1][x1+1])
    if y1+1 <= 7 and x1+1 > 0:
        if map[y1+1][x1-1] not in echiquier:
            mouvement.append(map[y1+1][x1-1])
        else:
            boufer.append(map[y1+1][x1-1])

def deplacement_cavalier(x, y, mouvement, echiquier, boufer):
    px = 90
    py = 85
    for i in range(8):
        if x == px:
            x1 = i
        px += 50
    for i in range(8):
        if y == py:
            y1 = i
        py += 50

    mouvement.append(map[y1][x1])
    if y1 + 2 <= 7 and x1 - 1 >= 0:
        if map[y1+2][x1-1] not in echiquier:
            mouvement.append(map[y1+2][x1-1])
        boufer.append(map[y1 + 2][x1 - 1])


    if y1 + 2 <= 7 and x1 + 1 <= 7:
        if map[y1+2][x1+1] not in echiquier:
            mouvement.append(map[y1+2][x1+1])
        boufer.append(map[y1 + 2][x1 + 1])

    if y1 - 2 >= 0 and x1 - 1 >= 0:
        if map[y1-2][x1-1] not in echiquier:
            mouvement.append(map[y1-2][x1-1])
        boufer.append(map[y1 - 2][x1 - 1])

    if y1 - 2 >= 0 and x1 + 1 <= 7:
        if map[y1-2][x1+1] not in echiquier:
            mouvement.append(map[y1-2][x1+1])
        boufer.append(map[y1 - 2][x1 + 1])



    if x1 + 2 <= 7 and y1 - 1 >= 0:
        if map[y1-1][x1+2] not in echiquier:
            mouvement.append(map[y1-1][x1+2])
        boufer.append(map[y1 - 1][x1 + 2])

    if x1 + 2 <= 7 and y1 + 1 <= 7:
        if map[y1+1][x1+2] not in echiquier:
            mouvement.append(map[y1+1][x1+2])
        boufer.append(map[y1 + 1][x1 + 2])

    if x1 - 2 >= 0 and y1 - 1 >= 0:
        if map[y1-1][x1-2] not in echiquier:
            mouvement.append(map[y1-1][x1-2])
        boufer.append(map[y1 - 1][x1 - 2])

    if x1 - 2 >= 0 and y1 + 1 <= 7:
        if map[y1+1][x1-2] not in echiquier:
            mouvement.append(map[y1+1][x1-2])
        boufer.append(map[y1 + 1][x1 - 2])


    #print(mouvement)

#x = 90
#y = 285
#liste = []
#liste2 = [7, 34, 63]
#liste3 = []
#a = True
#deplacement_pionB(x, y, liste, a, liste2, liste3)
#print(deplacement_pionB(90, 435))