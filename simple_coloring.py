# Simple Coloring module
import search_sodoku
import sodoku_list
import print_sodoku

def find_start(sodoku, a):
    # Söker efter startpositionen för enkel färglägning    
##    a = search_sodoku.ninki(sodoku)
    for i in range(9):
        for j in range(9):
            statement1 = sodoku[i][j][0] == " "
            statement2 = search_sodoku.search_row_hidden(sodoku, i, a) == 2
            statement3 = search_sodoku.search_kol_hidden(sodoku, j, a) == 2
            statement4 = search_sodoku.search_box_hidden(sodoku, i, j, a) == 2
            if statement1 and statement2 and statement3 and statement4:
                start = (i, j)
                sodoku[i][j].insert(0, "X")
                print("Start coloring kandidate", a, "with X at", i, j)
                return start #, a
    return () 
#def find_next(sodoku, i0, j0, i1, j1, i2, j2, a):
    
    

def color_row(sodoku, n, i, j, a):
    end = True
    for k in range(9):
        if sodoku[i][k][0] == " " and sodoku[i][k].count(a) == 1 and search_sodoku.search_row_hidden(sodoku, i, a) < 3:
            if n % 2 == 0:
                sodoku[i][k].insert(0, "X")
                print("Coloring", i, k, "with X.")
            else:
                sodoku[i][k].insert(0, "O")
                print("Coloring", i, k, "with O.")
            n = n + 1
            j = k
            end = False
    return j, n, end
    
def color_kol(sodoku, n, i, j, a):
    end = True
    for k in range(9):
        # kolla så kolumnen inte innehåller mer än två istället för boxen!
        # markera ut alla, sen i slutet tas de koordinaterna in i kompisrutor
        # letar funktionen! samma för rad!
        if sodoku[k][j][0] == " " and sodoku[k][j].count(a) == 1 and search_sodoku.search_kol_hidden(sodoku, j, a) < 3:
            if n % 2 == 0:
               sodoku[k][j].insert(0, "X")
               print("Coloring", k, j, "with X.")
            else:
               sodoku[k][j].insert(0, "O")
               print("Coloring", k, j, "with O.")
            n = n + 1
            i = k
            end = False
    return i, n, end

def color_box(sodoku, n, i, j, a):
    end = True
    for k in range(i - i % 3, i - i % 3 + 3):
        for l in range(j - j % 3, j - j % 3 + 3):
            if sodoku[k][l][0] == " " and sodoku[k][l].count(a) == 1 and search_sodoku.search_box_hidden(sodoku, i, j, a) < 3:
                if n % 2 == 0:
                    sodoku[k][l].insert(0, "X")
                    print("Coloring", k, l, "with X.")
                else:
                    sodoku[k][l].insert(0, "O")
                    print("Coloring", k, l, "with O.")
                n = n + 1
                i = k
                j = l
                end = False
    return i, j, n, end

def buddies(i1, j1, i2, j2):
    # Funktion som hittar kompisrutor. Två koord in, lista med koord ut.
    koord = []
    if i1 != i2 and j1 != j2 and i1 - i1 % 3 != i2 - i2 % 3 and j1 - j1 % 3 != j2 - j2 % 3:
        koord = [(i1, j2), (i2, j1)]
        return koord
    elif i1 != i2 and j1 != j2 and i1 - i1 % 3 == i2 - i2 % 3 and j1 - j1 % 3 != j2 - j2 % 3:
        for k in range(j1 - j1 % 3, j1 - j1 % 3 + 3):
            koord.append((i2, k))
        for k in range(j2 - j2 % 3, j2 - j2 % 3 + 3):
            koord.append((i1, k))
        return koord
    elif i1 != i2 and j1 != j2 and i1 - i1 % 3 != i2 - i2 % 3 and j1 - j1 % 3 == j2 - j2 % 3:
        for k in range(i1 - i1 % 3, i1 - i1 % 3 + 3):
            koord.append((k, j2))
        for k in range(i2 - i2 % 3, i2 - i2 % 3 + 3):
            koord.append((k, j1))
        return koord
    else:
        print("Koordinates share a box so the buddies should already have been \n dealt with earlier.")
        return koord


    
def simple_coloring(sodoku, a):
    # Får kolla av rad/kol och sen box. Skulle ena ge återvändsgränd gå efter
    # den andra. Ger båda återvändsgränd terminerar vi.
