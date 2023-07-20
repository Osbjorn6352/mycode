#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["sheep", "cows", "pigs", "cats", "chickens", "llamas"]
plants = ["carrots", "celery"]


def basic():
    for farm in farms:
        if farm["name"] == "NE Farm":
            for animal in farm["agriculture"]:
                print(animal)

def userInpPlantsAnimals():
    # Now let's do it with user input
    for farm in farms:
        print(farm["name"])

    # First we get them to choose a farm
    farmChoice = input("Please choose one of the above farms to learn about what's cultivated there!\n> ")

    print('\n')

    # Next, we loop through in a similar way to what we did above
    for farm in farms:
        if farm["name"] == farmChoice:
            for cultivated in farm["agriculture"]:
                print(cultivated)

def userInpJustAnimals():
    
    #Set up similarly to above with one added step
    for farm in farms:
        print(farm["name"])

    # First we get them to choose a farm
    farmChoice = input("Please choose one of the above farms to learn about what animals are raised there!\n> ")


    # Next, we loop through in a similar way to what we did above
    for farm in farms:
        if farm["name"] == farmChoice:
            for cultivated in farm["agriculture"]:
                if cultivated in animals:
                    print(cultivated)

if __name__ == "__main__":

    #basic()
    #userInpPlantsAnimals()
    userInpJustAnimals()


