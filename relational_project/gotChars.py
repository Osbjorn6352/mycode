import sqlite3

conn = sqlite3.connect('got_database.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Houses
        (house_id INT PRIMARY KEY,
        name TEXT)''')

houses = [
        (1, 'Stark'),
        (2, 'Baratheon'),
        (3, 'Greyjoy'),
        (4, 'Lannister'),
        (5, 'Frey')
        ]

c.executemany('INSERT INTO Houses VALUES (?, ?)', houses)

c.execute('''CREATE TABLE IF NOT EXISTS Characters
        (char_id INTEGER PRIMARY KEY,
        name TEXT)''')

characters = [
        (1, 'Jon'),
        (2, 'Eddard'),
        (3, 'Rob'),
        (4, 'Theon'),
        (5, 'Robert'),
        (6, 'Cersei'),
        (7, 'Walder'),
        (8, 'Bran'),
        (9, 'Arya'),
        (10, 'Tyrion'),
        (11, 'Stannis'),
        (12, 'Joffrey'),
        (13, 'Jaime')
]

c.executemany('INSERT INTO Characters VALUES (?, ?)', characters)

c.execute('''CREATE TABLE IF NOT EXISTS CharacterHouses
        (char_id INTEGER PRIMARY KEY,
        house_id INTEGER)''')

charactersToHouses = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 3),
        (5, 2),
        (6, 4),
        (7, 5),
        (8, 1),
        (9, 1),
        (10, 4),
        (11, 2),
        (12, 2),
        (13, 4)
]

c.executemany('INSERT INTO CharacterHouses VALUES(?, ?)', charactersToHouses)

conn.commit()
conn.close()

