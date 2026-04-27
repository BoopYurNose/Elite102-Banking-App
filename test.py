MoneyAddInput = input("How much money would you like to add: ")
if MoneyAddInput.isnumeric():
    print("works")
else:
    try:
        float(MoneyAddInput)
        if int(MoneyAddInput) > 0:
            print("Valid")
    except ValueError:
        print("Not valid number")
print("Not valid")
    