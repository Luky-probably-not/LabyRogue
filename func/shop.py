from func.cards import *
import random as rand
from readchar import readkey,key
import time
class Shop:

    def __init__(self):
        self.name = "shop"
        self.cards = []
        self.Available()
        self.offer = []
        for i in self.cards:
            self.offer.append(Offer(i,rand.randint(15,25)))
        self.indexCards = []
        for i in range(len(self.offer)):
            self.indexCards.append(str(i+1))
        return
    
    def __repr__(self):
        for i in range(len(self.offer)):
            self.offer[i].print(str(self.indexCards[i]))
        return ""

    def Available(self):
        cards = [   Card("Strike","atk",5),
                    Card("Block", "def", 5),
                    Card("First Heal", "heal", 2),
                    Card("Concentrate", "buff",1)
                ]
        for i in range(3):
            for f in cards:
                self.cards.append(f)
        for i in range(5):
            self.cards.pop(rand.randint(0,len(self.cards)-1))
    
    def interact(self,player):
        choice = ""
        while choice != "q" and choice != key.ENTER:
            print("\033c")
            print(self)
            print("Your money : ", player.gold)
            print("What card would you like to buy ? (press q to quit the shop)")
            choice = readkey()
            while choice != "q" and choice != key.ENTER and choice not in self.indexCards:
                print("Bad input")
                choice = readkey()
            if choice != "q" and choice != key.ENTER:
                self.buy(self.offer[self.indexCards.index(choice)],player)
                self.indexCards.remove(choice)
        
    def buy(self,offer,player):
        if player.gold < offer.price:
            print("Not enough money")
            time.sleep(1)
            return
        else:
            player.pioche.append(offer.card)
            self.offer.remove(offer)
            player.gold -= offer.price
            print(offer.card, " bought for " + str(offer.price) + " gold.")
            time.sleep(1)
                  
class Offer:

    def __init__(self,card,price):
        self.card = card
        self.price = price
    
    def print(self,index):
        print(str(index) + " - " + str(self.card) + " : " + str(self.price) + " coins")