class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def deposit(self,d):
        self.balance+=d
    def withdrawal(self,w):
        if w>self.balance:
            print("Impossible operation! Insufficient balance!")
        else:
            self.balance-=w
    def bank_fees(self):
        self.balance*=0.95
    def display(self):
        print(f'Account number:{self.account_number}\nAccount Name:{self.name}\nAccount balance:{self.balance}\n')

sefa=BankAccount('2007','sefa',80)
sefa.deposit(30)
sefa.withdrawal(150)
sefa.withdrawal(10)
sefa.bank_fees()
sefa.display()
    
