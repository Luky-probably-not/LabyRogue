def displayCard(player):
    line()
    for i in range(8):
        if i == 1:
            nameCard(player.hand)
        elif i == 4:
            effectCard(player)
        else:
            emptyColonne()

def nameCard(hand):
    line = "" 
    for i in range(3):
        carte = hand[i].n
        space = "│"
        for i in range(9-(len(carte)//2 + len(carte)%2)):
           space += " "
        space += carte
        for i in range(9-len(carte)//2):
            space += " "
        line += space
    print(line + "│")

def effectCard(player):
    line = ""
    for i in range(3):
        if player.hand[i].eff == "atk":
            carte = player.hand[i].eff + " : " + str(player.hand[i].s + player.strengh)
        elif player.hand[i].eff == "def":
            carte = player.hand[i].eff + " : " + str(player.hand[i].s + player.resis)
        else:
            carte = player.hand[i].eff + " : " + str(player.hand[i].s)
        space = "│"
        for i in range(9-(len(carte)//2 + len(carte)%2)):
            space += " "
        space += carte
        for i in range(9-len(carte)//2):
            space += " "
        line += space
    print(line + "│")

def line():
    print("├──────────────────┬──────────────────┬──────────────────┤")

def emptyColonne():
    print("│                  │                  │                  │")

def lineVoid():
    print("│                                                        │")
