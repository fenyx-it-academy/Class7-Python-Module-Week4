            #######################  Bank Account ########################

class BankAccount:
    def __init__(self, accountNumber, name, balance):

        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def deposit(self, d):
        self.balance += d

    def withdrawal(self, w):
        if self.balance > w:
            print('Impossible operation! Insufficient balance!')
        else:
            self.balance -= w
           
    
    def bankFees(self):
        self.balance =  1.05 * self.balance
    
    def display(self):
        print(f'''
        Account Number {self.accountNumber} 
        Name {self.name}  
        Balance {self.balance}
        ''')

x = BankAccount(123456789, 'Saffet', 1000)
x.withdrawal(200)
x.deposit(5000)
x.display()
    
        

    