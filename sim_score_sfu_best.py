# SFUs Best - Similarity Score 
# Author: Alissa Xu
# 10 November 2023

# Load data from a file
# "Read" it in a meaningful way 
# Link our Sim Score algo to the data

# Open the file
with open("./data.csv") as f:
    # Get the first line of data
    print(f.readline())

    # The second line of the csv file
    print(f.readline())

# Create a "profile" of likes (fave places in SFU)
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

with open("./data.csv") as f:
    # Throw away the header 
    header = f.readline()

    for line in f:

    # For every line of data in our csv file
        # Convert the string to a list
        current_likes = line.split(",")

        # Store the person's name
        current_name = current_likes[1]

        # Initialize the current sim score
        current_sim_score = 0

        # Sim score algorithm
        for item in profile: 
            if item in current_likes: 
                current_sim_score += 1

        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")
