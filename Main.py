'''Project Requirements
Your banking app must support:

Create new bank accounts (name, initial deposit)
Deposit money into an account
Withdraw money (with balance validation)
Check account balance
List / manage existing accounts
A simple menu-driven interface (terminal UI)'''
# This is my CLI if I finish this I will then make a web application version of this

# NOTE: have the sqlite3 database have all account credientials/balances/etc stored

# Everytime a user creates a new account store that accounts credientials in the database
#  and have a default balance value of 0 unless they change it

# you should add a character limit to the inputs of money, username, password, etc so some jackass doesn't type like 1,000 characters
# and mess up the formatting lmfao

def LineFormat(AmountLines):
    Lines = AmountLines
    LineFormat = ""
    for i in range(1, Lines):
        LineFormat += "-"

    print(LineFormat)

def AccountCreationValidator(Name, Username = None, Password = None):
    if not Username == None:
        pass
        # validate Username here

    if not Password == None:
        pass
        # Validate the password here
    
    if Name.isalpha():
        return True
    else:
        return False


    

def MainMenu():
    LineFormat(50)
    print("Welcome to my banking application! \n Would you like to either Sign in Type: SignIn \n Or would you like to Sign up Type: SignUp")

    UserChoice = input(":")
    if not UserChoice.lower() == "signin" and not UserChoice.lower() == "signup":
        print("Try again you can only pick either SignIn or SignUp by typing those and pressing enter \n")
        MainMenu()
        return
    elif UserChoice.lower() == "signin":
        # have sign in thing here
        pass
    elif UserChoice.lower() == "signup":
        LineFormat(50)
        print("Welcome to the sign up page \n if for any reason you would like to return to the MainMenu Type: Exit \n to any of the prompts")
        print("You will now input your name, username, password \n then after doing so you will be returned to the main menu")
        print("Make sure to remember these login credientials that you create \n becuase you will need to use these to login")
        print("After you've completed your account creation \n")

        NameInput = input("Please input your name Only include your first name with no numbers:")

        while not AccountCreationValidator(NameInput):
            print("Try again you need to input your name with NO NUMBERS")
            NameInput = input("Please input your name Only include your first name with no numbers:")
        
        UsernameInput = input("Please input your username now")


    
    
MainMenu()

