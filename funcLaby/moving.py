from readchar import readkey,key
from funcLaby.labyGenerator import *
from funcLaby.mazeSolver import *


def move(laby):
    finish = False
    count = 0
    while not finish:
        p1 = where(laby)
        input = readkey()
        list_input = [key.UP,key.DOWN,key.RIGHT,key.LEFT]
        while input not in list_input or not check(laby,p1,input):
            print("bad input")
            input = readkey()
        finish, laby = moving(laby,p1,input)
        count += 1
        laby.display()
    sol = Resolve(laby)
    sol[1].display()
    print("You win. Here is the fastest way possible")
    print("Your score : " + str(count))
    print("Best score possible : " + str(sol[0]))

def where(laby):
    for i in range(laby.l):
        for f in range(laby.l):
            if laby.m[i][f].type == "P":
                return (i,f)
            elif laby.m[i][f].type == "A":
                A = (i,f)
    return A

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
    
def moving(laby,p1,input):
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
    laby.m[lig_p1+NS][col_p1+WE].type = "P"
    return finish, laby