def showBalance(balance):
    print(f"Your Balance is ${balance:.2f}")
def withdraw(balance):
    amount = float(input("Enter an amount to withdraw from your account: "))
    if amount>balance:
        print("Insufficient balance in your account")
        return 0
    elif amount<0:
        print("This is not a valid amount.")
        return 0
    else:
        return amount
    
def deposit():
    amount = float(input("Enter an amount to save in your account: "))
    if amount<0:
        print("This is not a valid amount.")
        return 0
    else:
        return amount
def main():
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
            showBalance(balance)
        elif choice == '2':
            balance-=withdraw(balance)
        elif choice == '3':
            balance+=deposit()
        elif choice == '4':
            isRunning = False
        else:
            print("Your input is not valid.")

    print("Thank you for banking with us. Have a nice day!")

if __name__ == '__main__':
    main()