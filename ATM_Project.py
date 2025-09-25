import sys

account_info = [
    {
        "name": "Hasan Yılmaz",
        "account_no": 12345,
        "balance": 2500,
        "overdraft": 1500,
        "username": "hasanyilmaz",
        "password": "1234"
    },
    {
        "name": "Eren Balkış",
        "account_no": 98765,
        "balance": 1600,
        "overdraft": 400,
        "username": "erenbalkis",
        "password": "9876"
    },
    {
        "name": "Hüseyin Çakmak",
        "account_no": 23456,
        "balance": 2000,
        "overdraft": 500,
        "username": "huseyincakmak",
        "password": "5678"
    },
    {
        "name": "Salih Korkmaz",
        "account_no": 67891,
        "balance": 5000,
        "overdraft": 2500,
        "username": "salihkorkmaz",
        "password": "9123"
    }
]

def display_menu(account):
    print()
    print(f"Hello {account['name']}")
    print("Press 1 for Balance Inquiry,")
    print("Press 2 for Withdrawals,")
    print("Press 3 for Deposits,")
    operation = input("Press 0 to exit: ")

    if operation == "1":
        check_balance(account)
    elif operation == "2":
        withdraw_money(account)
    elif operation == "3":
        deposit_money(account)
    elif operation == "0":
        print("\t\t HAVE A GOOD DAY, SEE YOU SOON!")
        sys.exit()
    else:
        print("Invalid input:")
    display_menu(account)

def check_balance(account):
    print()
    print(f"Your current balance: {account['balance']}")
    print(f"Your overdraft balance: {account['overdraft']}")

def withdraw_money(account):
    print()
    withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

    if account["balance"] >= withdrawal_amount:
        account["balance"] -= withdrawal_amount
        print("Don't forget to take your money!")
    else:
        total = account["balance"] + account["overdraft"]
        if total >= withdrawal_amount:
            print("Insufficient balance!")
            overdraft_permission = input("Should the overdraft be used? (y/n)")
            if overdraft_permission == "y":
                amount_to_use = withdrawal_amount - account["balance"]
                account["balance"] = 0
                account["overdraft"] -= amount_to_use
                print("You can take your money!")
            else:
                print("Sorry, your balance is insufficient!")
        else:
            print("Sorry, your balance is insufficient!")

def deposit_money(account):
    print()
    deposit_amount = int(input("Enter the amount you want to deposit: "))
    if deposit_amount > 0:
        account["balance"] += deposit_amount
        print("Money has been added to your account.")
    else:
        print("\t\t INVALID ENTRY!")

def login():
    username = input("Username: ")
    password = input("Password: ")

    is_logged_in = False

    for account in account_info:
        if account["username"] == username and account["password"] == password:
            is_logged_in = True
            display_menu(account)
            break

    if not is_logged_in:
        print("Username or password is incorrect!")

login()
