import sqlite3


def get_accounts():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute('''
            SELECT * FROM clients 
''')
    all_data = cursor.fetchall()

    return all_data


def create_account(user, initial_deposit):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute(f'''
        INSERT INTO clients (name, balance) VALUES
        ('{user}', '{initial_deposit}')
''')
    print('Account has been made, closing connection.')
    connection.commit()
    connection.close()


def withdraw(user, amount):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute(f''' 
        UPDATE clients
        SET balance = balance - '{amount}'
        WHERE name = '{user}'
''')
    connection.commit()
    connection.close()
    print("Balance has been updated")


def deposit(user, amount):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute(f''' 
        UPDATE clients
        SET balance = balance + '{amount}'
        WHERE name = '{user}'
''')
    connection.commit()
    connection.close()
    print("Balance has been updated")


def delete():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute('''
            DELETE FROM clients;
''')
    connection.commit()
    connection.close()
    print("All rows deleted")


def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    print("What would you like to do?")
    print('1.) Create account')
    print('2.) Withdraw from existing account')
    print('3.) Deposit into existing account')
    print('4.) Delete all rows')
    choice = input()

    if int(choice) == 1:
        user = input("What would you like to name the account?\n")
        int_dp = input(
            "How much would you like to deposit into this acccount?\n")
        create_account(user, int_dp)

    elif int(choice) == 2:
        user = input(
            'What is the name of the account you would like to withdraw from?\n')
        amount = input('How much would you like to withdraw\n')
        withdraw(user, amount)

    elif int(choice) == 3:
        user = input(
            'What is the name of the account you would like to deposit into?\n')
        amount = input('How much would you like to deposit\n')
        deposit(user, amount)

    elif int(choice) == 4:
        cursor.execute('''
            DELETE FROM clients;
''')
        connection.commit()
        connection.close()
        print("All rows deleted")


if __name__ == "__main__":
    main()
