# Parental Bot
# Author: Alissa Xu
# Date created: November 20

points = 0

question_list = ["Did you eat? ", "Did you study? ", "Did you do your laundry? " , "Did you call grandma? "]

for question in question_list:
    answer = input(question).strip("?.,! ").lower()
    if answer == "yes":
        points += 1

if (points == 0):
    print("I'm coming over.")
elif (1 <= points <= 2):
    print("Ok.")
elif ( 3 <= points <= 4):
    print("Good!")
        
        
        

