# Forced chain module

def find_guess(sodoku):
    for i in range(9):
        for j in range(9):
            if sodoku[i][j][0] == " ":
                guess = sodoku[i][j][1:]
                break
    return guess, i, j

def forced_chain(sodoku):
    try:
        guess ,i, j = find_guess(sodoku)
        for k in guess:
            sodoku[i][j] = [k]
            solve_sodoku(sodoku)
    except IndexError:
        print("Wrong guess")
    else:
        return sodoku
