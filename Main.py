import sqlite3

# Connection Here! :3
Connection = sqlite3.connect("BankingDatabase")
Data = Connection.cursor()

#Creating a table
Data.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL)''')

# Inserting Data
Data.execute("INSERT INTO users (name, age) VALUES ('Amelia', 22)")

Connection.commit()

Data.execute("SELECT * FROM users")
rows = Connection.fetchall()
for row in rows:
    print(row)

Connection.close()