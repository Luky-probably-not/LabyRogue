from func.labyGenerator import *
from copy import deepcopy

def Resolve(laby):
    maze = deepcopy(laby)
    xA = yA = 0
    xB = yB = laby.l-1
    maze.m[xA][yA].id = 'A'
    maze.m[xB][yB].id = 'B'
    path = Path(maze,xA,yA)
    rev = ReversePath(path,maze)
    maze = solve(rev,maze)
    maze = beauty(maze)
    return len(rev)-1, maze



def Path(maze,x,y):
    chemin = []
    for i in range(0,maze.l):
        ligne=[]
        for j in range(0,maze.l):
            ligne+=[1000]
        chemin+=[ligne]
    chemin[x][y] = 0
    index = 0
    end = False
    while not end:
        end = True
        for i in range(maze.l):
            for f in range(maze.l):
                if chemin[i][f] == index:
                    if not maze.m[i][f].n:
                        Indice(chemin,i-1,f,index)
                    if not maze.m[i][f].e:
                        Indice(chemin,i,f+1,index)
                    if not maze.m[i][f].s:
                        Indice(chemin,i+1,f,index)
                    if not maze.m[i][f].w:
                        Indice(chemin,i,f-1,index)
                    end = False
        index += 1
    return chemin

def Indice(chemin,i,f,index):
    if chemin[i][f] > index+1:
        chemin[i][f] = index+1
    return chemin

def ReversePath(path,maze):
    xA = yA = 0
    x = y = maze.l-1
    way = [(x,y)]
    while x != xA or y != yA:
        x,y = checkSmall(path,x,y,maze)
        way += [(x,y)]
    return reverse(way)

    
def checkSmall(path,x,y,maze):
    index = []
    indexList = []
    if x > 0 and not maze.m[x][y].n:
        index += [path[x-1][y]]
        indexList += [(x-1,y)]
    if y > 0 and not maze.m[x][y].w:
        index += [path[x][y-1]]
        indexList += [(x,y-1)]
    if x < len(path)-1 and not maze.m[x][y].s:
        index += [path[x+1][y]]
        indexList += [(x+1,y)]
    if y < len(path[x])-1 and not maze.m[x][y].e:
        index += [path[x][y+1]]
        indexList += [(x,y+1)]
    return smaller(index,indexList)

def smaller(index,indexList):
    if index[0] != "W":
        min = index[0]
    else:
        min = 1000
    id = indexList[0]
    for i in range(len(index)):
        if index[i] != "W":
            if min > index[i]:
                min = index[i]
                id = indexList[i]
    return id
 
def reverse(l):
    final = []
    for i in range(1,len(l)):
        final += [l[-i]]
    final += [l[0]]
    return final

def solve(path,maze):
    index = 0
    for i in path:
        maze.m[i[0]][i[1]].id = index
        index += 1
    return maze

def beauty(maze):
    for i in range(maze.l):
        for f in range(maze.l):
            if maze.m[i][f].id != 0:
                maze.m[i][f].type = 1
    maze.m[0][0].type = "A"
    maze.m[maze.l-1][maze.l-1].type = "B"
    return maze

