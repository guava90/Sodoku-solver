# Slice n' dice module
import sodoku_list

def write_number(sodoku, i, j):
    # Om det bara finns en kandidat för en cell tar denna funktionen bort
    # Den tomma placeholder strängen så siffran blir satt. Lyckas funktionen
    # returnerar den True, annars False.
    if (len(sodoku[i][j]) == 2) and (sodoku[i][j][0] == " "):
        del sodoku[i][j][0]
        return True
    return False

def find_singels(sodoku):
    # Går igenom varje cell i sodokut och letar efter listor som bara har en kandidat.
    
    i = 0
    j = 0
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
            sodoku_list.uppdate_list(sodoku, i, j)
            miss = 0
    return

    