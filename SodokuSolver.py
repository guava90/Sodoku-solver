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
import x_wing
import determined_chain
import simple_coloring


def solve_sodoku(sodoku):

    empty_old = search_sodoku.search(sodoku)
    
    empty = slice_n_dice.find_singles(sodoku)
    empty = slice_n_dice.hidden_singles(sodoku)
    print("Entering for-loop.")
    #while empty > 0:
    for n in range(5):
        if empty == 0:
            break
##        if empty == empty_old:
##            Nishio(sodoku)
                             
        else:
            print(100 * (1 - empty / 81), "% done.")

        while empty < empty_old:
            empty_old = empty
            empty = slice_n_dice.find_singles(sodoku)
            empty = slice_n_dice.hidden_singles(sodoku)

        list = bounded_pairs.find_pair(sodoku)


        koord = bounded_pairs.bounded_pair(list)

        for k in range(len(koord)):
            if k % 2 == 0:
                sodoku_list.update_list_pair(sodoku, koord[k], koord[k + 1])

        triples = bounded_triples.kand_triples(sodoku)
        for k in range(len(triples[1])):
        # koord skrivs över nu!
            koord = bounded_triples.find_triples_kol(sodoku, triples[0][k], triples[1][k])
            if len(koord) == 3:
                sodoku_list.update_list_triples(sodoku, koord[0], koord[1], koord[2], triples[1][k])
            koord = bounded_triples.find_triples_row(sodoku, triples[0][k], triples[1][k])
            if len(koord) == 3:
                sodoku_list.update_list_triples(sodoku, koord[0], koord[1], koord[2], triples[1][k])

        x_wing.x_wing_row(sodoku)
        x_wing.x_wing_kol(sodoku)
        determined_chain.determined_rectangle(sodoku)
        for a in range(1,10):
            simple_coloring.simple_coloring(sodoku, a)
    #print(triples)
        empty = slice_n_dice.find_singles(sodoku)
        empty = slice_n_dice.hidden_singles(sodoku)



    return sodoku

sodoku19 = [[[ 4 ],[" "],[" "],[" "],[ 8 ],[ 6 ],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[" "],[" "],[ 3 ],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[" "],[" "],[" "],[" "],[ 9 ],[ 7 ]],
            [[" "],[ 7 ],[ 9 ],[" "],[" "],[" "],[" "],[" "],[" "]],
            [[" "],[ 1 ],[" "],[" "],[" "],[" "],[" "],[ 6 ],[" "]],
            [[" "],[" "],[" "],[" "],[" "],[" "],[ 4 ],[ 3 ],[" "]],
            [[ 6 ],[ 4 ],[" "],[" "],[" "],[" "],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[ 7 ],[" "],[" "],[" "],[" "],[" "]],
            [[" "],[" "],[" "],[ 1 ],[ 2 ],[" "],[" "],[" "],[ 8 ]]]

# TESTS

print("Input:")
print_sodoku.print_sodoku(sodoku19)
sodoku_list.make_list(sodoku19)
solve_sodoku(sodoku19)
print("Output:")
print_sodoku.print_sodoku(sodoku19)