##    try:
##        start, a = find_start(sodoku)
##    except TypeError:
##        print("None found.")
##        return
##    else:
##        print("Found", a)
    start = find_start(sodoku, a)
    
    if len(start) == 0:
        return
    
    i0 = start[0]
    j0 = start[1]

    j1, n, end1 = color_row(sodoku, 1, i0, j0, a)
    i1, n, end2  = color_kol(sodoku, 1, i0, j0, a)
    i2, j2, n, end3  = color_box(sodoku, 1, i0, j0, a)
    n = 2
    # Om 1 och 2 stämmer kan vi gå längs kolumn j0 till rad i1 och
    # uppdatera där.
    statement1 = search_sodoku.search_row_hidden(sodoku, i1, a) == 2
    statement2 = search_sodoku.search_box_hidden(sodoku, i1, j0, a) == 2
    
    # Om 3 och 4 stämmer kan vi gå längs rad i0 till kolumn j1 och
    # uppdatera där.
    statement3 = search_sodoku.search_kol_hidden(sodoku, j1, a) == 2
    statement4 = search_sodoku.search_box_hidden(sodoku, i0, j1, a) == 2
    
    # Om 5 stämer och 6 inte stämmer går vi till (i2,j2) och uppdaterar
    # raden. Eller tvärt om.
    statement5 = search_sodoku.search_row_hidden(sodoku, i2, a) == 2
    statement6 = search_sodoku.search_kol_hidden(sodoku, j2, a) == 2
    
    end = end1 and end2 and end3
    while not end:
        # Om 1 och 2 stämmer kan vi gå längs kolumn j0 till rad i1 och
        # uppdatera där.
        if statement1 and statement2: # and statement3:
            print("Moving to position", i1, j0, "n =", n)
            i0 = i1
            j1, m, end1 = color_row(sodoku, n, i0, j0, a)
            i2, j2, n, end2 = color_box(sodoku, n, i0, j0, a)
            
            end = end1 and end2
            
            statement1 = False
            statement2 = False
        
            statement3 = search_sodoku.search_kol_hidden(sodoku, j1, a) == 2
            statement4 = search_sodoku.search_box_hidden(sodoku, i0, j1, a) == 2
        
            statement5 = search_sodoku.search_row_hidden(sodoku, i2, a) == 2
            statement6 = search_sodoku.search_kol_hidden(sodoku, j2, a) == 2
        # Om 3 och 4 stämmer kan vi gå längs rad i0 till kolumn j1 och
        # uppdatera där.
        elif statement3 and statement4:
            print("Moving to position", i0, j1, "n =", n)
            j0 = j1
            i1, m, end1 = color_kol(sodoku, n, i0, j0, a)
            i2, j2, n, end2 = color_box(sodoku, n, i0, j0, a)
            
            end = end1 and end2
            
            statement1 = search_sodoku.search_row_hidden(sodoku, i1, a) == 2
            statement2 = search_sodoku.search_box_hidden(sodoku, i1, j0, a) == 2
        
            statement3 = False
            statement4 = False
            
            statement5 = search_sodoku.search_row_hidden(sodoku, i2, a) == 2
            statement6 = search_sodoku.search_kol_hidden(sodoku, j2, a) == 2
        # Om 5 stämer och 6 inte stämmer går vi till (i2,j2) och uppdaterar
        # raden. Eller tvärt om.
        elif statement5 and not statement6:
            print("Moving to position", i2, j2, "n =", n)
            i0 = i2
            j0 = j2
            j1, n, end = color_row(sodoku, n, i0, j0, a)
            
            statement1 = search_sodoku.search_row_hidden(sodoku, i1, a) == 2
            statement2 = search_sodoku.search_box_hidden(sodoku, i1, j0, a) == 2
            
            statement3 = search_sodoku.search_kol_hidden(sodoku, j1, a) == 2
            statement4 = search_sodoku.search_box_hidden(sodoku, i0, j1, a) == 2
            
            statement5 = False
            statement6 = search_sodoku.search_kol_hidden(sodoku, j2, a) == 2
            
        elif not statement5 and statement6:
            print("Moving to position", i2, j2, "n =", n)
            i0 = i2
            j0 = j2
            i1, n, end = color_kol(sodoku, n, i0, j0, a)
            
            statement1 = search_sodoku.search_row_hidden(sodoku, i1, a) == 2
            statement2 = search_sodoku.search_box_hidden(sodoku, i1, j0, a) == 2
            
            statement3 = search_sodoku.search_kol_hidden(sodoku, j1, a) == 2
            statement4 = search_sodoku.search_box_hidden(sodoku, i0, j1, a) == 2
            
            statement5 = search_sodoku.search_row_hidden(sodoku, i2, a) == 2
            statement6 = False
            
        else:
            end = True
    print("Making a simple coloring:")
    print_sodoku.print_sodoku(sodoku)
    sodoku_list.update_list_color(sodoku, a)
    return

def find_O(sodoku):
    for i in range(9):
        for j in range(9):
            if sodoku[i][j][0] == "O":
                return i, j
    return 9, 9
            
def find_X(sodoku, i, j, a):
    for k in range(9):
        for l in range(9):
            if k != i and l != j and sodoku[k][l][0] == "X":
                koord = buddies(i,j,k,l)
                for n in range(len(koord)):
                    i0 = koord[n][0]
                    j0 = koord[n][1]
                    if sodoku[i0][j0].count(a) != 0:
                        print("Executing: sodoku[", i0, "][", j0, "].remove(", a, ")")
                        sodoku[i0][j0].remove(a)
    sodoku[i][j].remove("O")
    return
    
def remove_X(sodoku):
    for i in range(9):
        for j in range(9):
            if sodoku[i][j].count("X") == 1:
                sodoku[i][j].remove("X")
    return

