# Bounded pair module

def find_pair(sodoku):
    # Kollar vilka celler som har listor med två element + " ".
    # Returnerar lista med koordinater.
    pair_koord = [[],[]]
    for i in range(9):
        for j in range(9):
            if len(sodoku[i][j]) == 3:
                pair_koord[0].append([i,j])
                pair_koord[1].append(sodoku[i][j])
    return pair_koord

def bounded_pair_box(pair_koord): # ANDVÄNDS EJ I NULÄGET!
    # Kollar vilka par som ligger i samma box.
    check = []
    for k in range(len(pair_koord[0])):
        check.append([pair_koord[0][k][0] - pair_koord[0][k][0] % 3,
                      pair_koord[0][k][1] - pair_koord[0][k][1] % 3])
    return check

def compare_pair(list):
    # Kollar om paren i list upprepas och när.
    pair = []
    for n in range(len(list) - 1):
        for k in range(n + 1, len(list)):
            if list[n][1] == list[k][1] and list[n][2] == list[k][2]:
                pair.append([n,k])
    return pair
    
def bounded_pair(pair_koord):
    # Tar fram bundna par ur pair_koord och ordnar deras koordinater
    # och returnerar dom i par.
    koord = []
    pair = compare_pair(pair_koord[1])
    for k in range(len(pair)):
        for l in range(2):
            koord.append(pair_koord[0][pair[k][l]])
    return koord
    
