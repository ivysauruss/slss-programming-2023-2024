# Function Exercise 1
# Author: Alissa Xu
# Date created: 27 November 2023

def stars(number: int) -> None:
    """Creates stars based on the argument
    Results in integer.

    Params: 
    
    number - number of stars created"""

    starnumber = number

    for i in range(number):
        print("*")

stars(5)

