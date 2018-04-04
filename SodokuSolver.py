# Pathway: C:\Users\Mattias\AppData\Local\Programs\Python\Python36-32

# Hårdkodad Sodoku att testa med. Går att göra egen med funktionen setup fast
# det är ganska jobbigt. Vill göra en smidigare inmatning där man skriver in
# allt på en gång.
sodoku1 = [[[5],[" "],[7],[" "],[9],[3],[4],[1],[" "]],
          [[" "],[2],[" "],[" "],[7],[" "],[" "],[3],[" "]],
          [[9],[3],[" "],[2],[5],[" "],[8],[" "],[" "]],
          [[" "],[" "],[6],[" "],[" "],[" "],[1],[" "],[" "]],
          [[" "],[" "],[9],[4],[" "],[1],[7],[" "],[" "]],
          [[" "],[" "],[2],[" "],[" "],[" "],[3],[" "],[" "]],
          [[" "],[" "],[5],[" "],[4],[2],[" "],[7],[1]],
          [[" "],[7],[" "],[" "],[1],[" "],[" "],[5],[" "]],
          [[" "],[9],[3],[5],[6],[" "],[2],[" "],[4]]]

sodoku2 = [[[" "],[" "],[1],[" "],[" "],[" "],[" "],[" "],[8]],
          [[2],[" "],[" "],[4],[" "],[" "],[" "],[" "],[6]],
          [[" "],[" "],[" "],[" "],[9],[" "],[" "],[5],[" "]],
          [[" "],[5],[" "],[" "],[" "],[7],[" "],[3],[" "]],
          [[" "],[" "],[8],[" "],[" "],[" "],[2],[" "],[" "]],
          [[" "],[4],[" "],[6],[" "],[" "],[" "],[9],[" "]],
          [[" "],[7],[" "],[" "],[1],[" "],[" "],[" "],[" "]],
          [[6],[" "],[" "],[" "],[" "],[3],[" "],[" "],[4]],
          [[4],[" "],[" "],[" "],[" "],[" "],[5],[" "],[" "]]]

# Delade upp koden i moduler när den började bli stor.
# Ska kanske lägga till en module för vanligare funktioner som
# write_number() i slice_n_dice.py utifall jag behöver den i
# kommande moduler också.
import print_sodoku
import sodoku_list
import slice_n_dice
import bounded_pairs
#import search_sodoku
        
def setup(sodoku):    
    insert = 1
    while insert == 1:
        print("Insert locked numbers.")
        x = int(input("x koordinate: "))
        y = int(input("y koordinate: "))
        value = int(input("Enter the value: "))

        insert_number(sodoku,value,x,y)
        response = input("Input another value? y/n ")
        if response == "n":
            insert = 0



# TESTS

print("Input:")
print_sodoku.print_sodoku(sodoku2)
sodoku_list.make_list(sodoku2)
empty = slice_n_dice.find_singles(sodoku2)
empty = slice_n_dice.hidden_singles(sodoku2)

for i in range(10):
    list = bounded_pairs.find_pair(sodoku2)
    #print(list[0])
    #print(list[1])

    koord = bounded_pairs.bounded_pair(list)
    #print(koord)
    for k in range(len(koord)):
        if k % 2 == 0:
            sodoku_list.update_list_pair(sodoku2, koord[k], koord[k + 1])
   
    empty = slice_n_dice.find_singles(sodoku2)
    empty = slice_n_dice.hidden_singles(sodoku2)


print("Output:")
print_sodoku.print_sodoku(sodoku2)


