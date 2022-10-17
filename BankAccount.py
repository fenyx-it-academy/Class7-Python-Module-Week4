# 3. BankAccount


class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self,d):
        self.balance = d+self.balance
        return self.balance

    def withdrawal(self,w):
        if w <= self.balance:
            self.balance = self.balance-w
        else:
            print("Impossible operation! Insufficient balance!")
        return self.balance

    def bankFees(self):
        self.balance = self.balance - (self.balance*0.05)
        return self.balance

    def desplay(self):
        print(f"Bank Account Details:\nBank account number: {self.accountNumber}\nName: {self.name}\nBalance: {self.balance}")

acc = BankAccount(1234,"shatha",150)
acc.deposit(50)
acc.withdrawal(10)
acc.withdrawal(50)
acc.withdrawal(40)
acc.bankFees()
acc.withdrawal(100)
acc.desplay()