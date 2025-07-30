from func.labyGenerator import *
from func.mazeSolver import *
from func.moving import *
from func.encounter import *
import random as rand

def checkAround(laby,id):
    x,y = id
    return (not laby.m[x][y].n and not laby.m[x][y].w and not laby.m[x][y].s and not laby.m[x][y].e)

def addInPath(laby,size,type):
    path = ReversePath(Path(laby,0,0),laby)
    gap = size
    for i in range(len(path)):
        if gap == 0:
            if laby.m[path[i][0]][path[i][1]].type == " ":
                laby.m[path[i][0]][path[i][1]].type = type
                gap = size
            else:
                gap += 1
        gap -= 1
    return laby

def addOutPath(laby,type,nb):
    path = ReversePath(Path(laby,0,0),laby)
    i = nb
    for i in range(nb):
        x = rand.randint(0,laby.l-1)
        y = rand.randint(0,laby.l-1)
        while lookList(path,(x,y)) and laby.m[x][y] != " ":
            x = rand.randint(0,laby.l)
            y = rand.randint(0,laby.l)
        laby.m[x][y].type = type
    return laby

def lookList(list,tuple):
    a, b = tuple
    for i in range(len(list)):
        if list[i][0] == a and list[i][1] == b:
            return True
    return False

def FillLaby(laby):
    laby = addInPath(laby,15,"h")
    laby = addInPath(laby,9,"s")
    laby = addInPath(laby,40,"b")
    laby = addOutPath(laby,"S",3)
    laby = addOutPath(laby,"z",9)
    return laby



