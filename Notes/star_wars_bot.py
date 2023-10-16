# Star Wars Bot
# Author: Alissa Xu
# Date: Oct 15 2023

import time 
print("I will decide if you can join the Dark Side ")

# Ask the questions

time.sleep(1)
colour = input("Is red your favourite colour? ")
cape = input("Do you like capes? ")

# Decide whether the user belongs to the dark side or the light side 

if colour.lower().strip("? , . !") == "yes" or cape.lower().strip("?,.!") == "yes": 
    print("Dark side it is!")
else: 
    print("Light side, I see.")