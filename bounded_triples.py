# Bounded triples module

# hitta listor med 3 kandiadater, extrahera dessa, kolla om de finns par som
# har två av dessa kandidater, kolla om det finns tre listor i samma region
# som har två eller tre av kandidaterna i sig, profit.

def kand_triples(sodoku):
    # Söker efter listor som har längd 4 (3 kandidater).
    # Returnerar deras koordinater och listor.
    kand = [[],[]]
    #kand = []
    for i in range(9):
        for j in range (9):
            if len(sodoku[i][j]) == 4:
                kand[0].append([i,j])
                kand[1].append(sodoku[i][j])
    return kand


def find_triples_row(sodoku, kand_koord, kand_value):
    # Söker igenom sodoku efter koordinater till de celler där åtminstånde två av
    # kandidaterna finns. Dessa celler har listor med två eller tre kandidater.
    # In variabeln "kand" ska vara en lista där kand[0] innehåller koordinater och
    # kand[1] innehåller kandidaterna.
    n = 0
    koord = []
    i = kand_koord[0]
    for j in range(9):
        for k in kand_value[1:5]:
            #print(i, j, k, sodoku[i][j].count(k))
            n = n + sodoku[i][j].count(k)
            if (n == 2 and len(sodoku[i][j]) == 3) or (n == 3 and len(sodoku[i][j]) == 4) :
                koord.append([i,j])
                n = 0
        n = 0
    return koord

def find_triples_kol(sodoku, kand_koord, kand_value):
    #
    n = 0
    koord = []
    j = kand_koord[1]
    for i in range(9):
        for k in kand_value[1:5]:
            #print(i, j, k, sodoku[i][j].count(k))
            n = n + sodoku[i][j].count(k)
            if (n == 2 and len(sodoku[i][j]) == 3) or (n == 3 and len(sodoku[i][j]) == 4) :
                koord.append([i,j])
                n = 0
        n = 0
    return koord

def remove_triples_kol(sodoku, a, i1, j1, b, i2, j2, c, i3, j3):
    for k in range(9):
        # kan bli fel med if-satsen. Isåfall lägg till append() i en till
        # if-sats!
        if k!= i1 and k != i2 and k != i3 and sodoku[k][j1].count(a) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", a, ")")
            sodoku[k][j1].remove(a)
        if k!= i1 and k != i2 and k != i3 and sodoku[k][j1].count(b) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", b, ")")
            sodoku[k][j1].remove(b)
        if k!= i1 and k != i2 and k != i3 and sodoku[k][j1].count(c) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", c, ")")
            sodoku[k][j1].remove(c)
    return

def remove_triples_row(sodoku, a, i1, j1, b, i2, j2, c, i3, j3):
    for k in range(9):
        # kan bli fel med if-satsen. Isåfall lägg till append() i en till
        # if-sats!
        if k!= j1 and k != j2 and k != j3 and sodoku[i1][k].count(a) != 0:
            print("Exicuting: sodoku[", i1, "][", k, "].remove(", a, ")")
            sodoku[i1][k].remove(a)
        if k!= j1 and k != j2 and k != j3 and sodoku[i1][k].count(b) != 0:
            print("Exicuting: sodoku[", i1, "][", k, "].remove(", b, ")")
            sodoku[i1][k].remove(b)
        if k!= j1 and k != j2 and k != j3 and sodoku[i1][k].count(c) != 0:
            print("Exicuting: sodoku[", i1, "][", k, "].remove(", c, ")")
            sodoku[i1][k].remove(c)
    return

def remove_triples_box(sodoku, a, i1, j1, b, i2, j2, c, i3, j3):
    for k in range(i1 - i1 % 3, i1 - i1 % 3 + 3):
        for l in range(j1 - j1 % 3, j1 - j1 % 3 + 3):
            # kan bli fel med if-satsen. Isåfall lägg till append() i en till
            # if-sats!
            if (k != i1 or k != i2 or k != i3 or l != j1 or l != j2 or
                l != j3) and sodoku[k][l].count(a) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                print("Exicuting: sodoku[", k, "][", l, "].remove(", a, ") box")
                sodoku[k][l].remove(a)
            if (k != i1 or k != i2 or k != i3 or l != j1 or l != j2 or
                l != j3) and sodoku[k][l].count(b) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                print("Exicuting: sodoku[", k, "][", l, "].remove(", b, ") box")
                sodoku[k][l].remove(b)
            if (k != i1 or k != i2 or k != i3 or l != j1 or l != j2 or
                l != j3) and sodoku[k][l].count(c) != 0:
                # or för att vi redan sökt k = i, l = j ovan.
                print("Exicuting: sodoku[", k, "][", l, "].remove(", c, ") box")
                sodoku[k][l].remove(c)
    return
