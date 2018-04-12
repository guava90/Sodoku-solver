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

##def chain(list):
##    koord_chain = [list[0][0]]
##    #list[0].remove(koord_chain[0])
##    i = koord_chain[0][0]
##    for k in renge(len(list[0])):
##        if list[0][k][0] == i and (list[1][k][1] == or list[1][k][1] == ):
##            koord_chain.append(list[0][k])
##            break
##    
    
    
            
            
    
def solve_sodoku(sodoku):
    
    empty_old = search_sodoku.search_empty(sodoku)
    sodoku_list.make_list(sodoku)
    empty = slice_n_dice.find_singles(sodoku)
    empty = slice_n_dice.hidden_singles(sodoku)
    print("Entering for-loop.")
    #while empty > 0:
    for n in range(5):
        if empty == 0:
            break
        #if empty == empty_old:
             #solve_sodoku(sodoku)
##        print("No advancement, terminated.")
            #print(100 * (1 - empty / 81), "% done.")
##        break
##            list = bounded_pairs.find_pair(sodoku)
##            new_sodoku = sodoku
##            i = list[0][0][0]
##            j = list[0][0][1]
##            a = list[1][0][1]
##            new_sodoku[i][j] = [a]
##            sodoku_list.update_list(new_sodoku, i, j)
##            solve_sodoku(new_sodoku)
##            print("Output:")
##            print_sodoku.print_sodoku(sodoku)
            #return sodoku   
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


    #print(triples)
        empty = slice_n_dice.find_singles(sodoku)
        empty = slice_n_dice.hidden_singles(sodoku)

    return sodoku
    
    

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
solve_sodoku(sodoku25)
print("Output:")
print_sodoku.print_sodoku(sodoku25)
