#!/usr/bin/env python3 

with open("/home/student/mycode/simpledoc.txt", "r") as simpleFile:
    lineList = []
    for line in simpleFile.readlines():
        print(line, end="")
        lineList.append(line)

print(lineList)
with open("/home/student/mycode/simpledoc.txt", "w") as sF:
    print("Roses are red\nViolets are Blue\nYou look like a noob\nAnd play like one too", sF)
