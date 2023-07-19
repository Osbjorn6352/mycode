#!/usr/bin/env python3
Iroh = {
        "Nation": "Fire",
        "Relatives": ["Zuko - Nephew", "Ozai - Brother", "Lu Ten - Son (Deceased)", "Azulon - Father", "Ilah - Mother"],
        "Bending element" : "Fire",
        "Voiced by" : ["Mako - books 1 & 2", "Greg Baldwin - book 3"],
        "Created by" : ["Michael Dante DiMartino", "Bryan Konietzko"]
        }

print(Iroh["Nation"])

bender = "Iroh"
benderDict = Iroh
benderNation = benderDict["Nation"]

print(f"{bender} is from the {Iroh["Nation"]} nation. His/her relatives include {Iroh["Relatives"]}")
