import sqlite3


connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
            SELECT * FROM clients 
''')
all_data = cursor.fetchall()

print(all_data[0][1])
