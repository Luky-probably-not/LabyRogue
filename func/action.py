import time
from func.display import display
from readchar import readkey,key
import random
import copy

def Turn(player,enemy):
    time.sleep(1)
    StartTurn(player)
    display(player,enemy)
    while enemy.hp > 0 and player.m != 0:
        playerAction(player,enemy)
        loseHP(enemy)
    player.endTurn()
    if enemy.hp > 0:
        enemy.shield = 0
        enemyAction(player,enemy)
        loseHP(player)
    display(player,enemy)
    return player.hp > 0

def enemyAction(player,enemy):
    action = enemy.p[0]
    if action == "atk":
        attack(enemy.a,player)
    elif action == "def":
        enemy.shield += enemy.d
    elif action == "buff":
        enemy.a += enemy.buff
    elif action == "heal":
        gainHP(enemy,enemy.d)
    elif action == "crit":
        attack(enemy.a*2,player)
    enemy.p.append(action)
    enemy.p.remove(action)
    time.sleep(1)
    display(player,enemy)
    
def playerAction(player,enemy):
    print("What card to play ?")
    k = readkey()
    while k != "1" and k != "2" and k != "3" and k != "q" and k != "Q" and k != "p":
        print("bad input")
        k = readkey()
    if k == "q" or k == "Q":
        player.m = 0
        return
    if k == "p":
        enemy.hp = 0
        return
    action(player,int(k)-1,enemy)
    display(player,enemy)
    time.sleep(1)

def action(player,index,enemy):
    card = player.hand[index]
    playedCard =copy.deepcopy(card)
    action = card.eff
    if action == "atk":
        attack(card.s + player.strengh,enemy)
        playedCard.s += player.strengh

    elif action == "def":
        player.shield += (card.s + player.resis)
        playedCard.s += player.resis
    elif action == "heal":
        gainHP(player,card.s)
    elif action == "buff":
        if random.choice([True,False]):
            player.strengh += 1
        else:
            player.resis += 1
        player.m += 1
    player.hunter(enemy)
    player.updateHand(index)
    player.m -= 1
    print(playedCard)

def round(player):
    player.strengh = 0
    player.resis = 0
    player.shuffleHand()

def attack(atk,tank):
    if tank.shield > atk:
        tank.shield -= atk
    else:
        tank.hp -= atk - tank.shield
        if tank.role == "player":
            tank.barbarian(atk-tank.shield)
        tank.shield = 0
    loseHP(tank)

def gainHP(entity,heal):
    entity.hp += heal
    if entity.hp > entity.hpmax:
        entity.hp = entity.hpmax

def loseHP(entity):
    if entity.hp <= 0:
        entity.hp = 0

def StartTurn(player):
    player.shield = 0
    player.m = player.mmax
    player.strengh += player.tstrengh
    player.resis += player.tresis
