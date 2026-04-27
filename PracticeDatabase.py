import sqlite3

# Connect to database
DatabaseConnection = sqlite3.connect("Customer.db")

# Create a cursor
Cur = DatabaseConnection.cursor()

# Create a table
Cur.execute("""CREATE TABLE IF NOT EXISTS people (
        FirstName text,
        LastName text,
        Email text               
    )""")

# sqlite3 datatypes
'''
NULL
INTEGER
REAL
TEXT
BLOB
'''

Cur.execute("INSERT INTO people VALUES ('Pumpkin', 'Cat', 'kittycat@gmail.com')")

print("Successfully ran!")
# Commit our command
DatabaseConnection.commit()

# Close the connection
DatabaseConnection.close()