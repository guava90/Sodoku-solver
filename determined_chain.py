# determined chain module

import bounded_pairs

def determined_rectangle(sodoku):
    # Funktionen letar efter rektanglar med samma kandidater i alla hörn.
    # Skulle alla hörnen vara exact samma skulle sodokut inte vara unikt
    # lösbart, därför om ett hörn har ytterligare en kandidat måste denna
    # vara siffran som ska vara där.
    list = bounded_pairs.find_pair(sodoku)
    koord = bounded_pairs.bounded_pair(list)

    # Detta stycke görs för att se till så de paren som hittas ligger i
    # samma rad/kolumn.
    n = 0
    for k in range(len(koord) - 1):
        if k % 2 == 0 and koord[k][0] != koord[k + 1][0] and koord[k][1] != koord[k + 1][1]:
            koord[k] = [9, 9]
            koord[k + 1] = [9, 9]
            n = n + 2
    if n != 0:
        for k in range(n):
            koord.remove([9, 9])

    # Letar efter koordinater som dycker upp två gånger i koord. Gör de det
    # utgör de ett hörn. Därefter letar vi igenom kolumnen/raden efter de
    # koordinaten där kandidaterna finns och då hittar resterande hörn.
    for n in range(len(koord) - 1):
        for k in range(n + 1, len(koord)):
            if koord[n] == koord[k]:
                i1 = koord[n][0]
                j1 = koord[n][1]
                a = sodoku[i1][j1][1]
                b = sodoku[i1][j1][2]
                for i in range(9):
                    if (i != i1 and sodoku[i][j1].count(a) == sodoku[i][j1].count(b) == 1):
                        i2 = i
                for j in range(9):
                    if j != j1 and sodoku[i1][j].count(a) == sodoku[i1][j].count(b) == 1:
                        j2 = j

                # Om hörnet i2,j2 har mer än 3 kandidater och två av dessa är
                # samma som i resterande hörn tas de kandidaterna bort.
                if (len(sodoku[i2][j2]) > 3 and
                sodoku[i2][j2].count(a) == sodoku[i2][j2].count(b) == 1):
                    print("Found determined rectangle at: (", i1, ",", j1, ") , (", i1, ",", j2, ") , (", i2, ",", j1, ") , (", i2, ",", j2, ")")
                    print("Executing sodoku[", i2, "][", j2, "].remove(", a, ")")
                    print("Executing sodoku[", i2, "][", j2, "].remove(", b, ")")
                    sodoku[i2][j2].remove(a)
                    sodoku[i2][j2].remove(b)
    return

def semi_determined_rectangle(sodoku):
    list = bounded_pairs.find_pair(sodoku)
    koord = bounded_pairs.bounded_pair(list)

    n = 0
    for k in range(len(koord) - 1):
        if (k % 2 == 0 and koord[k][0] != koord[k + 1][0] and
        koord[k][1] != koord[k + 1][1]):
            koord[k] = [9, 9]
            koord[k + 1] = [9, 9]
            n = n + 2
    if n != 0:
        for k in range(n):
            koord.remove([9, 9])

    for k in range(len(koord)):
        if k % 2 == 0 and koord[k][0] == koord[k + 1][0]:
            i1 = koord[k][0]
            j1 = koord[k][1]
            j2 = koord[k + 1][1]
            a = sodoku[i1][j1][1]
            b = sodoku[i1][j1][2]
            for i in range(9):
                if (i != i1 and sodoku[i][j1].count(a) == 1 and
                sodoku[i][j1].count(b) == 1 and sodoku[i][j2].count(a) == 1 and
                sodoku[i][j2].count(b) == 1 and
                len(sodoku[i][j1]) == len(sodoku[i][j2]) == 4 and
                sodoku[i][j1][3] == sodoku[i][j2][3]):
                    c = sodoku[i][j1][3]
                    print("Found semi determined rectangle.")
                    bounded_pairs.remove_pair_row(sodoku, c, i, j1, 0, i, j2)
        elif k % 2 == 0 and koord[k][1] == koord[k + 1][1]:
            i1 = koord[k][0]
            i2 = koord[k + 1][0]
            j1 = koord[k][1]
            a = sodoku[i1][j1][1]
            b = sodoku[i1][j1][2]
            for j in range(9):
                if (j != j1 and sodoku[i1][j].count(a) == sodoku[i2][j].count(a)
                == sodoku[i1][j].count(b) == sodoku[i2][j].count(b) == 1 and
                len(sodoku[i1][j]) == len(sodoku[i2][j]) == 4 and
                sodoku[i1][j][3] == sodoku[i2][j][3]):
                    c = sodoku[i][j1][3]
                    print("Found semi determined rectangle.")
                    bounded_pairs.remove_pair_kol(sodoku, c, i1, j, 0, i2, j)

    return
