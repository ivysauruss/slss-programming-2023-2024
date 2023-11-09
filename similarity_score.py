# Calculating Similarity Score 
# Author: Alissa Xu
#  Date created: 9 November 2023

# Calculate similarity scores between two people 

# Create two lists that represent the movies that they like
ubials_fave_movies = [
    "the matrix",
    "avengers: infinity war",
    "infernal affairs",
    "rogue one",
    "the empire strikes back"
]
bens_fave_movies = [
    "thomas and friends, big world big adventure",
    "paddington 2",
    "avengers: infinity war",
    "minions",
    "rogue one"
]

similarity_score = 0

# For every movie in the first list
    # If that movie is in the second list 
        # Increase the similarity score by 1
for movie in ubials_fave_movies:
    if movie in bens_fave_movies:
        similarity_score += 1
        

# Display the results 
print(f"The similarity score between the users is:")
print(similarity_score)