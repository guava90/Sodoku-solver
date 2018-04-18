# Slice n' dice module
import sodoku_list
import search_sodoku

def write_number(sodoku, i, j):
    # Om det bara finns en kandidat för en cell tar denna funktionen bort
    # Den tomma placeholder strängen så siffran blir satt. Lyckas funktionen
    # returnerar den True, annars False.
    
    if (len(sodoku[i][j]) == 2) and (sodoku[i][j][0] == " "):
        del sodoku[i][j][0]
        print("Writhing", sodoku[i][j][0], "at sodoku[", i, "][", j, "]")
        return True
    return False

def find_singles(sodoku):
    # Går igenom varje cell i sodokut och letar efter listor som bara har en kandidat.
    
    i = 0
    j = 0
    empty = search_sodoku.search(sodoku)
    miss = 0
    # Missar vi 81 ggr i rad finns det inga mer singlar på spelplan.
    while miss < 81:
        # write_number() skickar ut en flagga om den lyckats eller inte. Misslyckas den
        # uppdaterar vi koordinaten och testar igen. Lyckas den uppdaterar vi listorna.
        if not write_number(sodoku, i, j):
            miss = miss + 1
            i = i + 1
            if i == 9:
                i = 0
                j = (j + 1) % 9
        else:
            sodoku_list.update_list(sodoku, i, j)
            miss = 0
            empty = empty - 1
            print("Remaining empty cells:", empty)
    return empty

def hidden_singles(sodoku): 
    # Går igenom region en siffra i taget och kollar om det finns någon kandidat
    # som bara kan vara i en specifik cell.
    miss = 0
    i = 0
    j = 0
    a = 1
    empty = search_sodoku.search(sodoku)
    while miss < 729:
        # har haft problem med if-satsen: den har skrivit över en icke tom cell!
        # kolla om det går att ha radbrytning i if-satsen så raden inte är 156
        # karaktärer lång!
        if ((search_sodoku.search_row_hidden(sodoku, i, a) == 1) or
            (search_sodoku.search_kol_hidden(sodoku, j, a) == 1) or
            (search_sodoku.search_box_hidden(sodoku, i, j, a) == 1)) and (sodoku[i][j].count(a) == 1):# and (sodoku[i][j][0] == " "):
            sodoku[i][j] = [a]
            print("Writhing hidden", sodoku[i][j][0], "at sodoku[", i, "][", j, "]")
            sodoku_list.update_list(sodoku, i, j)
            empty = empty - 1
            miss = 0
            i = i + 1
            if i == 9:
                i = 0
                j = (j + 1) % 9
        else:
            miss = miss + 1
            if miss > a * 81:
                a = a + 1
                if a > 9:
                    a = 1
                
            i = i + 1
            if i == 9:
                i = 0
                j = (j + 1) % 9
            
    return empty
