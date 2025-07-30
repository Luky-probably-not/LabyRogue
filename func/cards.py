from random import shuffle

class Card:

    def __init__(self,nom,effet,stat):
        self.n = nom
        self.eff = effet
        self.s = stat
    
    def __repr__(self):
        return "("  + self.n + ", " + self.eff + ", " + str(self.s) + ")"
    
def InitCards():
    frappe = Card("Strike","atk",5)
    defense = Card("Block", "def", 5)
    soin = Card("First Heal", "heal", 2)
    boost = Card("Concentrate", "buff", 1)
    l = [frappe,frappe,frappe,defense,defense,soin,boost]
    shuffle(l)
    return l