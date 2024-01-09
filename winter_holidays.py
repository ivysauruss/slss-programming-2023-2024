# Winter Holidays Review
# Author: Alissa Xu
# 8 January 2024

# Requirements: 
# - create a function called winter_holiday()
# = take one parameter
#   - string
# return a summary of an event from your holidays


import random

good_list = [ 
    "I went to Richmond centre to exchange gifts with friends",
    "I celebrated New Years outside with a dinner at Earl's",
    "I played video games instead of doing work"
]

bad_list = [
    "I felt too unproductive to do anything",
    "The weather was always bad"
    "I didn't have much to do"
]

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our wnter holidays 2023/24
    
    Params: 
        good_or_bad - indicate what kind of event to summarize
        
    
    Returns: 
        an event that happened during the holidays"""
    
    if (good_or_bad == "good"): 
        event = (random.choice(good_list))
    else: 
        event = (random.choice(bad_list))
    
    
    print(event)
    return event
        
winter_holiday("bad")
    

# Chatgpt for problem solving