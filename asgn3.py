# 1. Create a Python class called  `BankAccount`  which represents a bank account, having as attributes: 
# `accountNumber`,  `name` , `balance`.

# 2.  Create a  **constructor**  with parameters:  `accountNumber`, `name`, `balance`.
# 3.  Create a  `deposit()`  method which manages the deposit actions. (deposit() method will take parameter
# d and you will increase the balance with the amount d)

# 4.  Create a  `withdrawal()` method which manages withdrawals actions. (withdrawal() 
# method will take parameter w, you will reduce the amount of balance with w, if w is larger than the balance: 
# then print `Impossible operation! Insufficient balance!"`)


# 5.  Create a `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account. 
# (When this method is called, the balance amount should reduce 5%)
# 6.  Create a  `display()` method to display account details.
class BankAccount():
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance
    def deposit(self):
        d=float(input('enter the amount you want to deposit: '))
        self.balance+=d
        return self.balance
    def withdrawal(self):
        w=float(input('enter the withdrawal amount'))
        if self.balance >= w:
            return self.balance-w
        else:
            print('mpossible operation! Insufficient balance!')
    def bankFees(self):
        return self.balance*.05
    def display(self):
        y=input('which operation would you like to undertake,withdraw or disposit? for disposit ener d for withdraw w: ').lower()
        if y=='d':
            dip=bankdetail.deposit()
            return f'account number: {self.accountNumber} -accountholder: {self.name} -current balance: {dip}'
        elif y=='w':
            wit=bankdetail.withdrawal()
            fe=bankdetail.bankFees()
            return f'account number:{self.accountNumber} -Accountholder:{self.name} -current balance:{wit} nankfee:{fe}'
        

        
bankdetail=BankAccount('w12e3r4','tamerat',50)
print(bankdetail.display())
    