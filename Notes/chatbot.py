# Chatbot 
# Author: Alissa 
# Date: 21 September 2023

# Greet the user 
print("Hello there!")
print("I'm a crude chatbot, here to talk to you.")

# Get the user's name and store in a variable 
user_name = input("So... what's your name?")

# Respond with the user's name 
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is 
favourite_food = input("What's your favourite food, by the way?")

# Respond with something that is NOT too repetitive
# Create a list of appropriate responses 
list_of_fave_food_responses = [
    "Mmmmm. That sounds delicious.",
    f"Yes, {favourite_food} is one of my favourites too!",
    "Cool.",
    "Interesting, I've never tried that before."
]

# Choose one response randomly from the list 
import random 
random_response = random.choice(list_of_fave_food_responses)

# Print out the chosen response
print(random_response)