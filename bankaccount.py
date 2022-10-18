class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, d):
        self.balance += d
    
    def withdrawal(self, w):
        if w > self.balance:
            print("Impossible operation! Insufficient balance!")
        else:
            self.balance -= w

    def bankFees(self):
        self.balance = (95/100) * self.balance

    def display(self):
        print (f'''Account Number: {self.accountNumber}
            Name: {self.name}
            Balance: {self.balance}''')


account = BankAccount(1223456, "Nadine", 5000)

account.withdrawal(5100)
account.display()
account.deposit(5300)
account.display()
account.bankFees()
account.display()