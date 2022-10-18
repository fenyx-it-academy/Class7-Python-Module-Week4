#Python program to create BankAccount class
#with both a deposit() and withdraw function.

#create the constructor with parameters: account_number, name and balance
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    #create deposit() method    
    def deposit(self):
        amount = float(input('Enter amount to be deposited: '))
        self.balance += amount

    #create withdrawal() method
    def withdrawal(self):
        amount = float(input('Enter amount to be withdrawn: '))
        if self.balance < amount :
            print('Impossible operation! Insufficient balance!')
        else:
            self.balance -= amount

    #create bankFees() method
    def bankFees(self):
        self.balance = (95/100)* self.balance

    #create display() method
    def display(self):
        print('\nAccount Number :' , self.account_number)
        print('Account Name :' , self.name)
        print('Account Balance :' , self.balance , '€')


print('Hello! Welcome to Deposit & Withdrawal Machine')
new_account = BankAccount(account_number=int(input('Account Number: ')), name=input('Account Name: '), balance=int(input('Account Balance: ')))
new_account.withdrawal()
new_account.deposit()
new_account.display()