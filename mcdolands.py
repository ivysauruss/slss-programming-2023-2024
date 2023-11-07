# Mcdonalds 
# Author: Alissa Xu
# 6 November 2023

burger = input("Would you like a burger for $5? (Yes/No) ")
fries = input("Would you like fries for $3? (Yes/No) ")

total = 0 

if burger.lower().strip(" , . ? !") == ("yes"):
    total += 5

if fries.lower().strip(", . ?! ") == ("yes"):
    total += 3

total_with_tax = total + (total * 0.14)

print(f"Your total is ${total_with_tax:.2f}")