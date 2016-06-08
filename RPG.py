# RPG Character Creator version 3
# Version 1 can be found here: https://github.com/KelroyBrown/RPG_Chararacter/blob/master/charCreatorV1.py
# Version 2 can be found here: https://github.com/KelroyBrown/RPG_Chararacter/blob/master/charCreatorV2.py
# Based on and expanded from Charles Wade's original code from August of 2013
# Edits by Kelroy Brown - KelroyBrown.com - March 2016
# Learning and Experimenting with Python by doing fun mini projects

# import statements

import pickle
import os


# initialize variables

choice = None  # menu choices
chars = {}  # dictionary for characters

# constants or global variables

POOL = 30


#  Secondary Stats Functions
#  Health, Evasion, Physical Defence, Magic Defence, Physical Attack, Magic Attack, Speed and Mana

def hpCalc(vit, str, prof):
    hp = vit * str
    if prof == "Cleric":
        hp += 5
    return hp

def evaCalc(dex, lck, prof):
    eva = dex * lck
    if prof == "Monk":
        eva += 5
    return eva

def pDefCalc(str, vit, prof):
    pdef = str * vit
    if prof == "Fighter":
        pdef += 5
    return pdef

def mDefCalc(spi, wis):
    mdef = spi * wis
    return mdef

def pAttCalc(str, dex, prof):
    patt = str * dex
    if prof == "Rogue":
        patt += 5
    return patt

def mAttCalc(int, wis):
    matt = int * wis
    return matt

def spdCalc(vit, dex, prof):
    spd = vit * dex
    if prof == "Ranger":
        spd += 5
    return spd

def manaCalc(spi, int, prof):
    mana = spi * int
    if prof == "Mage":
        mana += 5
    return mana

# Character class
class Character:
    __name = ""
    __proff = ""
    __pStats = {}
    __sStats = {}
    __affin = ""

# constructor
    def __init__(self, name, proff, pstats, sstats, affin):
        self.__name = name
        self.__proff = proff
        self.__pStats = pstats
        self.__sStats = sstats
        self.__affin = affin
# setters
    def set_name(self, name):
        self.__name = name

    def set_proff(self, proff):
        self.__proff = proff

    def set_pStats(self, pstats):
        self.__pStats = pstats

    def set_sStats(self, sstats):
        self.__sStats = sstats

    def set_affin(self, affin):
        self.__affin = affin
# getters
    def get_name(self):
        return self.__name

    def get_proff(self):
        return self.__proff

    def get_pstats(self):
        return self.__pStats

    def get_stats(self):
        return self.__sStats

    def get_affin(self):
        return self.__affin

# Character Profile method
    def profile(self):
        return "Name: {}\nClass: {}\nElement: {}".format(self.__name, self.__proff, self.__affin)

# do the deed

