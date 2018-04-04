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

def remove_pair_box(sodoku, a, i, j, b, I, J):
    for k in range(i - i % 3, i - i % 3 + 3):
        for l in range(j - j % 3, j - j % 3 + 3):
            if (k != i or l != j) and sodoku[k][l].count(a) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                print("Exicuting: sodoku[", k, "][", l, "].remove(", a, ") box")
                sodoku[k][l].remove(a)
                if k == I and l == J:
                    print("Exicuting: sodoku[", I, "][", J, "].append(", a, ")")
                    sodoku[I][J].append(a)
            if (k != i or l != j) and sodoku[k][l].count(b) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                print("Exicuting: sodoku[", k, "][", l, "].remove(", b, ") box")
                sodoku[k][l].remove(b)
                if k == I and l == J:
                    print("Exicuting: sodoku[", I, "][", J, "].append(", b, ")")
                    sodoku[I][J].append(b)
    return

def remove_pair_row(sodoku, a, i, j, b, I, J):
    for k in range(9):
        if k != j and i == I and sodoku[i][k].count(a) != 0 and k != J:
            print("Exicuting: sodoku[", i, "][", k, "].remove(", a, ")")
            sodoku[i][k].remove(a)
        if k != j and i == I and sodoku[i][k].count(b) != 0 and k != J:
            print("Exicuting: sodoku[", i, "][", k, "].remove(", b, ")")
            sodoku[i][k].remove(b)
    return

def remove_pair_kol(sodoku, a, i, j, b, I, J):
    for k in range(9):
        if k != i and j == J and sodoku[k][j].count(a) != 0 and k != I:
            print("Exicuting: sodoku[", k, "][", j, "].remove(", a, ")")
            sodoku[k][j].remove(a)
        if k != i and j == J and sodoku[k][j].count(b) != 0 and k != I:
            print("Exicuting: sodoku[", k, "][", j, "].remove(", b, ")")
            sodoku[k][j].remove(b)
    return
   
