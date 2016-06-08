from classesV1 import *
from functionsV1 import *


Kelroy = Hero("Kelroy", "Mage", [10,9,11], "Fire") #Hero instance with name and other properties passes in
print (Kelroy.profile()) #check to see instance of Hero class created
Moth = Enemy0("Moth") #Enemy Moth created
Sword = Item(000, "Rusty Sword", "weapon", [3,4], 0, 0) #sword
Armour = Item(100, "Coat", "armour",[0,0],10,0) #armour
Pin = Item(200, "Blessed Pin", "accessory",[0,0],0,10) #accessory
Equip(Kelroy,Sword) #equip Sword
Equip(Kelroy, Armour) #equip Armour
Equip(Kelroy, Pin) #equip Accessory
print (Kelroy.profile()) #see if stats changed
commands(Kelroy, Moth) #Kelroy vs Moth
print (Kelroy.profile())#result


#http://stackoverflow.com/questions/28542427/python-isinstance-undefined-global-name
#http://effbot.org/zone/import-confusion.htm

