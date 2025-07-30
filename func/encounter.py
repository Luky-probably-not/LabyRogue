from func.enemies import *
from func.action import *
from func.player import *
from func.shop import *
import time
class Encounter:

    def __init__(self,name,kind):
        self.name = name
        self.type = type(kind)
        self.info = kind

    def Encounter(self,p1):
        checkHP = True
        if self.type == Enemy:
            self.info = self.info
            while self.info.hp > 0 and checkHP:
                checkHP = Turn(p1,self.info)
            if checkHP:
                gold = rand.randint(15,25)
                print("Gold gained : " + str(gold))
                p1.gold += gold
            return checkHP
        elif self.type == Shop:
            time.sleep(1)
            self.info.interact(p1)
        return True