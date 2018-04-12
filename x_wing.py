# X wing module
import search_sodoku
import bounded_pairs

def x_search_row(sodoku, a):
    # Söker igenom sodoku efter a och om a förekommer två gånger i två rader
    # returnerar funktionen vilka rader det förekom.
    R = []
    k = 0
    for i in range(9):
        n = search_sodoku.search_row_hidden(sodoku, i, a)
        if n == 2:
            R.append([i])
            for j in range(9):
                if sodoku[i][j].count(a) == 1:
                    R[k].append(j)
            k = k + 1
    return R

def x_search_kol(sodoku, a):
    # Söker igenom sodoku efter a och om a förekommer två gånger i två rader
    # returnerar funktionen vilka rader det förekom.
    K = []
    k = 0
    for j in range(9):
        n = search_sodoku.search_kol_hidden(sodoku, j, a)
        if n == 2:
            K.append([j])
            for i in range(9):
                if sodoku[i][j].count(a) == 1:
                    K[k].append(i)
            k = k + 1
    return K

def x_wing_row(sodoku):
    for a in range(1,10):
        R = x_search_row(sodoku, a)
        if len(R) == 2 and R[0][1] == R[1][1] and R[0][2] == R[1][2]:
            i1 = R[0][0]
            i2 = R[1][0]
            j1 = R[0][1]
            j2 = R[0][2]
            print("Found X-wing at (", i1, ",", j1, "), (", i2, ",", j2, ")")
            bounded_pairs.remove_pair_kol(sodoku, a, i1, j1, 0, i2, j1)
            bounded_pairs.remove_pair_kol(sodoku, a, i1, j2, 0, i2, j2)
    return

def x_wing_kol(sodoku):
    for a in range(1,10):
        K = x_search_kol(sodoku, a)
        if len(K) == 2 and K[0][1] == K[1][1] and K[0][2] == K[1][2]:
            i1 = K[0][1]
            i2 = K[0][2]
            j1 = K[0][0]
            j2 = K[1][0]
            print("Found X-wing at (", i1, ",", j1, "), (", i2, ",", j2, ")")
            bounded_pairs.remove_pair_row(sodoku, a, i1, j1, b, i1, j2)
            bounded_pairs.remove_pair_row(sodoku, a, i2, j1, b, i2, j2)
    return
