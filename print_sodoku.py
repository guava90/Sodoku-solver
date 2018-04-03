# print sodoku module

def print_sodoku(sodoku):
    # Skriver ut sodokun i terminalen.
    for i in range(9):
        if (i % 3) == 0:
            print("||===|===|===||===|===|===||===|===|===||")
        else:
            print("||---|---|---||---|---|---||---|---|---||")

        print("||",sodoku[i][0][0],"|",sodoku[i][1][0],"|",sodoku[i][2][0],"||"
                  ,sodoku[i][3][0],"|",sodoku[i][4][0],"|",sodoku[i][5][0],"||"
                  ,sodoku[i][6][0],"|",sodoku[i][7][0],"|",sodoku[i][8][0],"||")

    print("||===|===|===||===|===|===||===|===|===||")
    return
