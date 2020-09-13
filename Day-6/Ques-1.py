class bank_account():
    def __init__(self,ownerName, balance):
        self.ownerName=ownerName
        self.balance=balance
        

    def deposit(self):
        print("Initial amount=",self.balance)
        depo=int(input("Enter the amount to be deposited"))
        self.balance += depo
        print("Money deposited=", depo)
        print("Total amount=",self.balance)

    def withdraw(self):
        withdraw=int(input("Enter the withdrawal amount"))
        print("Net Amount=",self.balance)
        if self.balance<=withdraw:
            print("withdrawal is cancelled")
        else:
            self.balance -=withdraw
            print("Withdrawal Amount=",withdraw )
            print("Net Amount",self.balance)

anv = bank_account("Priya", 10000)
anv.deposit()
anv.withdraw()
print("*****************")
anv.deposit()
anv.withdraw()
print("*****************")
anv.deposit()
anv.withdraw()
