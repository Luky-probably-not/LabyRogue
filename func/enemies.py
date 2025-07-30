import random as rand

class Enemy:

    def __init__(self,enemyDic):
        self.n = enemyDic["nom"][0]
        self.name = enemyDic["nom"]
        self.a = enemyDic["atk"]
        self.d = enemyDic["def"]
        self.buff = rand.randint(1,3)
        self.hpmax, self.hp = enemyDic["hp"], enemyDic["hp"]
        self.strengh = 0
        self.p = enemyDic["patern"]
        self.shield = 0
        self.role = "enemy"

    def __repr__(self):
        return "(" + self.name + ", " + str(self.a) + ", " + str(self.d) + ", " + str(self.hp) + ", " + str(self.p) + ")\n"
    
    def statAction(self):
        p = self.p[0]
        if p == "atk":
            return self.a + self.strengh
        elif p == "def" or p == "heal":
            return self.d
        elif p == "buff":
            return self.buff
        elif p == "crit":
            return (self.a  + self.strengh) * 2

def InitMobs():
    zombie = Enemy({"nom" : "zombie", "atk" : 4, "def" : 3, "hp" : 50, "patern" : ["def","atk","atk","def","buff"]})
    boss = Enemy({"nom" : "boss", "atk" : 8, "def" : 11, "hp" : 150, "patern" : ["atk", "def", "def", "buff", "crit", "heal"]})
    squelette = Enemy({"nom" : "squelette", "atk" : 7, "def" : 8, "hp" : 40, "patern" : ["atk","def","crit","def","heal"]})
    harpie = Enemy({"nom" : "harpie","atk" : 6,"def" : 5, "hp" : 70, "patern" : ["def","buff","atk","crit","heal"]})
    return [zombie,squelette,harpie,boss]
