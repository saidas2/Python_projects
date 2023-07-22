#------------------- modules-----------------------

import converters

print(converters.kg_to_lbs(70))



import converters
from converters import kg_to_lbs

kg_to_lbs(100)


print(converters.kg_to_lbs(70))
# file is a module instead of writing all codes in one file we can  sort them in files
    

from converters import find_max

numbers=[10,3, 6, 2] 
max = find_max(numbers)
print(max)



#------------packages------------------------
# package = directory or folder
 # watch youtube





#------------------------generating randon values------------------

import random 

for i in range(3):
    print(random.randint(10, 20))



import random

member= ['John', 'di', 'mi','bob']
leader=random.choice (member)
print(leader)


import random

for i in range(9):
 dice1=random.randint(1, 9)

for t in range(9):
 dice2=random.randint(1, 9)


print((dice1, dice2))


#OOOR you also can do it like this:

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice=Dice()
print(dice.roll())

# ---------------files and directories-------------------

from pathlib import Path

#https://youtu.be/_uQrJ0TkZlc?t=14174








