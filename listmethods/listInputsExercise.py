#!/usr/bin/env python3
import random

wordbank= ["indentation", "spaces"]
tlgstudents= ['Alex', 'Benji', 'Cayla', 'Demetra', 'Derek', 'Deshawn', 'James', 'Maria', 'Marylyn', 'Nor', 'Sal', 'Sammy']

# Append the integer 4 to our list of students:
tlgstudents.append(4)

# Ask the user for input
numString = input("Please enter a number between 1 and 11:\n> ")
if numString.isnumeric():
    num = int(numString)
    student_name = tlgstudents[random.randrange(0, 12)]

    # Print our output
    print(student_name + " always uses " + str(tlgstudents[-1]) + " " + wordbank[1] + " to indent.")

else:
    print(numString + " always uses " + str(tlgstudents[-1]) + " " + wordbank[1] + " to indent.")
