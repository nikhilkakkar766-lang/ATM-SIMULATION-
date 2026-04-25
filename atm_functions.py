
# atm_functions.py
from account import account
# Check balance
def check_balance():
    print("Balance:", account["balance"])

# Deposit money
def deposit():
    amt = int(input("Enter amount to deposit: "))
    account["balance"] += amt
    account["transactions"].append("Deposited " + str(amt))
    print("Money deposited")

# Withdraw money
def withdraw():
    amt = int(input("Enter amount to withdraw: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
        account["transactions"].append("Withdrew " + str(amt))
        print("Take your money")
    else:
        print("Not enough balance")

# Show statement
def statement():
    print("Transaction History:")
    for t in account["transactions"]:
        print(t)