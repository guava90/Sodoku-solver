# Pathway: C:\Users\Mattias\AppData\Local\Programs\Python\Python36-32

# Delade upp koden i moduler när den började bli stor.
# Ska kanske lägga till en module för vanligare funktioner som
# write_number() i slice_n_dice.py utifall jag behöver den i
# kommande moduler också.
import print_sodoku
import sodoku_list
import slice_n_dice
import bounded_pairs
#import bounded_triples
import search_sodoku

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
    print("Searching for triples in row", i)
    for j in range(9):
        for k in kand_value[1:5]:
            #print(i, j, k, sodoku[i][j].count(k))
            n = n + sodoku[i][j].count(k)
            if (n == 2 and len(sodoku[i][j]) == 3) or (n == 3 and len(sodoku[i][j]) == 4) :
                koord.append([i,j])
                n = 0
    if len(koord) == 3:
        return koord
    else:
        print("No triples found.")
        return []

def find_triples_kol(sodoku, kand_koord, kand_value):
    #
    n = 0
    koord = []
    j = kand_koord[1]
    print("searching for triples in kolumn", j)
    for i in range(9):
        for k in kand_value[1:5]:
            #print(i, j, k, sodoku[i][j].count(k))
            n = n + sodoku[i][j].count(k)
            if (n == 2 and len(sodoku[i][j]) == 3) or (n == 3 and len(sodoku[i][j]) == 4) :
                koord.append([i,j])
                n = 0
    if len(koord) == 3:
        #print("Triples found at (",i ,",", j, ") \n kand:", kand_value)
        return koord
    else:
        print("No triples found.")
        return []

def remove_triples_row(sodoku, a, i1, j1, b, i2, j2, c, i3, j3):
    for k in range(9):
        # kan bli fel med if-satsen. Isåfall lägg till append() i en till
        # if-sats!
        if k!= i1 and k != i2 and k != i3 and sodoku[k][j1].count(a) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", a, ")")
            sodoku[k][j1].remove(a)
        if k!= i1 and k != i2 and k != i3 and sodoku[k][j1].count(a) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", b, ")")
            sodoku[k][j1].remove(b)
        if k!= i1 and k != i2 and k != i3 and sodoku[k][j1].count(a) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", c, ")")
            sodoku[k][j1].remove(c)
    return

def remove_triples_kol(sodoku, a, i1, j1, b, i2, j2, c, i3, j3):
    for k in range(9):
        # kan bli fel med if-satsen. Isåfall lägg till append() i en till
        # if-sats!
        if k!= j1 and k != j2 and k != j3 and sodoku[i1][k].count(a) != 0:
            print("Exicuting: sodoku[", i1, "][", k, "].remove(", a, ")")
            sodoku[i1][k].remove(a)
        if k!= j1 and k != j2 and k != j3 and sodoku[i1][k].count(b) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", b, ")")
            sodoku[i1][k].remove(b)
        if k!= j1 and k != j2 and k != j3 and sodoku[i1][k].count(c) != 0:
            print("Exicuting: sodoku[", k, "][", j1, "].remove(", c, ")")
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



sodoku25 = [[[" "],[" "],[" "],[ 3 ],[" "],[" "],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[" "],[" "],[" "],[ 9 ],[ 8 ],[" "]],
            [[" "],[" "],[ 2 ],[ 1 ],[ 4 ],[" "],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[ 1 ],[ 4 ]],
            [[" "],[ 9 ],[" "],[" "],[" "],[" "],[" "],[ 3 ],[" "]],
            [[ 6 ],[ 8 ],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[" "],[ 9 ],[ 8 ],[ 6 ],[" "],[" "]],
            [[" "],[ 2 ],[ 1 ],[" "],[" "],[" "],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[" "],[" "],[ 5 ],[" "],[" "],[" "]]]

# TESTS

print("Input:")
print_sodoku.print_sodoku(sodoku25)
empty_old = search_sodoku.search_empty(sodoku25)
sodoku_list.make_list(sodoku25)
empty = slice_n_dice.find_singles(sodoku25)
empty = slice_n_dice.hidden_singles(sodoku25)
print("Entering for-loop.")
for i in range(5):
    if empty == 0:
        # När koden är klar ska for-loopen bli en while-loop och då ska den
        # terminera när empty = 0 (dvs while empty > 0:)
        print("Done after", i, "iterations!")
        break
##    elif empty == empty_old:
##        # Här ska koden för triplarna ske.
##        print("No advancement, terminated.")
##        print(100 * (1 - empty / 81), "% done.")
##        break
    else:
        print(100 * (1 - empty / 81), "% done.")

    while empty < empty_old:
        empty_old = empty
        empty = slice_n_dice.find_singles(sodoku25)
        empty = slice_n_dice.hidden_singles(sodoku25)

    list = bounded_pairs.find_pair(sodoku25)
    #print(list[0])
    #print(list[1])

    koord = bounded_pairs.bounded_pair(list)

    #print(koord)
    for k in range(len(koord)):
        if k % 2 == 0:
            sodoku_list.update_list_pair(sodoku25, koord[k], koord[k + 1])

    triples = kand_triples(sodoku25)
    for k in range(len(triples[1])):
        # koord skrivs över nu!
        koord = find_triples_kol(sodoku25, triples[0][k], triples[1][k])
        if len(koord) == 3:
            sodoku_list.update_list_triples(sodoku25, koord[0], koord[1], koord[2], triples[1][k])



    #print(triples)
    empty = slice_n_dice.find_singles(sodoku25)
    empty = slice_n_dice.hidden_singles(sodoku25)


print("Output:")
print_sodoku.print_sodoku(sodoku25)
