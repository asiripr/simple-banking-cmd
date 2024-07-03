def showBalance():
    pass
def withdraw():
    pass
def deposit():
    pass

balance = 0
isRunning = True

while isRunning:
    print("---Banking Program---")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == 1:
        showBalance
    elif choice == 2:
        withdraw
    elif choice == 3:
        deposit
    elif choice == 4:
        isRunning = False
    else:
        print("Your input is not valid.")
        