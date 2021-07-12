class Account():

    def __init__(self,name,amount=0):
        self.name = name
        self.amount = amount

    def deposit(self,amount):
        self.amount += amount
        print("Deposit succeed!")
        print("{} deposited,Account balance is {}".format(amount,self.amount))
        print(" ")

    def withdraw(self,amount):
        if(amount>self.amount):
            print("Account has incefficient balance,{}".format(self.amount))
        else:
            self.amount -= amount
            print("Withdraw succeed,Account balance is {}".format(self.amount))
            print(" ")

    def __str__(self):
        return "Account Owner: {}".format(self.name)

 

