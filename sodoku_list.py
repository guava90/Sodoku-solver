# Sodoku list module
import search_sodoku

def insert_number(sodoku, a, x, y):
    # Lägger till siffran "a" i listan bakom de tomma cellerna.
    # x och y är koordinater 1 till 9 varför de minskas med 1.
    if sodoku[x - 1][y - 1][0] == " ":
        sodoku[x - 1][y - 1].append(a) # sodoku[rad][kolumn][värde]
    return

def make_list(sodoku):
    # Går igenom talen 1 - 9 för varje cell och kollar om de är kandidat
    # att skriva in. Är de kandidat läggs de till i listan.
    for a in range(1,10):
        for i in range(9):
            for j in range(9):
                if not ((search_sodoku.search_box(sodoku, i, j, a) or
                         search_sodoku.search_row(sodoku, i, a)) or
                         search_sodoku.search_kol(sodoku, j, a)):
                    insert_number(sodoku, a, i + 1, j + 1)
    return

def uppdate_list(sodoku, i, j):
    # Kolla de "fält" som påvärkats av inskriven siffra och tar bort kandidater
    # ur de listorna.
    a = sodoku[i][j][0]
    for k in range(9):
        if k != i and sodoku[k][j].count(a) != 0:
            sodoku[k][j].remove(a)
        if k != j and sodoku[i][k].count(a) != 0:
            sodoku[i][k].remove(a)
    for k in range(i - i % 3, i - i % 3 + 3):
        for l in range(j - j % 3, j - j % 3 + 3):
            if (k != i or l != j) and sodoku[k][l].count(a) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                sodoku[k][l].remove(a)
    return
