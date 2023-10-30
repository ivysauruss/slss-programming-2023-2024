# Bubble Tea Popularity Algorithm 
# Author: Alissa Xu
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is 
# Print out a summary of the data

coco_likes = 0
chatime_likes = 0
suntea_likes = 0 
xingfutang_likes = 0 
bbqueen_likes = 0
other_likes = 0

NUM_RESPONDENTS = 5

coco_percentage = (coco_likes / NUM_RESPONDENTS) * 100



for _ in range(NUM_RESPONDENTS):


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
    elif fave_bbt == "xingfutang":
        xingfutang_likes = xingfutang_likes + 1
    elif fave_bbt == "bbqueen":
        bbqueen_likes = bbqueen_likes + 1
    else: 
       other_likes = other_likes + 1




# Print a summary of the results 
print(f"CoCo Likes: {coco_likes} | {coco_percentage:.2f} %")
print(f"ChaTime Likes: {chatime_likes}")
print(f"Suntea Likes: {suntea_likes}")
print(f"Xing Fu Tang Likes: {xingfutang_likes}")
print(f"BBQueen Likes: {bbqueen_likes}")

print(f"{coco_percentage}")