from readchar import readkey,key # type: ignore
from func.labyGenerator import *
from func.mazeSolver import *
from func.encounter import *
from func.start import *
from func.action import *
from func.enemies import *
import copy 
import random as rand 


def play(laby):
    player,mobs = InitGameLaby()
    laby.display()
    laby = fillLaby(laby,mobs)
    finish = False
    count = 0
    while not finish:
        p1 = where(laby)
        input = readkey()
        list_input = [key.UP,key.DOWN,key.RIGHT,key.LEFT]
        while input not in list_input or not check(laby,p1,input):
            print("bad input")
            input = readkey()
        finish, laby,checkHP = moving(laby,p1,input,player)
        if not checkHP:
            break
        round(player)
        count += 1
        laby.display()
    if checkHP:
        score,sol = Resolve(laby)
        print("You win.")
    else:
        print("You lose")

def where(laby):
    for i in range(laby.l):
        for f in range(laby.l):
            if laby.m[i][f].type == "P":
                return (i,f)
            elif laby.m[i][f].type == "A":
                A = (i,f)
    return (0,0)

def check(laby,p1,input):
    lig_p1, col_p1 = p1
    if laby.m[lig_p1][col_p1].n and input == key.UP:
        return False
    elif laby.m[lig_p1][col_p1].s and input == key.DOWN:
        return False
    elif laby.m[lig_p1][col_p1].w and input == key.LEFT:
        return False
    elif laby.m[lig_p1][col_p1].e and input == key.RIGHT:
        return False
    else:
        return True
    
def moving(laby,p1,input,player):
    checkHP = True
    lig_p1, col_p1 = p1
    NS = WE = 0
    if input == key.DOWN:
        NS = 1
        laby.m[lig_p1][col_p1].type = " "
    elif input == key.UP:
        NS = -1
        laby.m[lig_p1][col_p1].type = " "
    elif input == key.RIGHT:
        WE = 1
        laby.m[lig_p1][col_p1].type = " "
    elif input == key.LEFT:
        WE = -1
        laby.m[lig_p1][col_p1].type = " "
    if laby.m[lig_p1+NS][col_p1+WE].type == "B":
        finish = True
    else:
        finish = False
    p1 = where(laby)
    listType = ["B","A"," "]
    if laby.m[lig_p1+NS][col_p1+WE].type not in listType:
        checkHP = laby.m[lig_p1+NS][col_p1+WE].info.Encounter(player)
    laby.m[lig_p1+NS][col_p1+WE].type = "P"
    return finish, laby,checkHP

def fillLaby(laby,mobs):
    for i in range(laby.l):
        for f in range(laby.l):
            if laby.m[i][f].type == "b":
                laby.m[i][f].info = copy.deepcopy(mobs[3])
            elif laby.m[i][f].type == "S":
                laby.m[i][f].info = Encounter("Magasin",Shop())
            elif laby.m[i][f].type == "s":
                laby.m[i][f].info = copy.deepcopy(mobs[1])
            elif laby.m[i][f].type == "h":
                laby.m[i][f].info = copy.deepcopy(mobs[2])
            elif laby.m[i][f].type == "z":
                laby.m[i][f].info = copy.deepcopy(mobs[0])
    return laby
