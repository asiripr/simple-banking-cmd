def showBalance():
    print(f"Your Balance is ${balance:.2f}")
def withdraw():
    pass
def deposit():
    amount = float(input("Enter an amount to save in your account: "))
    if amount<0:
        print("This is not a valid account.")

balance = 0
isRunning = True

while isRunning:
    print("---Banking Program---")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        showBalance()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        deposit()
    elif choice == '4':
        isRunning = False
    else:
        print("Your input is not valid.")

print("Thank you for banking with us. Have a nice day!")