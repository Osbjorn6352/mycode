import sqlite3

conn = sqlite3.connect('got_database.db')
c = conn.cursor()

c.execute('''
        SELECT Characters.name
        FROM Characters''')

char_list = [] 
for char in c.fetchall():
    char_list.append(char[0])
print(char_list)

characterName = input("Please enter one of the above characters' names:\n> ")

#Ensure the entered name was valid
while characterName not in char_list:
    characterName = input("Name not among those listed. Did you spell the name correctly? Try again:\n> ")


c.execute('''
    SELECT Houses.name
    FROM Houses
    JOIN CharacterHouses ON Houses.house_id = CharacterHouses.house_id
    JOIN Characters ON Characters.char_id = CharacterHouses.char_id
    WHERE Characters.name = ?
    ''', (characterName, ))

house = c.fetchone()

print(f"{characterName} is in house {house[0]}.")

conn.close()