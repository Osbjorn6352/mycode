import sqlite3

conn = sqlite3.connect('my_database.db')

c = conn.cursor()

c.execute('''SELECT products.name
             FROM products
             INNER JOIN companies ON products.company_id = companies.id
             WHERE companies.name = 'XYZ Corp';''')

result = c.fetchone()

print(result[0])
conn.close()
