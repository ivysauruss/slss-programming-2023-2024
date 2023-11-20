# Similarity Score Input
# Author: Alissa Xu
# Date Created: November 17

print("Please enter hobbies, separated by spaces. ")
person_1_hobs = input("Person 1: ")
person_2_hobs = input("Person 2: ")

person_1_hobs_list = (person_1_hobs).strip(" . ! ? , ").lower().split()
person_2_hobs_list = (person_2_hobs).strip(" . ! ? , ").lower().split()

sim_score = 0

for item in person_1_hobs_list:
    if item in person_2_hobs_list:
        sim_score += 1
    else:
        sim_score = sim_score

print(f"You have {sim_score} hobbies in common!")