classinfo = {
    "all": [
	    {
	        "Name": "Alex",
	        "Spirit Animal": "Tiger",
	        "Super Power": "Telekinesis",
	        "Skill Level": "Phenomenal"
	    },
	    {
	        "Name": "Benji",
	        "Spirit Animal": "Bear",
	        "Super Power": "Time Manipulation",
	        "Skill Level": "Spectacular"
	    },
	    {
	        "Name": "Cayla",
	        "Spirit Animal": "Owl",
	        "Super Power": "Flight",
	        "Skill Level": "Magnificent"
	    },
	    {
	        "Name": "Demetra",
	        "Spirit Animal": "Dragonfly",
	        "Super Power": "Invisibility",
	        "Skill Level": "Astounding"
	    },
	    {
	        "Name": "Derek",
	        "Spirit Animal": "Wolf",
	        "Super Power": "Teleportation",
	        "Skill Level": "Marvelous"
	    },
	    {
	        "Name": "Deshawn",
	        "Spirit Animal": "Eagle",
	        "Super Power": "Super Strength",
	        "Skill Level": "Incredible"
	    },
	    {
	        "Name": "James",
	        "Spirit Animal": "Lion",
	        "Super Power": "Mind Reading",
	        "Skill Level": "Wonderful"
	    },
	    {
	        "Name": "Maria",
	        "Spirit Animal": "Fox",
	        "Super Power": "Shape-Shifting",
	        "Skill Level": "Astonishing"
	    },
	    {
	        "Name": "Marylyn",
	        "Spirit Animal": "Dolphin",
	        "Super Power": "Telepathy",
	        "Skill Level": "Epic"
	    },
	    {
	        "Name": "Nor",
	        "Spirit Animal": "Butterfly",
	        "Super Power": "Elemental Control",
	        "Skill Level": "Fantastic"
	    },
	    {
	        "Name": "Sal",
	        "Spirit Animal": "Tiger",
	        "Super Power": "Telekinesis",
	        "Skill Level": "Phenomenal"
	    },
	    {
	        "Name": "Sammy",
	        "Spirit Animal": "Bear",
	        "Super Power": "Time Manipulation",
	        "Skill Level": "Spectacular"
	    }
	]

}

myDict = classinfo['all'][1]

print("My name is", myDict['Name'], "and my super power is", myDict['Super Power'])

for personDict in classinfo['all']:
    if personDict['Skill Level'][0].lower() in 'aeiou' and personDict['Super Power'][0].lower() in 'aeiou':
        print(f"{personDict['Name']}, an {personDict['Skill Level']} {personDict['Spirit Animal']} of a programmer, possesses an {personDict['Super Power']} factor for moonlighting as a superhero!")
    elif personDict['Skill Level'][0].lower() in 'aeiou' and personDict['Super Power'][0].lower() not in 'aeiou':
        print(f"{personDict['Name']}, an {personDict['Skill Level']} {personDict['Spirit Animal']} of a programmer, possesses a {personDict['Super Power']} factor for moonlighting as a superhero!")
    
    elif personDict['Skill Level'][0].lower() not in 'aeiou' and personDict['Super Power'][0].lower() in 'aeiou':
        print(f"{personDict['Name']}, a {personDict['Skill Level']} {personDict['Spirit Animal']} of a programmer, possesses an {personDict['Super Power']} factor for moonlighting as a superhero!")
    else:
       print(f"{personDict['Name']}, a {personDict['Skill Level']} {personDict['Spirit Animal']} of a programmer, possesses a {personDict['Super Power']} factor for moonlighting as a superhero!")
