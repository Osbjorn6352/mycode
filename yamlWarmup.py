#!/usr/bin/env python3

import yaml
import json

selfDict = {"name": "Benjamin Osborn", 
            "movie": "Interstellar", 
            "ice cream": "Mint Chocolate Chip", 
            "color": "Sea Green"
           }


def main():
    jsonFile = open("favs.json", 'r')
    pythonData = json.load(jsonFile)
    pythonData.append(selfDict)
    
    with open("yamlFavs.yaml", 'w') as yamlFile:
        yaml.dump(pythonData, yamlFile)

    print("YAML file has been saved as yamlFavs.yaml")

if __name__ == '__main__':
    main()
