#Create a bank account with members account no.,name,type of account,balance

class bank():
    def __init__(self):
        self.accntno=0
        self.name=""
        self.type=""
        self.balance=0

    def getdata(self,accntno,name,type,balance):
        self.accntno=accntno
        self.name=name
        self.type=type
        self.balance=balance

    def display(self):
        print("Account number:",self.accntno)
        print("Name:",self.name)
        print("Account type:",self.type)
        print("Balance:",self.balance)

    def withdraw(self):
        print("Balance",self.balance)
        w=int(input("Enter the amount to withdraw:"))
        self.balance=self.balance-w
        print("Remaining balance:",self.balance)

    def deposit(self):
        print("Balance", self.balance)
        d = int(input("Enter the amount to deposit"))
        self.balance = self.balance + d
        print("Remaining balance:", self.balance)

    def checkbalance(self):
        print("Balance",self.balance)

account=bank()
while True:
    print("Choose the options:")
    print("1.Create account\n2.Deposit\n3.Withdraw\n4.Check balance\n5.EXIT")
    n=int(input())
    if n==1:
        an=int(input("Enter your account number:"))
        n = input("Enter your name:")
        t = input("Enter your account type (current/savings):")
        ab = int(input("Enter your account balance:"))
        account.getdata(an, n, t, ab)
        account.display()
    elif n==2:
        account.deposit()
    elif n==3:
        account.withdraw()
    elif n==4:
        account.checkbalance()
    elif n==5:
        exit()
    else:
        print("Invalid number!!Choose number between 1 and 5.")



