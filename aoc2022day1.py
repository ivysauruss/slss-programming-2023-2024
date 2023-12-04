# AOC Day 1
# Author: Alissa Xu
# 30 November 2023

# There is one elf carrying the most calories
# How many does that one have?

# Create a list that holds all the calories of the elves
elves = []

# Open the file
with open("aoc2022day1.txt") as f:
    # Calories of the current elf
    current_cals = 0

    for line in f:
        # If there is something in the line
        if line.strip():
            current_cals += int(line.strip())
        else: 
            # Dump current_cals into elves list
            elves.append(current_cals)
            
            # Reset current_cals for next elf
            current_cals = 0

    # Find the biggest calories in the list
    biggest_cals = 0
    for elf in elves:
        if elf > biggest_cals:
            biggest_cals = elf

print(current_cals)
print(elves)
print(max(elves))

# Get the top three and sum them 
sorted_elves = sorted(elves)
top_three = sorted_elves[-3:]
top_three_total = sum(top_three)

print(sum(sorted(elves)[-3:]))