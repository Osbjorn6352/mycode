#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """run-time code"""
    
    for i in range(0, 100):
        # create two cheater objects
        cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
        cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6

        # both players take turns
        cheater1.roll()
        cheater2.roll()

        # both players use their cheat methods
        cheater1.cheat()
        cheater2.cheat()

        with open("cheatResults.txt", 'a') as openFile:
            #print(f"Cheater 1 rolled {cheater1.get_dice()}", file = openFile)
            #print(f"Cheater 2 rolled {cheater2.get_dice()}", file = openFile)

            if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
                print("Draw!", file = openFile)

            elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
                print("Cheater 1 wins!", file = openFile)

            else:
                print("Cheater 2 wins!", file = openFile)

    drawCounter = 0
    oneCounter = 0
    twoCounter = 0

    with open("cheatResults.txt", 'r') as inFile:
        for line in inFile.readlines():
            if line.startswith("Draw!"):
                drawCounter += 1

            elif line.startswith("Cheater 1"):
                oneCounter += 1

            elif line.startswith("Cheater 2"):
                twoCounter += 1

    print(f"In 100 games, there were {drawCounter} draws, Cheater 1 won {oneCounter} times, and Cheater 2 won {twoCounter} times")

    with open("cheatResults.txt", 'w') as eraseFile:
        print("", file = eraseFile)

if __name__ == "__main__":
    main()

