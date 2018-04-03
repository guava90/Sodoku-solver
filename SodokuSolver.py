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

def hidden_singels(sodoku): # EJ LÄNGRE AKTIV!
    # Går igenom region en siffra i taget och kollar om det finns någon kandidat
    # som bara kan vara i en specifik cell.
    #miss = 0
    n = 0
    #while miss < 81: # while satsen måste fixas så den går igenom hela spelplanen ordentligt!
    for j in range(9):
        for a in range(1, 10):
            I = []
            for i in range(9):
                if sodoku[i][j][0] == " ":
                    n = n + sodoku[i][j].count(a)
                    if n == 1:
                        I.append(i)
            if n == 1:
                sodoku[I[0]][j] = [a]
                sodoku_list.uppdate_list(sodoku, I[0], j)
                    #miss = 0
                del I
            n = 0
     #   miss = miss + 1
    return

# TESTS

#print("Input:")
#print_sodoku.print_sodoku(sodoku2)
sodoku_list.make_list(sodoku2)
#print(sodoku[0][0])
slice_n_dice.find_singels(sodoku2)
#hidden_singels(sodoku2)
list = bounded_pairs.find_pair(sodoku2)
print(list)
list1 = bounded_pairs.bounded_pair_box(list)
print(list1)

#print("Output:")
#print_sodoku.print_sodoku(sodoku2)
#print(sodoku[0][0])

#setup(sodoku)    
#print_sodoku(sodoku)

#print(sodoku[3][8])
#write_number(sodoku, 3, 8)
#print_sodoku(sodoku)
#uppdate_list(sodoku, 3, 8)
#print(sodoku[3][0])
#print(search_box(sodoku, 4, 7, 1))

