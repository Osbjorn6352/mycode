#!/usr/bin/env python3

# This simple script uses the Riot Games API to find the champion with highest base hp in LoL

import requests

AOIF_CHAMP = "http://ddragon.leagueoflegends.com/cdn/13.14.1/data/en_US/champion.json"

def main():

    # Get the champion list from the Riot Games API
    gotDict = requests.get(AOIF_CHAMP).json()

    # Champions are held as a value under the "data" key
    champions = gotDict.get("data")

    # We'll need a current max hp tracker to update if we find a champion with higheer base hp
    maxHp = 0
    maxHpChamp = ""

    # Now let's iterate through the champions to find out who has the highest base hp!
    for champion in champions:
        
        championHp = champions[champion]["stats"]["hp"]
        
        if championHp > maxHp:
            maxHp = championHp

    # Now, we might have more than one champion with the same base hp
    # Let's make a list of all the champions with our newly found max HP value
    highHpChampList = []

    for champion in champions:

        championHp = champions[champion]["stats"]["hp"]

        if championHp == maxHp:
            highHpChampList.append(champions[champion]["id"])

    print(f"The highest base hp value in LoL at the moment is {maxHp}\n Champions with {maxHp} hp currently include:\n{highHpChampList}")

main()




