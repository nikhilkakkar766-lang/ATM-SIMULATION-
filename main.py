from atm_functions import check_balance, deposit, withdraw, statement

while True:
    print(" ----- ATM MENU -----")
    print("1.Displsy Balance")
    print("2. withdraw money")
    print("3. Deposit Money")
    print("4. Statement")
    print("5. Exit")
    choice= input("enter choice:")
    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        statement()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Wrong choice")