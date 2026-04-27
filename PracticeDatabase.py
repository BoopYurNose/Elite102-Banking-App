import sqlite3

# Connect to database
DatabaseConnection = sqlite3.connect("Customer.db")

# Create a cursor
Cursor = DatabaseConnection.cursor()

# Create a table
Cursor.execute("""CREATE TABLE people (
                   
)



    """)