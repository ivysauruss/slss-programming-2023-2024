# Olympic Judging
# Author: Alissa Xu
# Date: 3 November 2023

judge_1 = 0
judge_2 = 0
judge_3 = 0
judge_4 = 0 
judge_5 = 0 

judge_1 = float(input("Judge 1: "))
judge_2 = float(input("Judge 2: "))
judge_3 = float(input("Judge 3: "))
judge_4 = float(input("Judge 4: "))
judge_5 = float(input("Judge 5: "))

judge_total = (judge_1 + judge_2 + judge_3 + judge_4 + judge_5) / 5
print(f"Your Olympic score is {judge_total:.1f}")
