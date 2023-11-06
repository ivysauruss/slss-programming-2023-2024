# World Traveller 
# Author: Alissa Xu
# Date created: 6 November 2023
tally_continent = 0

continents = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antartica"]

for continent in continents: 
    continent_arrival = input(f"Have you been to {continent}? ")
    if continent_arrival.lower().strip(",.?! ") == ("yes") :
        tally_continent = tally_continent + 1
    elif continent_arrival.lower().strip(", . ?! ") == ("no") :
        tally_continent = tally_continent 
    else: 
        break

print(f"{tally_continent} /7")
              