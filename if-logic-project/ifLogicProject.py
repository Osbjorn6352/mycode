#!/usr/bin/env python3

# The following program is meant to simulate going through a maze in the dark. 

class MazeBlock:

    def __init__(self, north=None, south=None, east=None, west=None, roomType = "dark room"):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.roomType = roomType

    def __str__(self):
        return f"To the north you see a {self.north.roomType}. To the south you see a {self.south.roomType}. To the east you see a {self.east.roomType}. To the west you see a {self.west.roomType}."

start = MazeBlock()
darkRoom0 = MazeBlock()
darkRoom1 = MazeBlock()
darkRoom2 = MazeBlock()
wall0 = MazeBlock()
wall0.roomType = "wall"

start.north = darkRoom0
start.east = darkRoom1
start.south = darkRoom2
start.west = wall0

location = start
darkRoom0.roomType = "exit"
darkRoom1.west = start

while location.roomType != "exit":
    print(location)
    direction = input("Will you go north, south, east, or west?\n> ")
    
    while direction not in ["north", "south", "east", "west"]:
        print("Invalid direction. Please try again.\n> ")
    
    if direction == "east" and location.east.roomType != "wall":
        location = location.east

    elif direction == "west" and location.west.roomType != "wall":
        location = location.west

    elif direction == "north" and location.north.roomType != "wall":
        location = location.north

    elif direction == "south" and location.south.roomType != "wall":
        location = location.south

    else:
        print("You can't walk through walls, traveler...")

    if location == start:
        print("Hmmm this looks familiar. You're back where you started.")

print("Congratulations, adventurer. You've found your way out of the maze. Might I recommend stopping at the tavern on the way home? It's been a long journey.")


