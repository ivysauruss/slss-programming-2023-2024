# Bubble Tea Popularity Algorithm 
# Author: Alissa Xu
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is 
# Print out a summary of the data

coco_likes = 0
chatime_likes = 0
suntea_likes = 0 
xingfutang = 0 
bbqueen_likes = 0

# Ask the user whwat their favourite bbt place is 
print("What's your favourite bubble tea place? ")
fave_bbt = input().strip(",.?! ").lower()

# Tallying/Counting Algo

# Options: CoCo, Chatime, SunTea, Xing Fu Tang, Bubble Queen
# If they say CoCo, increase the counter for Coco one by one, each time

if fave_bbt == "coco":
    coco_likes = coco_likes + 1 
elif fave_bbt == "chatime": 
    chatime_likes += 1
elif fave_bbt == "suntea": 
    suntea_likes += 1 

# Print a summary of the results 
print(f"CoCo Likes: {coco_likes}")
