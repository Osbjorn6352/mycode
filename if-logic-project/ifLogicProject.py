#!/usr/bin/env python3

# The following program is meant to simulate going through a maze in the dark. 

class MazeBlock:

    def __init__(self, roomType = "dark room", north=None, south=None, east=None, west=None):
        self.roomType = roomType
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __str__(self):
        return f"To the north you see a {self.north.roomType}. To the south you see a {self.south.roomType}. To the east you see a {self.east.roomType}. To the west you see a {self.west.roomType}."

gramr = False
skadisBuckler = False

start = MazeBlock()

hintOfLight0 = MazeBlock("hint of light") # Hints of light indicate proximity to brighter rooms
hintOfLight1 = MazeBlock() 
hintOfLight2 = MazeBlock()

brighterLight0 = MazeBlock() # Brighter rooms indicate proximity to well-lit rooms
brighterLight1 = MazeBlock() # Rooms 1 and 2 should indicate heat being sensed from dragonfire
brighterLight2 = MazeBlock()

wellLitRoom0 = MazeBlock() # This room is illuminated by dragonfire. Players will have a better chance of slaying the dragon if they've collected gramr and/or Skadi's buckler
wellLitRoom1 = MazeBlock() # This room is right next to the exit, and is the room following the dragon's chamber.

# Dark rooms are the basic room types
darkRoom0 = MazeBlock()
darkRoom1 = MazeBlock()
darkRoom2 = MazeBlock()
darkRoom3 = MazeBlock()
darkRoom4 = MazeBlock()
darkRoom5 = MazeBlock()
darkRoom6 = MazeBlock()
darkRoom7 = MazeBlock()

wall = MazeBlock()
wall.roomType = "wall"

start.north = hintOfLight0
start.east = darkRoom0
start.south = darkRoom1
start.west = wall

location = start
hintOfLight0.roomType = "hint of light"
hintOfLight0.south = start
hintOfLight0.east = hintOfLight1
darkRoom0.west = start
darkRoom0.east = wall
darkRoom0.south = wall
darkRoom0.north = wall

print(hintOfLight0.roomType)

while location.roomType != "exit":
    print(location)
    direction = input("Will you go north, south, east, or west?\n> ").lower()
    
    while direction not in ["north", "south", "east", "west"]:
        direction = input("Invalid direction. Please try again.\n\n Will you go north, south, east, or west\n> ").lower()
    
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
