from functionsV1 import *

# Hero class
class Hero:
    name = ""
    proff = ""
    affin = ""
    lvl = 1
    mana = 0
    hpMax = 10
    xp = 0
    lvlNxt = 10
    atk = [1,2]
    dfn = 0
    arm = "nekkid"
    wea = "unarmed"
    acc = "none"
    pStats = {"Vitality": 0, "Dexterity": 0, "Intelligence": 0}
    sStats = {"Health":0, "Speed": 0, "Evasion":0}

# constructor
    def __init__(self, name, proff, pstats, affin):
        self.name = name
        self.proff = proff
        self.pStats["Vitality"] = pstats
        self.affin = affin
        self.sStats["Health"] = hpCalc(pstats[0], proff) #use health function to calculate
        self.sStats["Speed"] = spdCalc(pstats[1], proff) #use speed function to calculate
        self.sStats["Evasion"] = evaCalc(pstats[2], proff) #use evasion function to calculate
        self.hpMax = hpCalc(pstats[0], proff)

    #ignore - for future use - base stat for secondary stats that change with equiped item
    #http://stackoverflow.com/questions/31950236/python-text-based-game-equip-armor-stats
    # @property
    # def defx(self):
    #     dfn = self.dfn
    #     if self.arm =="Coat":
    #         dfn += 10
    #     return dfn
    # @property
    # def manax(self):
    #     mana = self.mana
    #     if self.acc == "Blessed Pin":
    #         mana += 10
    #     return mana

    # Hero Profile method
    def profile(self):
        return "Name: {}\nClass: {}\nElement: {}\nLevel: {}\nWeapon: {}\nArmour: {}\nAccessory: {}\nAttack: {}\nDefence: {} \
                \nMana: {}\nHP: {}\nSpeed: {}\nEvasion: {}".format(self.name, self.proff, self.affin, self.lvl, self.wea, self.arm, self.acc,
                self.atk, self.dfn, self.mana, self.sStats["Health"], self.sStats["Speed"],self.sStats["Evasion"])

#Basic Enemy
class Enemy0:
    name = ""
    lvl = 0
    xpG = 10
    atk = [1,2]
    dfn = 0
    loot = []
    sStats = {"Health": 5, "Speed": 0, "Evasion": 0}

    def __init__(self, name):
        self.name = name

#Item
class Item:
    id = 0
    name = ""
    type = ""
    atk = []
    dfn = 0
    spd = 0
    mana = 0

    def __init__(self, id, name, type, atk, dfn, mana):
        self.id = id
        self.name = name
        self.type = type
        self.atk = atk
        self.dfn = dfn
        self.mana = mana


