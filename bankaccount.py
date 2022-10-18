class BankAccount:
    def __init__(self, accountNumber,  name , balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance


    def deposit(self, d):
        self.balance += d
       

    def withdrawal(self, w):
        if  w > self.balance:
            print("Impossible operation! Insufficient balance!")
        else:
            self.balance -= w
    
    def bankFees(self):
        return self.balance - self.balance*0.05

    def display(self):
        print(f"""
        Name:          {self.name}
        Account Number:{self.accountNumber}
        Balance :      {self.balance}

        """)

Account1 = BankAccount('NL20 503 8675 30 12', 'Richman', 600000)

Account1.deposit(5000)
Account1.withdrawal(10000)
Account1.bankFees()
Account1.display()




    





    