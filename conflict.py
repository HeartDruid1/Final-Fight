#conflict.py
from random import randint

def conflictMain(player, enemy):
    print('--------------------------------')
    print(player[0])
    print('Health: ',player[1],'/',player[2])
    print('Energy: ',player[4],'/',player[5])
    print('VS.')
    print(enemy[0])
    print('Health: ',enemy[1],'/',enemy[2])
    print('Energy: ',enemy[4],'/',enemy[5])
    print('--------------------------------')
    print('*Attack*')
    print('Drink *Potion*')
    print('Refill *Energy*')
    print('Attempt *Flee*?')
    battleMove = input('>>> ')

    return battleMove.lower()

def victory(player,enemy):
    print('You have successfully defeated ',enemy[0])
    print('You have won ',player[1],'dollars.')
    player[6] += player[1]
    print('Congratulations!')

def mechanicsEnemy(player, enemy):
    fight = randint(player[3]//2, player[3])
    if fight == player[3]:
        print('Your attack missed, no damage was delt')
    else:
        enemy[1] -= fight
        player[4] -= fight//2
        print('You delt',fight,'damage')

    return enemy[1]

def mechanicsPlayer(player, enemy):
    enemyFight = randint(enemy[3]//2,enemy[3])
    if enemyFight == enemy[3]//2:
        print('You took no damage from the enemy',enemy[0])
    else:
        enemy[4] -= enemyFight//2
        player[1] -= enemyFight
        print('You took ',enemyFight,'damage')

    return player[1]

def flee(player, enemy):
    chance = randint(0,player[4])
    if chance == player[4]:
        print('You have successfully fleed')
        fightOn = False
        menuOn = True
    else:
        print('You could not flee')
        flee = False

        return flee
