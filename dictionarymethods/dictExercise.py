#!/usr/bin/env python3

hellenkeller= {
    "Occupation"  : "Author, political, activist, lecturer",
    "Education"   : "Radcliffe College",
    "Powers"      : "Heightened sense of smell",
    "Vertical"    : "44.5",
    "Mile time"   : "4:42"
    }

# Add a new value to the dictionary
hellenkeller["100 meter freestyle time"] = "1:02"

# Print a list of all the keys in the dictionary
print(hellenkeller.keys())

# Ask user for input from within the listed keys
choice = input("Pick one of the keys above to discover Hellen's most powerful attributes!\n> ")

# Print appropriate output
while choice not in hellenkeller.keys():
    choice = input("Come on, dude. Even Hellen Keller learned to read. Do you see your choice among those listed? Try again.\n> ")

if choice == "Powers":
    print(f"Hellen Keller's powers include a {hellenkeller[choice]}. But that's just the tip of the iceberg.")

elif choice == "Education":
    print(f"Hellen Keller's {choice} was at {hellenkeller[choice]}.")

else:
    print(f"Hellen Keller's {choice} is an impressive {hellenkeller[choice]}.")
