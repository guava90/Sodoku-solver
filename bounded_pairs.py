# Bounded pair module

def find_pair(sodoku):
    pair_koord = []
    for i in range(9):
        for j in range(9):
            if len(sodoku[i][j]) == 3:
                pair_koord.append([i,j])
    return pair_koord

def bounded_pair_box(pair_koord):
    check = []
    pair = []
    for k in range(len(pair_koord)):
        check.append([pair_koord[k][0] - pair_koord[k][0] % 3,
                      pair_koord[k][1] - pair_koord[k][1] % 3])
        # kolla om check innehåller par

