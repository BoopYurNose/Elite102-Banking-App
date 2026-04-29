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

# Uncomment this when you want to test if the database properly updated an account value
#Sealious.execute(" SELECT rowid, * FROM BankingAccounts")
#Test = Sealious.fetchall()

#for items in Test:
#    print(items)


def AccountCreate(Username, Password, Name):
    NewData = (Username, Password, Name, 0, 1)
    Sealious.execute("INSERT INTO BankingAccounts VALUES (?,?,?,?,?)", NewData)
    print("Account successfully created")
    ConnectionBank.commit()





def QueryLogin(userinput, passinput):
    print("worked")
    UsernameSearch = userinput
    Sealious.execute("SELECT rowid, * FROM BankingAccounts WHERE Username = UsernameSearch;") #WORK ON THIS
    AccountFound = Sealious.fetchall()
    print(AccountFound)
    for Info in AccountFound:
        print(Info)
        if Info == userinput:
            print(f"found username {Info}")
            


print("Successfully Ran!")

#ConnectionBank.commit() # remember to comment this out (only uncomment these both things when you have to make an update to this script REMEMBER THAT)
#ConnectionBank.close() # This too

def CloseDatabase():
    ConnectionBank.close()