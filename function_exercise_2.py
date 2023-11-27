# Function Exercise 2 
# Author: Alissa Xu
# Date created: 27 November 2023

def biggest_number(number1: int, number2: int, number3: int) -> None:
    """Finds the biggest number out of the three
    Result is an integer.

    Params: 
    
    number1 - the first number
    number2 - the second number
    number3 - the third number

    """
    

    if number1 > number2 and number1 > number3:
        maxnumber = number1
    elif number2 > number1 and number2 > number3:
        maxnumber = number2
    else: 
        maxnumber = number3

    print(maxnumber)

biggest_number(3,77,17)