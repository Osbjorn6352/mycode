#!/usr/bin/env python3

import shutil
import os

#Get source and destination from the user
source = input("Please specify a source directory - starting at the root directory - to copy all files from\n> ")
destination = input ("Please specify a destination directory - starting at the root directory - to copy all files to\n> ")

for file in os.listdir(source):
    if os.path.isdir(source + '/' + file) == False:
        shutil.move(source + '/' + file, destination + '/' + file)
#
