# Pathway: C:\Users\Mattias\AppData\Local\Programs\Python\Python36-32

# Delade upp koden i moduler när den började bli stor.
# Ska kanske lägga till en module för vanligare funktioner som
# write_number() i slice_n_dice.py utifall jag behöver den i
# kommande moduler också.
import print_sodoku
import sodoku_list
import slice_n_dice
import bounded_pairs
import bounded_triples
import search_sodoku


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
        koord = bound_triples.find_triples_kol(sodoku25, triples[0][k], triples[1][k])
        if len(koord) == 3:
            sodoku_list.update_list_triples(sodoku25, koord[0], koord[1], koord[2], triples[1][k])
        koord = bound_triples.find_triples_row(sodoku25, triples[0][k], triples[1][k])
        if len(koord) == 3:
            sodoku_list.update_list_triples(sodoku25, koord[0], koord[1], koord[2], triples[1][k])


    #print(triples)
    empty = slice_n_dice.find_singles(sodoku25)
    empty = slice_n_dice.hidden_singles(sodoku25)


print("Output:")
print_sodoku.print_sodoku(sodoku25)
