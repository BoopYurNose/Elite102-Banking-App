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
    #print("worked")
    UsernameSearch = userinput
    Sealious.execute("SELECT rowid, * FROM BankingAccounts WHERE Username = ?", (UsernameSearch,)) #WORK ON THIS
    AccountFound = Sealious.fetchall()
    print(AccountFound)
    for Info in AccountFound:
        #print(Info)
        if Info[1] == userinput:
            PasswordCheck = Info[2]
            ID = Info[0]
            PersonName = Info[3]
            CurrentBalance = Info[4]
            LoggedInCheck = Info[5]
    print(PasswordCheck)
    if PasswordCheck == passinput:
            print(f"Found password, {PasswordCheck}")
            Sealious.execute(
            "UPDATE BankingAccounts SET LoggedIn = 1 WHERE Username = ? AND Password = ?",
             (userinput, passinput))
            ConnectionBank.commit()
            AccountFound = Sealious.fetchall()
            return ID, PersonName, CurrentBalance, LoggedInCheck

def Logout(ID):
    Sealious.execute(
        "UPDATE BankingAccounts SET LoggedIn = 0 WHERE rowid = ?",
        (ID)
    )
    ConnectionBank.commit()
    return

def AddOrWithdrawMoney(ID, Choice, Amount):
    MoneyMove = Amount

    if Choice == "AddMoney":
        Sealious.execute(
            "UPDATE BankingAccounts SET Balance = Balance + ? WHERE rowid = ?",
            (MoneyMove, ID)
        )
        ConnectionBank.commit()
        return

    elif Choice == "RemoveMoney":
        Sealious.execute(
            "UPDATE BankingAccounts SET Balance = Balance - ? WHERE rowid = ?",
            (MoneyMove, ID)
        )
        ConnectionBank.commit()
        return

print("Successfully Ran!")

#ConnectionBank.commit() # remember to comment this out (only uncomment these both things when you have to make an update to this script REMEMBER THAT)
#ConnectionBank.close() # This too

def CloseDatabase():
    ConnectionBank.close()