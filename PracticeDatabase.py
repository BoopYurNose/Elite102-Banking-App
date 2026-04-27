import sqlite3

# Connect to database
DatabaseConnection = sqlite3.connect("Customer.db")

# Create a cursor
Cur = DatabaseConnection.cursor()

# Query The Database

#Cur.execute("SELECT rowid, * FROM people WHERE LastName LIKE 'Am%'")
#Cur.execute("SELECT rowid, * FROM people WHERE LastName LIKE 'Luau'")

#print(Cur.fetchone())
#Cur.fetchmany(3)


# Update Records
'''Cur.execute("""UPDATE people SET FirstName = 'Pumpkin'
            WHERE rowid = 3
""")
'''

# Delete Records
#Cur.execute("DELETE from people WHERE rowid = 6")

# ORDER BY
#Cur.execute("SELECT rowid, * FROM people ORDER BY rowid") #NOTE if left ommitted (meaning no specification) it'll automatically just ascend
#Cur.execute("SELECT rowid, * FROM people ORDER BY rowid DESC") descending order

#Cur.execute("SELECT rowid, * FROM people ORDER BY LastName") # alphabetical order from A-Z
#Cur.execute("SELECT rowid, * FROM people ORDER BY LastName DESC") #Same as previous but just other way around




# Query The Database - AND/OR
#Cur.execute("SELECT rowid, * FROM people WHERE LastName LIKE 'Am%' AND rowid = 1") #literally the same logic as the and and or operator in if statements in python
#Cur.execute("SELECT rowid, * FROM people WHERE LastName LIKE 'Am%' OR rowid = 3")

# Query The Database - LIMIT
#Cur.execute("SELECT rowid, * FROM people LIMIT 2") just limits the amount of results you can get from a query
#Cur.execute("SELECT rowid, * FROM people ORDER BY rowid DESC LIMIT 2")




# Drop Table (How to delete an entire table)
#Cur.execute("DROP TABLE people")

Cur.execute("SELECT rowid, * FROM people")

Data = Cur.fetchall()

for Items in Data:
    print(Items)


#print("NAME" + "\t\tEMAIL")
#print("-------" + "\t\t-------")
#Items = Cur.fetchall()
#for Stuff in Items:
#    print(Stuff[0] + "\t" + Stuff[1] + "\t" + Stuff[2])


'''ManyPeople = [('Tetsuya', 'Kiriyu', 'Tetsuya@gmail.com'), ('Ohma', 'Tokita', 'Ohma@gmail.com'), ('Luh', 'Luau', 'luhluaprogrammer@gmail.com')]

# Create a table
Cur.execute("""CREATE TABLE IF NOT EXISTS people (
        FirstName text,
        LastName text,
        Email text               
    )""")

# sqlite3 datatypes

NULL
INTEGER
REAL
TEXT
BLOB


Cur.execute("INSERT INTO people VALUES ('Pumpkin', 'Cat', 'kittycat@gmail.com')")
Cur.executemany("INSERT INTO people VALUES (?,?,?)", ManyPeople)
'''
print("Successfully ran!")
# Commit our command
DatabaseConnection.commit()

# Close the connection
DatabaseConnection.close()