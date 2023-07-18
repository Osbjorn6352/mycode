#!/usr/bin/env python3

def askName():
    name = input("Please enter your name: ")
    weekday = input("Also, what day of the week is it by the way?: ")
    print("Hello",name + ',', "happy " + weekday + '!')

askName()
