class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def deposit(self,d):
        self.balance+=d

    def  withdrawal(self , w):
        if self.balance <w : 
            print (' Impossible operation! Insufficient balance!')
        else:
            self.balance-=w

    def bankFees(self):
        self.balance = self.balance - (self.balance*0.05)
        return self.balance
    def display(self) :
        print (f'''
      accountNumber: {self.accountNumber }
      name: {self.name}
      balance: {self.balance }''' )

b=BankAccount (567894,'accountHolder', 5000)
b.withdrawal(500)
b.deposit(10000)
b.bankFees()
b.display()