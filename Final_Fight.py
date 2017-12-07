

#written in Python 3.5
#Final Fight main script

#modules
import random
import enemies #enemy roster
import conflict #'fighting script'
import title

#toggle switches for simplistic menu navigation
gameOn = False
battleOn = False
menuOn = False
shopOn = False
fightOn = False

def playerCreate(name): #creates player and returns values in a list
    name = name
    maxHealth = 100
    health = maxHealth
    attack = 35
    maxEnergy = 75
    energy = maxEnergy
    money = 100
    potions = 0
    energyFill = 0
	
    if name == "MoneyBagz":
        money = 500
    elif name == "BeefCake":
        attack = 55
    elif name == "GODMODE":
        maxHealth = 75
        health = maxHealth
        attack = 25
        maxEnergy = 50
        energy = maxEnergy
        money = 100
        potions = 0
        energyFill = 0
    elif name == "Prepared":
        money = 200
        potions = 4
        energyFill = 5
    elif name == "HeartDruid1":
        print('THE ALMIGHTY CREATOR!')
        name = name
        maxHealth = 200
        health = maxHealth
        attack = 50
        maxEnergy = 100
        energy = maxEnergy
        money = 400
        potions = 5
        energyFill = 5
		
    return [name,health,maxHealth,attack,energy,maxEnergy,money,potions,energyFill]

def menu(player): # main menu; returns the menuchoice in lowercase
    print('-----------------')
    print('Welcome',player[0])
    print('-----------------')
    print('Battle *Arena*')
    print('*Shop*')
    print('*Stats*')
    menuChoice = input('>>> ')

    return menuChoice.lower()

def battleGenerator(): # selects enemies from a list and returns the results like the player character
    enemyList = [enemies.BrilliantBlue(),enemies.ShadowKnight(),
                enemies.BlackMagic(),enemies.BrassKnuckles(),enemies.OrangeClockwork(),
                enemies.SoylentGreen(),enemies.KingCrimson()]
    enemy = random.choice(enemyList)

    return enemy

def stats(character):
    print('-----------------')
    print("Name: ",character[0])
    print("Health: ",character[1],'/',character[2])
    print("Attack: ",character[3])
    print("Energy: ",character[4],'/',character[5])
    print("Money: ",character[6])
    print("Potions: ",character[7])
    print("Energy Fills:",character[8])

def battleMenu():
    print('-----------------')
    print('Welcome',player[0])
    print('*Fight*')
    print('*Shop*')
    print('*Stats*')
    menuChoice = input('>>> ')

    return menuChoice.lower()

def shops():
    print('-----------------')
    print('Welcome to the Shop')
    print('*Potion* = 50$')
    print('*Energy* Refill = $25')
    print('Go *Back*')
    purchase = input('What would you like to buy? ').lower()

    return purchase

if __name__ == '__main__':
    title.title()
    print('----------------------')
    print('github/HeartDruid1')
    print('----------------------')
    input('"Press Enter To Start"')
    print('What is your name?')
    playerName = input('>>> ')
    player = playerCreate(playerName)
    menuOn = True

while True: #game loop so that any 'back' keywords don't end script
    while menuOn:
        menuSelect = menu(player)
        if menuSelect == 'arena':
            battleOn = True
            menuOn = False
        elif menuSelect == 'shop':
            shopOn = True
            menuOn = False
        elif menuSelect =='stats':
            stats(player)
        elif menuSelect == 'exit':
            quit()
        else:
            menuSelect = menu(player)

    while battleOn:
        enemy = battleGenerator()
        battleChoice = battleMenu()
        if battleChoice == 'fight':
            #assigned here to avoid repetition in fight loop
            enemy[1] = enemy[2] #enemy health at full
            enemy[4] = enemy[5] #enemy energy at full
            player[4] = player[5] #player energy at full
            fightOn = True
            battleOn = False
        elif battleChoice == 'stats':
            stats(player)
        elif battleChoice == 'shop':
            shopOn = True
            battleOn = False
        elif menuSelect == 'exit':
            quit()
        else:
            battleChoice = battleMenu()

    while shopOn:
        purchase = shops()
        if purchase == 'potion':
            if player[6] >= 50:
                player[6] -= 50
                player[7] += 1
                print('Thank you, you now have',player[7],'potions')
            else:
                print("You don't have enough money for that")
        elif purchase == 'energy':
            if player[6] >= 25:
                player[8] += 1
                player[6] -= 25
                print('Thank you, you now have',player[8], 'energy fills')
            else:
                print("You don't have enough money for that")
        else:
            shopOn = False
            menuOn = True

    while fightOn:
        if player[1] >= 0:#If player health is bigger than 0
            fightCard = conflict.conflictMain(player, enemy) #The battle menu and choices
            if fightCard == 'attack':
                if player[4] > 0: #if the player's energy is above 0
                    enemyHealth = conflict.mechanicsEnemy(player, enemy) #recieves enemy health from battle
                    #evaluation for continuing battle
                    if enemyHealth <= 0:
                        conflict.victory(player, enemy)
                        menuOn = True
                        fightOn = False
                    else: #if the enemy is still alive, attack player
                        if enemy[4] > 0:
                            playerHealth = conflict.mechanicsPlayer(player, enemy) #recives player health from battle
                            #if the player is 'dead' end game
                            if playerHealth <= 0:
                                print('Sorry, you lost')
                                print('Game Over')
                                stats(player)
                                quit()
                        else:
                            enemy[4] = 0
                            print('The enemy has no more energy to attack, you can win this!')
                else:
                    player[4] = 0
                    print('You do not have enough energy to attack')
                    playerHealth = conflict.mechanicsPlayer(player, enemy) #recives player health from battle
                    #if the player is 'dead' end game
                    if playerHealth <= 0:
                        print('Sorry, you lost')
                        print('Game Over')
                        stats(player)
                        quit()
            if fightCard == 'potion':
                if player[7] > 0:
                    player[7] -= 1
                    player[1] += 20
                    if player[1] > player[2]:
                        player[1] = player[2]
                    print('You now have ',player[7],'potions left')
                    print('You now have ',player[1],'health')
                else:
                    print('You have no remaining potions')
            if fightCard == 'energy':
                if player[8] > 0:
                    player[8] -= 1
                    player[4] = player[5]
                    print('You now have ',player[8],'refills left')
                    print('You now have ',player[4],'energy to attack')
                else:
                    print('You have no remaining refills')
            if fightCard == 'flee':
                flee = conflict.flee(player, enemy)
                if flee == False:
                    conflict.mechanicsPlayer(player, enemy)
                if player[1] <= 0:
                    print('Sorry, you lost')
                    print('Game Over')
                    stats(player)
                    quit()
