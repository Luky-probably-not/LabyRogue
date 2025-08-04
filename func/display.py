from func.displayEnemy import *
from func.displayPlayer import *
from func.displayCard import *

def display(player,enemy):
    print("\033c")
    lineBorder("u")
    for i in range(15):
        if i > 1 and i < 5:
            continue
        elif i == 1:
            displayEnemy(enemy)
            lineVoid()
        elif i == 6:
            displayPlayer(player)
            lineVoid()
        elif i > 7 and i < 15:
            continue
        elif i == 7:
            displayCard(player)
        else:
            lineVoid()

    lineBorder("d")


def lineBorder(p):
    if p == "u":
        print("┌────────────────────────────────────────────────────────┐")
    elif p == "d":
        print("└──────────────────┴──────────────────┴──────────────────┘")