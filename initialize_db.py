import sqlite3

DB_NAME = 'example.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients
            (id integer primary key, 
            name text, 
            balance real)
    ''')

    print("Table created.")


initialize_database()
