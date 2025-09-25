# ATM Withdrawal program
balance=int(input("enter your account balance:"))
withdrawal=int(input("enter withdrawal amount:"))
if withdrawal > balance:
    print("insufficient balance")
elif withdrawal % 100!=0:
    print("enter amount in multiples of 100")
    balance = withdrawal
    print("Transaction successful")
    print("Remaining balance:",balance)