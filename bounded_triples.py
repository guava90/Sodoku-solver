# Bounded triples module

# hitta listor med 3 kandiadater, extra hera dessa, kolla om de finns par som
# har två av dessa kandidater, kolla om det finns tre listor i samma region
# som har två eller tre av kandidaterna i sig, profit.

def kand_triples(sodoku):
    # Söker efter listor som har längd 4 (3 kandidater).
    # Returnerar deras koordinater och listor.
    kand = [[],[]]
    for i in range(9):
        for j in range (9):
            if len(sodoku[i][j]) == 4:
                kand[0].append([i,j])
                kand[1].append(sodoku[i][j])
    return kand

def find_tripels(sodoku, kand):
    