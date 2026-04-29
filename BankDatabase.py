import sqlite3

ConnectionBank = sqlite3.connect("BankData")

Sealious = ConnectionBank.cursor()

'''Sealious.execute(""" CREATE TABLE IF NOT EXISTS BankingAccounts (
                 Username TEXT,
                 Password TEXT,
                 Name TEXT,
                 Balance INT,
                 LoggedIn INT)
""")


SampleData = [('DerpAndCo', 'YouNeverCrackThisPassword', 'Will', 39000, 0), ('Ameliaah', 'password', 'Amelia', 17, 0), ('Zachgaming1', 'password', 'Zachary', 160, 0)]

Sealious.executemany("INSERT INTO BankingAccounts VALUES (?,?,?,?,?)", SampleData)


'''
Sealious.execute(" SELECT rowid, * FROM BankingAccounts")
Test = Sealious.fetchall()

for items in Test:
    print(items)


def QueryLogin(userinput, passinput):
    Sealious.execute("SELECT rowid, FROM BankingAccounts WHERE Username LIKE '{userinput}'")

print("Successfully Ran!")

ConnectionBank.commit()

ConnectionBank.close()