
# ## 3. BankAccount

# 1. Create a Python class called  `BankAccount`  which represents a bank account, having as attributes:  `accountNumber`,  `name` , `balance`.
# 2.  Create a  **constructor**  with parameters:  `accountNumber`, `name`, `balance`.
# 3.  Create a  `deposit()`  method which manages the deposit actions. (deposit() method will take parameter d and you will increase the balance with the amount d)
# 4.  Create a  `withdrawal()` method which manages withdrawals actions. (withdrawal() method will take parameter w, you will reduce the amount of balance with w, if w is larger than the balance: then print `Impossible operation! Insufficient balance!"`)
# 5.  Create a `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account. (When this method is called, the balance amount should reduce 5%)
# 6.  Create a  `display()` method to display account details.
 
class BankAccount:
    def __init__(self ,accountNumber , name,balance ):
        self.accountNumber = accountNumber
        self.name=name
        self.balance=balance

    def deposit(self,d):
        self.balance+=d

    def  withdrawal(self , w)   :
        if self.balance <w : 
            print (' Impossible operation! Insufficient balance!')
        else:
            self.balance-=w

    def bankFees(self )  :
        self.balance *=0.95   

    def display(self) :
        print (f'''
      accountNumber {self.accountNumber }
      name  {self.name}
      balance: {self.balance }''' )

b=BankAccount (3243434,'accountHolder' , 3000)
b.withdrawal(1000)
b.deposit(10000)
b.display()