def displayEnemy(enemy):
    nameEnemy(enemy)
    lineVoid()
    buff_hp(enemy)
    action_shield(enemy)


def nameEnemy(enemy):   #display the name
    f = len(enemy.name)%2
    print("│", end="")
    for i in range((56-len(enemy.name))//2):
        print(" ", end="")
    print(enemy.name, end="")
    for i in range((56-len(enemy.name))//2+f):
        print(" ", end="")
    print("|")

def buff_hp(enemy):
    hp = str(enemy.hp) + "/" + str(enemy.hpmax)
    if enemy.hp > 9:
        print("│       strengh : " + str(enemy.strengh) + "                    hp : " + hp, end="")
    else:
        print("│       strengh : " + str(enemy.strengh) + "                    hp : " + hp, end="")
    for i in range(13-len(hp)):
        print(" ", end="")
    print("│")
        


def action_shield(enemy):
    line = "│       shield : " + str(enemy.shield)
    action = enemy.p[0] + " : " + str(enemy.statAction())
    for i in range(13-(len(action)//2+len(action)%2)-(len(str(enemy.shield)))):
        line += " "
    line += action
    for i in range(27-len(action)//2):
        line += " "
    print(line + "│")


def lineVoid():
    print("│                                                        │")
