import classesV1
from random import randint

#battle system
def fight(atker, dfnder):
    dmg = randint(atker.atk[0],atker.atk[1])
    dfnderHP = dfnder.sStats["Health"]
    dfnderHP = dfnderHP - dmg
    dfnder.sStats["Health"] = dfnderHP

    if dfnderHP <= 0:
        print ("{} has been slain" .format(dfnder.name))

        if isinstance(atker, classes.Hero):
            lvler(atker, dfnder.xpG)
            print ("{} gainned {} XP\n" .format(atker.name,dfnder.xpG))
            print (atker.profile())
        else:
            print ("GAME OVER: {} has fallen" . format(dfnder.name))
            print ("{} devours {}'s lifeless corpse" . format(atker.name,dfnder.name))
    else:
        print ("{} takes {} damage!".format(dfnder.name, dmg))

def commands(fghter1, fghter2):

    while fghter2.sStats["Health"] > 0:
        cmd = input("Do you want to attack {}? yes/no:".format(fghter2.name)).lower()
        if 'yes' in cmd:
            fight(fghter1, fghter2)

        elif 'no' in cmd:
            print("{} attacks viciously!".format(fghter2.name))
            fight(fghter2, fghter1)
            if fghter1.sStats["Health"] <= 0:
                break
        else:
            pass

#Leveling Up
def lvler(hero, xpG):
    xpg = hero.xp
    xpG = xpg + xpG
    if xpG < hero.lvlNxt: # if XP gained is not enough level
        hero.xp = xpG
        return (hero)

    while xpG >= hero.lvlNxt: # xp gained enough to level loop
        hero.lvl = hero.lvl + 1 # raise level
        hero.sStats["Health"] = round(hero.hpMax * 1.2) #raise HP
        hero.hpMax = round(hero.hpMax * 1.2) #raise HPMax
        hero.sStats["Speed"] = round(hero.sStats["Speed"] * 1.2) #raise Speed
        hero.sStats["Evasion"] = round(hero.sStats["Evasion"] * 1.2)  # raise Evasion
        xpG = xpG - hero.lvlNxt
        hero.xp = xpG
        hero.lvlNxt = round(hero.lvlNxt * 1.5)
    return (hero)



#equipping items to hero
def Equip (hero, item):
    atk = item.atk
    dfn = item.dfn
    mana = item.mana


    if (item.type == "accessory"):
        hero.acc = item.name
        hero.mana = mana #accessory affects mana
    if (item.type == "weapon"):
        hero.wea = item.name
        hero.atk = atk #weapon affects Attack
    if (item.type == "armour"):
        hero.arm = item.name
        hero.dfn = dfn #armour affects defence

#calculating secondary stats
def hpCalc(vit, proff): #Health
    hp = vit * 1.6
    if proff == "Warrior": #Warriors get extra Health
        hp += 5
    return round(hp)
def spdCalc(dex, proff): #Speed
    spd = dex * 1.6
    if proff == "Archer": #Archers get extra Speed
        spd += 5
    return round(spd)
def evaCalc(int, proff): #Evasion
    eva = int * 1.6
    if proff == "Mage": #Mages get extra Evasion
        eva += 5
    return round(eva)




