# Food Suggestion Bot 
# Author : Alissa Xu
# Date : 6 October 2023

# A bot that asks the user what their favourite food is. The bot identifies the type/cuisine of the food and offer a suggestion for a restaurant. 

import random 
import time 
# Introduce the bot to the user
# Ask the user what their favourite food is 
print("Hello, I am here to suggest a restaurant to you.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is. ")
time.sleep(1)

# If they answer with an Italian dish
# Suggest an Italian restaurant 
# List all the Italian dishes 
# Add one more cuisine/type/etc.
# Test it to see if it works
italian_food = ["pizza", "pasta", "cannelon", "tiramisu"]
chinese_food = ["dumplings", "hot pot", "mapo tofu", "kung pao chicken"]

if fave_food.lower().strip("!,.? ") in italian_food :
    print("I think that you might like Italian food. 🍝")
    time.sleep(1)
    print("I suggest Bella Roma Italian Ristorante Richmond.")
    time.sleep(1)
    print("You can find the address below:")
    print("8368 Alexandra Rd, Richmond")
elif fave_food.lower().strip("!,.? ") in chinese_food : 
    print("I think that you might like Chinese food.")
    time.sleep(1)
    print("I suggest Tian Shi Fu restaurant.")
    time.sleep(1)
    print("You can find the address below:")
    print("4771 Mcclelland Rd, #1010 Richmond")
else: 
    print("Sorry. I don't recognize your favourite food.")
    print("My algorithm is still being worked on.")
    time.sleep(1)
    print("I can't offer a suggestion for you. 😭")

time.sleep(1)
print("Thanks for using this service.")