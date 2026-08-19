print("A5.10-----ATM")
balance = 1000.0

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance:.2f}")
    elif choice == '2':
        amount = float(input("Enter deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: $"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        elif amount > balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount.")
    elif choice == '4':
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 4.")
