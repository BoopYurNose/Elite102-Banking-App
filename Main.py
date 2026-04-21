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

# I will have it only allow you to have access to the account balance, manage accounts/list them, deposit money, widthdraw money, view transaction history etc
# after you've logged in to an account or have an account logged in

def Contains_UppercaseLowerNumber(Input, Check): # I made this for password validation, (probably don't use this for anything else unless it has same requirements as the password)
    if Check == "Upper":
        if any(Letter.isupper() for Letter in Input):
            return True
        else:
            return False
    elif Check == "Lower":
        if any(Letter.islower() for Letter in Input):
            return True
        else:
            return False
    elif Check == "Numbers":
        if any(Number.isdigit() for Number in Input):
            return True
        else:
            print("No numbers")
            return False

def LineFormat(AmountLines):
    Lines = AmountLines
    LineFormat = ""
    for i in range(1, Lines):
        LineFormat += "-"

    print(LineFormat)

def AccountCreationValidator(Name = None, Username = None, Password = None):
    Iterator = 0
    CharacterLimit = 20
    PasswordMinChars = 10

    if not Username == None:
        if Username.isalpha():
            for Characters in Username:
                Iterator += 1
                if Iterator > CharacterLimit:
                    print("Too long")
                    return False
            return True
        else:
            return False


    if not Password == None: # it has to contain atleast an uppercase and lowercase letter, and at the minimum 1 number character and atleast 10 characters long
        if Password.isalnum():
            if Contains_UppercaseLowerNumber(Password, "Upper") and Contains_UppercaseLowerNumber(Password, "Lower") and Contains_UppercaseLowerNumber(Password, "Numbers"):                 
                for Characters in Password:
                    Iterator += 1

            if Iterator < PasswordMinChars:
                return False
            else:
                return True
        else:
            return False
            
        # Validate the password here
    
    if not Name == None:
        if Name.isalpha():
            for Characters in Name:
                Iterator += 1
                if Characters.isdigit():
                    return False
                if Iterator > CharacterLimit:
                    print("Too long")
                    return False
            return True
        else:
            return False
    


    

def StartMenu():
    LineFormat(50)
    print("Welcome to my banking application! \n Would you like to either Sign in Type: SignIn \n Or would you like to Sign up Type: SignUp \n if you want to exit simply just type: Exit")

    UserChoice = input(":")
    if not UserChoice.lower() == "signin" and not UserChoice.lower() == "signup" and not UserChoice.lower() == "exit":
        print("Try again you can only pick either SignIn or SignUp by typing those and pressing enter \n")
        StartMenu()
        return
    elif UserChoice.lower() == "exit":
        print("Goodbye!")
        LineFormat(50)
        return
    elif UserChoice.lower() == "signin":
        LineFormat(50)
        print("welcome to the SignIn page! \n if you'd like to login type: Login \n if you forgot your username type: ForgotUsername \n otherwise if you'd like to be returned back to the StartMenu Type: Exit")

        UserOption = input(":")
        if not UserOption.lower() == "login" and not UserOption.lower() == "forgotusername" and not UserOption.lower() == "exit":
            print("You can only input the following options \n login \n forgotusername \n exit \n Try again the next time you come to the SignIn page")
            StartMenu()
            return
        elif UserOption.lower() == "login":
            print("prompt user for username and password")
        elif UserOption.lower() == "forgotusername":
            print("have the user verify themselves by typing in their name that is associated with the account \n then it'll give the user the username of all account names with that associated name they inputted")
        elif UserOption.lower() == "exit":
            StartMenu()
            return
        
        
    elif UserChoice.lower() == "signup":
        LineFormat(50)
        print("Welcome to the sign up page \n if for any reason you would like to return to the StartMenu Type: Exit \n to any of the prompts")
        print("You will now input your name, username, password \n then after doing so you will be returned to the main menu")
        print("Make sure to remember these login credientials that you create \n becuase you will need to use these to login")
        print("After you've completed your account creation \n")

        NameInput = input("Please input your name Only include your first name with no numbers also a maximum of 20 characters long:")

        while not AccountCreationValidator(NameInput):
            print("Try again you need to input your name with NO NUMBERS")
            NameInput = input("Please input your name Only include your first name with no numbers:")

        if NameInput.lower() == "exit":
            StartMenu()
            return


        UsernameInput = input("Please input your username now (numbers allowed but no longer than 20 characters):")
        while not AccountCreationValidator(None, UsernameInput):
            print("Try again you have surpassed the character limit")
            UsernameInput = input("Please input your username now (numbers allowed but no longer than 20 characters):")

        if UsernameInput.lower() == "exit":
            StartMenu()
            return
        
        PasswordInput = input("Now type in your password it has to contain atleast an uppercase and lowercase letter, and at the minimum 1 number character: ")

        while not AccountCreationValidator(None, None, PasswordInput):
            print("Try again you need to fufill all the requirements for creating a password")
            PasswordInput = input("Now type in your password it has to contain atleast an uppercase and lowercase letter, and at the minimum 1 number character And atleast 10 characters long: ")

        print("Great job on making an acccount, returning back to the main menu. \n")

        # For future reference here, when you figure out the SQLlite3 better, make these values into an account value that can be used as account credentials to login
        StartMenu()
        return
        
        



    
    
StartMenu()

