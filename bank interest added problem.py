class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print(f"{amount} is debited,bal is{self.getbal()}")
        else:
            print("in succient balance")
    def credit(self,amount):
            self.balance+=amount
            print(f"{amount} is credited,bal is{self.getbal()}")
    def getbal(self):
        return self.balance
class Savingsaccount(Account):
    def __init__(self,interest):
        self.interest=interest
        super().__init__(1000,"acc123")
    def interestrate(self):
        interest1=self.balance*(self.interest/100)
        self.balance+=interest1
        print(self.getbal())
acc1=Savingsaccount(10)
acc1.debit(100)
acc1.interestrate()
        