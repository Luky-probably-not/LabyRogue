import random as rand
class Case:

    def __init__(self,id,type):
        self.id = id
        self.n = True
        self.e = True
        self.s = True
        self.w = True
        if type == 0:
            self.type = " "
        else:
            self.type = type

    
    def __repr__(self):
        return str(self.id) + ", " + str([self.n,self.e,self.s,self.w])
    
class Laby:


    def __init__(self,n):
        events = []
        total = n*n
        for i in range(total//20):
            events.append("s")
        for i in range(total//25):
            events.append("b")
        for i in range(total//10):
            events.append("m")
        for i in range(total-len(events)):
            events.append(0)

        M = []
        id = 0
        line = []
        for i in range(n):
            line = []
            for f in range(n):
                choice = rand.randint(0,len(events)-1)

                line.append(Case(id,events[choice]))
                events.remove(events[choice])
                id += 1
            M.append(line)
        self.m = M
        self.l = len(self.m)
        self.Start("A")

    def __repr__(self):
        return str(self.m)
    
    def displayID(self):
        print("\033c")
        self.displayTop()
        for i in range(self.l-1):
            self.displayLineID(self.m[i])
            self.displaySeparator(i)
        self.displayLineID(self.m[-1])
        self.displayBot()
        return
    
    def display(self):
        print("\033c")
        self.displayTop()
        for i in range(self.l-1):
            self.displayLine(self.m[i])
            self.displaySeparator(i)
        self.displayLine(self.m[-1])
        self.displayBot()
    
    def displayTop(self):
        print("┌",end="")
        for i in range(self.l-1):
            print("───",end="")
            if self.m[0][i].e:
                print("┬",end="")
            else:
                print("─",end="")
        print("───",end="")
        print("┐")

    def displayBot(self):
        print("└",end="")
        for i in range(self.l-1):
            print("───",end="")
            if self.m[-1][i].e:
                print("┴",end="")
            else:
                print("─",end="")
        print("───",end="")
        print("┘")

    def displayLineID(self,line):
        print("│",end="")
        for i in range(self.l-1):
            print(" "+str(line[i].id)+" ",end="")
            if line[i].e:
                print("│",end="")
            else:
                print(" ",end="")
        print(" "+str(line[-1].id)+" ",end="")
        print("│")
    
    def displayLine(self,line):
        print("│",end="")
        for i in range(self.l-1):
            print(" "+str(line[i].type)+" ",end="")
            if line[i].e:
                print("│",end="")
            else:
                print(" ",end="")
        print(" "+str(line[-1].type)+" ",end="")
        print("│")
    


    def displaySeparator(self,idLine):
        case = self.m[idLine][0]
        if case.s:
            print("├",end="")
        else:
            print("│",end="")
        for i in range(self.l-1):
            case = self.m[idLine][i]
            caseMirror = self.m[idLine+1][i+1]
            if case.s:
                print("───",end="")
            else:
                print("   ",end="")
            print(self.cross(case,caseMirror),end="")
        if self.m[idLine][-1].s:
            print("───┤")
        else:
            print("   │")
                
    def cross(self,case,caseMirror):
        if case.s:
            if case.e:
                if caseMirror.w:
                    if caseMirror.n:
                        return "┼"
                    else:
                        return "┤"
                else:
                    if caseMirror.n:
                        return "┴"
                    else:
                        return "┘"
            else:
                if caseMirror.w:
                    if caseMirror.n:
                        return "┬"
                    else:
                        return "┐"
                else:
                    if caseMirror.n:
                        return "─"
                    else:
                        return " "
        else:
            if case.e:
                if caseMirror.w:
                    if caseMirror.n:
                        return "├"
                    else:
                        return "│"
                else:
                    if caseMirror.n:
                        return "└"
                    else:
                        return " "
            else:
                if caseMirror.w:
                    if caseMirror.n:
                        return "┌"
                    else:
                        return " "
                else:
                    return " "
        return " "

    def Start(self,case):
        if case == "A":
            self.m[0][0].type = case
        elif case == "B":
            self.m[self.l-1][self.l-1].type = case
    
    def Empty(self):
        for i in range(self.l):
            for f in range(self.l):
                self.m[i][f].type = " "
        self.Start("A")
        self.Start("B")


def Random(n):
    laby = Laby(n)
    maze = laby.m
    while check(maze):
        idLig = rand.randint(0,len(maze)-1)
        idCol = rand.randint(0,len(maze[idLig])-1)
        choice = rand.randint(0,3)
        while not checkDirection(maze,idLig,idCol,choice):
            choice = rand.randint(0,3)
        if not checkId(maze,idLig,idCol,choice):
            continue
        elif maze[idLig][idCol].id == 0:
            continue
        maze = connect(maze,idLig,idCol,choice)

    laby.m = maze
    return laby

def checkDirection(laby,idLig,idCol,choice):
    if idLig == 0 and choice  == 0:
        return False
    elif idLig == len(laby)-1 and choice == 2:
        return False
    elif idCol == 0 and choice == 3:
        return False
    elif idCol == len(laby[idLig])-1 and choice == 1:
        return False
    return True

def checkId(laby,idLig,idCol,choice):
    if choice == 0:
        dir = laby[idLig-1][idCol]
    elif choice == 2:
        dir = laby[idLig+1][idCol]
    elif choice == 1:
        dir = laby[idLig][idCol+1]
    elif choice == 3:
        dir = laby[idLig][idCol-1]
    if dir.id == laby[idLig][idCol].id:
        return False
    else:
        return True

def connect(laby,idLig,idCol,choice):
    center = laby[idLig][idCol]
    NS = 0
    WE = 0
    if choice == 0:
        dir = laby[idLig-1][idCol]
        NS = -1
        direction = "n"
    elif choice == 1:
        dir = laby[idLig][idCol+1]
        direction = "e"
        WE = 1
    elif choice == 2:
        dir = laby[idLig+1][idCol]
        direction = "s"
        NS = 1
    elif choice == 3:
        dir = laby[idLig][idCol-1]
        direction = "w"
        WE = -1
    keepId = min(center.id,dir.id)
    loseId = max(center.id,dir.id)
    laby = lose(laby,keepId,loseId)
    if direction == "n":
        center.n = False
        dir.s = False
    elif direction == "e":
        center.e = False
        dir.w = False
    elif direction == "s":
        center.s = False
        dir.n = False
    elif direction == "w":
        center.w = False
        dir.e = False
    laby[idLig][idCol] = center
    laby[idLig+NS][idCol+WE] = dir

    return laby

def lose(laby,keepid,loseid):
    for i in range(len(laby)):
        for f in range(len(laby[i])):
            if laby[i][f].id == loseid:
                laby[i][f].id = keepid
    return laby

def check(laby):
    for i in range(len(laby)):
        for f in range(len(laby[i])):
            if laby[i][f].id != 0:
                return True
    return False



