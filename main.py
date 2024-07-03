def showBalance(balance):
    print("************************")
    print(f"Your Balance is ${balance:.2f}")
    print("************************")
def withdraw(balance):
    print("************************")
    amount = float(input("Enter an amount to withdraw from your account: "))
    print("************************")
    if amount>balance:
        print("************************")
        print("Insufficient balance in your account")
        print("************************")
        return 0
    elif amount<0:
        print("************************")
        print("This is not a valid amount.")
        print("************************")
        return 0
    else:
        return amount
    
def deposit():
    print("************************")
    amount = float(input("Enter an amount to save in your account: "))
    print("************************")
    if amount<0:
        print("************************")
        print("This is not a valid amount.")
        print("************************")
        return 0
    else:
        return amount
def main():
    balance = 0
    isRunning = True

    while isRunning:
        print("************************")
        print("---Banking Program---")
        print("************************")
        print("1. Show Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        print("************************")
        
        print("************************")
        choice = input("Enter your choice (1-4): ")
        print("************************")

        if choice == '1':
            showBalance(balance)
        elif choice == '2':
            balance-=withdraw(balance)
        elif choice == '3':
            balance+=deposit()
        elif choice == '4':
            isRunning = False
        else:
            print("************************")
            print("Your input is not valid.")
            print("************************")
    print("************************")
    print("Thank you for banking with us. Have a nice day!")
    print("************************")

if __name__ == '__main__':
    main()