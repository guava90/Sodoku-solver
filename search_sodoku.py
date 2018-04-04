# Search sodoku module

def search_row(sodoku, i, a):
    # Söker igenom rad "i" och kollar om siffran "a" ingår. Gör den
    # det returneras True, annars False.
    for k in range(9):
        if sodoku[i][k][0] == a:
            return True
    return False
    # vill kanske ha ut position också. Men det såg rörigt ut.

def search_kol(sodoku, j, a):
    # Söker igenom kolumn "j" och kollar om siffran "a" ingår. Gör den
    # det returneras True, annars False.
    for k in range(9):
        if sodoku[k][j][0] == a:
            return True
    return False
        
def search_box(sodoku, i, j, a):
    # Söker igeom den lådan som "i" och "j" tillhör efter "a". Hittas
    # "a" returneras True, annars False.
    for k in range(i - i % 3, i - i % 3 + 3):
        for l in range(j - j % 3, j - j % 3 + 3):
            if sodoku[k][l][0] == a:
                return True
    return False

def search_row_hidden(sodoku, i, a):
    # Söker igenom listorna i rad "i" efter siffran "a" och returnerar
    # hur många det finns.
    n = 0
    for k in range(9):
        if sodoku[i][k][0] == " ":
            n = n + sodoku[i][k].count(a)
    return n

def search_kol_hidden(sodoku, j, a):
    # Söker igenom listorna i kolumn "j" efter siffran "a" och returnerar
    # hur många det finns.
    n = 0
    for k in range(9):
        #print(k, j, sodoku[k][j])
        if sodoku[k][j][0] == " ":
            n = n + sodoku[k][j].count(a)
    return n

def search_box_hidden(sodoku, i, j, a):
    # Söker igenom listorna i boxen som "i" och "j" tillhör efter "a" och
    # returnerar hur många det finns.
    n = 0
    for k in range(i - i % 3, i - i % 3 + 3):
        for l in range(j - j % 3, j - j % 3 + 3):
            if sodoku[k][l][0] == " ":
                n = n + sodoku[k][l].count(a)
    return n

def search_empty(sodoku):
    # Söker igenom sodoku och räknar hur många tomma celler som finns.
    n = 0
    for i in range(9):
        for j in range(9):
            if sodoku[i][j][0] == " ":
                n = n + 1
    return n
