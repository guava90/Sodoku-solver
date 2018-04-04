# Sodoku list module
import search_sodoku
import bounded_pairs

def insert_number(sodoku, a, x, y):
    # Lägger till siffran "a" i listan bakom de tomma cellerna.
    # x och y är koordinater 1 till 9 varför de minskas med 1.
    # print("inserting", a, "at", x - 1, y - 1)
    if sodoku[x - 1][y - 1][0] == " ":
        sodoku[x - 1][y - 1].append(a) # sodoku[rad][kolumn][värde]
    return

def make_list(sodoku):
    # Går igenom talen 1 - 9 för varje cell och kollar om de är kandidat
    # att skriva in. Är de kandidat läggs de till i listan.
    print("Making lists.")
    for a in range(1,10):
        for i in range(9):
            for j in range(9):
                if not ((search_sodoku.search_box(sodoku, i, j, a) or
                         search_sodoku.search_row(sodoku, i, a)) or
                         search_sodoku.search_kol(sodoku, j, a)):
                    insert_number(sodoku, a, i + 1, j + 1)
    return

def update_list(sodoku, i, j):
    # Kolla de "fält" som påvärkats av inskriven siffra och tar bort kandidater
    # ur de listorna.
    a = sodoku[i][j][0]
    print("Updating list, singel.")# Koordinate:", i, j, "Value:", a)
    for k in range(9):
        if k != i and sodoku[k][j].count(a) != 0:
            print("Exicuting: sodoku[", k, "][", j, "].remove(", a, ")")
            sodoku[k][j].remove(a)
        if k != j and sodoku[i][k].count(a) != 0:
            print("Exicuting: sodoku[", i, "][", k, "].remove(", a, ")")
            sodoku[i][k].remove(a)
    for k in range(i - i % 3, i - i % 3 + 3):
        for l in range(j - j % 3, j - j % 3 + 3):
            if (k != i or l != j) and sodoku[k][l].count(a) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                print("Exicuting: sodoku[", k, "][", l, "].remove(", a, ") box")
                sodoku[k][l].remove(a)
    return

def update_list_pair(sodoku, koord_pair1, koord_pair2):
    # Kollar vilka regioner som koordinaterna har gemensamt och tar bort siffrorna
    # från de listor som ligger i dessa regioner.
    i = koord_pair1[0]
    j = koord_pair1[1]
    I = koord_pair2[0]
    J = koord_pair2[1]
    a = sodoku[i][j][1]
    b = sodoku[i][j][2]
    
    print("Updating list, pair. Koordinates: (", i, ",", j, "), (", I, ",", J, ")")

    if i == I:
        print("koordinates share a row.")
        bounded_pairs.remove_pair_row(sodoku, a, i, j, b, I, J)
        
    if j == J:
        print("Koordinates share kolumn.")
        bounded_pairs.remove_pair_kol(sodoku, a, i, j, b, I, J)
        
    if (i - i % 3 == I - I % 3) and (j - j % 3 == J - J % 3):
        print("Koordinates share a box.")
        bounded_pairs.remove_pair_box(sodoku, a, i, j, b, I, J)
        
    return

