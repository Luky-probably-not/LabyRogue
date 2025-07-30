from func.action import * 
from func.cards import *
from func.display import *
from func.player import *
from func.encounter import *
from func.shop import*
from readchar import readkey,key # type: ignore
import copy

def start():
    deck = InitCards()
    p1 = Player(3,30,deck)
    print("What class would you like to play ?")
    print("     -hunter     (h)  : deal 2 damage every card played")
    print("     -mage       (m)  : gain +1 mana max")
    print("     -barbarian  (b)  : gain temporal strengh when you receive damage")
    p1.rank = readkey()
    while p1.rank != "h" and p1.rank != "m" and p1.rank != "b":
        print("Bad input, try again")
        p1.rank = readkey()
    if p1.rank == "h":
        print("Class : Hunter")
        p1.rank = "hunter"
    elif p1.rank == "m":
        print("Class : Mage")
        p1.rank = "mage"
    elif p1.rank == "b":
        print("Class : Barbarian")
        p1.rank = "barbarian"
    p1.mage()
    return p1, InitMobs()

def InitGameLaby():
    p1,mobs = start()
    mobs[0] = Encounter("Zombie",mobs[0])
    mobs[1] = Encounter("Squelette",mobs[1])
    mobs[2] = Encounter("Harpie",mobs[2])
    mobs[3] = Encounter("Boss",mobs[3])
    return p1,mobs