while choice != "0":

    print("""
    Character Creator - version 3
    =================
    Originally written by Charles Wade in August of 2013
    Modified and expanded upon as a learning project by Kelroy Brown (KelroyBrown.com) in March 2016

    Please choose a number corresponding with a menu option below:

    0 - Quit Character Creator
    1 - Create New Character
    2 - Delete Character
    3 - List All Characters
    4 - Load All Characters
    5 - Erase All Characters
    """)

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye. Thank you for using the Character Creator")
        print(choice)
    # create new char
    elif choice == "1":
        pool = POOL  # get value from constant/global variable
        name = input("What name do you want your character to have?: ")
        while name == "":  # Check if name blank
            name = input("What name do you want your character to have?: ")
        cname = name.capitalize()
        if cname not in chars:  # Check if name unique
            # choose a class
            proff = "0"
            while proff == "0":
                print("""
    Choose a Character Class
    =================

    Please choose a number corresponding with a Class option below:

    1 - Fighter
    2 - Rogue
    3 - Mage
    4 - Cleric
    5 - Ranger
    6 - Monk
    """)
                proff = input("Choice: ")
                if not (proff == "1" or proff == "2" or proff == "3" or proff == "4" or proff == "5" or proff == "6"):
                    proff = "0"
                if proff == "1":
                    cproff = "Fighter"
                    proffb = "+5 Physical Defence"
                if proff == "2":
                    cproff = "Rogue"
                    proffb = "+5 Physical Attack"
                if proff == "3":
                    cproff = "Mage"
                    proffb = "+5 Mana"
                if proff == "4":
                    cproff = "Cleric"
                    proffb = "+5 Health"
                if proff == "5":
                    cproff = "Ranger"
                    proffb = "+5 Speed"
                if proff == "6":
                    cproff = "Monk"
                    proffb = "+5 Evasion"
                    # Choose and Elemental Affinity

            elem = "0"
            while elem == "0":
                print("""
    Choose your character's Elemental Affinity
    =================

    Please choose a number corresponding with an Element option below:

    1 - Earth
    2 - Fire
    3 - Water
    4 - Wind
    """)
                elem = input("Choice: ")
                if not (elem == "1" or elem == "2" or elem == "3" or elem == "4" ):
                    elem = "0"
                if elem == "1":
                    celem = "Earth"
                if elem == "2":
                    celem = "Fire"
                if elem == "3":
                    celem = "Water"
                if elem == "4":
                    celem = "Wind"

            # Choose Primary Stats
            print("\nYou have ", pool, " points to spend on Vitality, Strength, Dexterity, Intelligence, "
                                       "Luck and Wisdom!")
            # Vitality
            vit = input("How much Vitality do you want them to have?: ")
            try:  # error handling
                cvit = int(vit)
            except ValueError:
                print("\nThat is not a number, made Vitality 0 and moving on! You can edit after if it was a mistake.")
                cvit = 0
            while cvit > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cvit = int(input("How much Vitality do you want them to have?: "))
            else:
                pool -= cvit
            print("\nYou have ", pool, " points to spend!")
            # Strength
            strn = input("How much Strength do you want them to have?: ")
            try:
                cstr = int(strn)
            except ValueError:
                print("\nThat is not a number, made Strength 0 and moving on! You can edit after if it was a mistake.")
                cstr = 0
            while cstr > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cstr = int(input("How much Strength do you want them to have?: "))
            else:
                pool -= cstr
            print("\nYou have ", pool, " points to spend!")
            # Dexterity
            dex = input("How much Dexterity do you want them to have?: ")
            try:
                cdex = int(dex)
            except ValueError:
                print("\nThat is not a number, made Dexterity 0 and moving on! You can edit after if it was a mistake"
                      ".")
                cdex = 0
            while cdex > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cdex = int(input("How much Dexterity do you want them to have?: "))
            else:
                pool -= cdex
            print("\nYou have ", pool, " points to spend!")
            # Intelligence
            inteli = input("How much Intelligence do you want them to have?: ")
            try:
                cinteli = int(inteli)
            except ValueError:
                print("\nThat is not a number, making Intelligence 0 and moving on! You can edit after if it was a "
                      "mistake.")
                cinteli = 0
            while cinteli > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cinteli = int(input("How much Intelligence do you want them to have?: "))
            else:
                pool -= cinteli
            print("\nYou have ", pool, " points to spend!")
            # Luck
            luck = input("How much Luck do you want them to have?: ")
            try:
                cluck = int(luck)
            except ValueError:
                print("\nThat is not a number, making Luck 0 and moving on! You can edit after if it was a mistake.")
                cluck = 0
            while cluck > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cluck = int(input("How much Luck do you want them to have?: "))
            else:
                pool -= cluck
            print("\nYou have ", pool, " points to spend!")
            # Spirit
            spir = input("How much Spirit do you want them to have?: ")
            try:
                cspir = int(spir)
            except ValueError:
                print("\nThat is not a number, making Spirit 0 and moving on! You can edit after if it was a mistake.")
                cspir = 0
            while cspir > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cspir = int(input("How much Spirit do you want them to have?: "))
            else:
                pool -= cspir
            print("\nYou have ", pool, " points to spend!")
            # Wisdom
            wis = input("How much wisdom do you want them to have?: ")
            try:
                cwis = int(wis)
            except ValueError:
                print("\nThat is not a number, making wisdom 0 and moving on! You can edit after if it was a mistake.")
                cwis = 0
            while cwis > pool:
                print("Not enough points left in pool, you have ", pool, " points available, try again!")
                cwis = int(input("How much wisdom do you want them to have?: "))
            else:
                pool -= cwis

            # Generating secondary stats - formulae can be editted for each stat as needed via functions
            hp = hpCalc(cvit, cstr, cproff)
            eva = evaCalc(cdex, cluck, cproff)
            pDef = pDefCalc(cstr, cvit, cproff)
            mDef = mDefCalc(cspir, cwis)
            pAtt = pAttCalc(cstr, cdex, cproff)
            mAtt = mAttCalc(cinteli, cwis)
            spd = spdCalc(cvit, cdex, cproff)
            mana = manaCalc(cspir, cinteli, cproff)

            cpstats = {"Vitality": cvit, "Strength": cstr, "Dexterity": cdex,"Intelligence": cinteli,
            "Luck": cluck, "Spirit": cspir, "Wisdom": cwis, "Bonus": proffb}

            csstats = {"Health": hp, "Evasion": eva, "Physical Defence": pDef, "Magic Defence": mDef,
           "Physical Attack": pAtt, "Magic Attack": mAtt, "Speed": spd, "Mana": mana}

            chars.update({cname: Character(cname, cproff, cpstats, csstats, celem) })

            # demonstrating pickling an object, loading to file, reading from file then printing same object

            with open ("toons.txt", 'wb') as outfile:
                pickle.dump(chars, outfile)

            with open ("toons.txt", "rb") as infile:
                chars = pickle.load(infile)

            print (chars[cname].profile())


        else:
            print("\nCharacter already exsists! Try editing it or deleting it!")

    # del char
    elif choice == "2":
        chardel = input("Which character would you like to delete?: ")
        chardelCap = chardel.capitalize()
        if chardelCap in chars:
            areusure = input("\nAre you sure you want to delete this character? 'Y' for YES, 'N' for NO: ")
            areusureCap = areusure.upper()
            if areusureCap == "Y":
                del chars[chardelCap]
                print("\nCharacter WAS deleted!")
            else:
                print("\nCharacter NOT deleted!")
        else:
            print("\nThat character doesnt exist!  Try adding it.")

    # list chars
    elif choice == "3":
        if chars:
            for key in chars:
                c = 1
                print(c,":", chars[key].get_name(),"-", chars[key].get_proff(), "\n" )
                c += 1
        else:
            print("\nYou have no characters! Try creating some!")

    # load chars
    elif choice == "4":

        if os.path.isfile('./toons.txt') is True:
            chars = pickle.load(open("toons.txt", "rb"))
            c = 1
            print("\nAll the following characters have been loaded from your last save:\n")
            if chars:
                for key in chars:
                    print ("\n",c,":", chars[key].get_name(), "-", chars[key].get_proff())
                    c += 1
        else:
            print("\nYou have no characters! Try creating some!")

    # wipe all chars
    elif choice == "5":
        areusure2 = input("\nAre you sure you want to erase ALL characters? 'Y' for YES, 'N' for NO: ")
        areusureCap2 = areusure2.upper()
        if areusureCap2 == "Y":
            chars = {}
            with open("toons.txt", 'wb') as delfile:
                pickle.dump(chars, delfile)
            print("\nAll characters have been erased!")
        else:
            print("\nCharacters NOT erased!")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")



input("\n\nPress the enter key to exit.")