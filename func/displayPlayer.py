def displayPlayer(p):
    shield_hp(p)
    mana_buff(p)

def shield_hp(p):
    if p.shield < 10:
        s = 1
    elif p.shield < 100:
        s = 2
    else :
        s = 3
    hp = "hp : " + str(p.hp) + "/" + str(p.hpmax)
    print("│       ", end="")
    print("shield : " + str(p.shield), end="")
    for i in range(22-s):
        print(" ", end="")
    print(hp, end="")
    for i in range(18 - len(hp)):
        print(" ", end="") #shield : " + str(p.shield) + "                      hp : " + str(p.hp) + "/" + str(p.hpmax) + "       
    print("│")

def mana_buff(p):
    mana = "mana : " + str(p.m) + "/" + str(p.mmax)
    strengh = "strengh : " + str(p.strengh)
    resis = "resis : " + str(p.resis)
    print("│       " + mana, end="")
    for i in range(21):
        print(" ", end="")
    print(strengh,end="")
    for i in range(8-len(str(p.strengh))):
        print(" ",end="")
    print("│")
    print("│", end="")
    for i in range(38):
        print(" ", end="")
    print(resis, end="")
    for i in range(10-len(str(p.resis))):
        print(" ",end="")
    print("│")
                                         