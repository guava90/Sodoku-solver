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
