# Semester Evaluator
# Author: Alissa Xu
# Date created: 6 November 2023

number_of_courses = int(input("How many courses are you taking? "))
total_rating = 0

for i in range(1, number_of_courses +1):
    course_rating = int(input(f"How do you rate course {i} out of 5: "))
    total_rating += course_rating

average = total_rating / number_of_courses

if average <= 1: 
    print(f"{average}? Ouch.")
elif 1 < average < 3: 
    print(f"{average}? Not a bad semester.")
else: 
    print(f"{average}? Glad to hear that!")
                    
