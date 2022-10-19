class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def deposit(self,d):
        self.balance+=d
    def withdrawal(self,w):    
        if w <= self.balance:  
            self.balance-=w
        else:
            print ("Impossible operation! Insufficient balance!")       
    def bankFees(self):
        self.balance -= (0.05* self.balance)   
    def display(self):
        print(vars(self))

account1 = BankAccount(1,"rama",100)
account1.display()
account1.deposit(200)
account1.display()
account1.bankFees()
account1.display()
account1.withdrawal(50)
account1.display()
