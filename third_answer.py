class BankAccount:
    fee = 0.05

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, d):
        self.balance += d

    def withdraw(self, w):
        if w <= self.balance:
            self.balance -= w
        else:
            print("Impossible operation! Insufficient balance!")

    def bankFees(self):
        self.balance -= (BankAccount.fee * self.balance)

    def display(self):
        print(f''''
        Account Number = {self.accountNumber}
        Name = {self.name}
        Balance = {self.balance}
        ''')


r1 = BankAccount(56445, "ghassan", 2000)
r1.display()
r1.deposit(1000)
r1.withdraw(500)
r1.display()
