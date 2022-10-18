# ## 3. BankAccount

# 1. Create a Python class called  `BankAccount`  which represents a bank account, having as attributes:  `accountNumber`,  `name` , `balance`.
# 2.  Create a  **constructor**  with parameters:  `accountNumber`, `name`, `balance`.
# 3.  Create a  `deposit()`  method which manages the deposit actions. (deposit() method will take parameter d and you will increase the balance with the amount d)
# 4.  Create a  `withdrawal()` method which manages withdrawals actions. (withdrawal() method will take parameter w, you will reduce the amount of balance with w, if w is larger than the balance: then print `Impossible operation! Insufficient balance!"`)
# 5.  Create a `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account. (When this method is called, the balance amount should reduce 5%)
# 6.  Create a  `display()` method to display account details.

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def deposit(self):
        amount = float(input('Enter amount to be deposited: '))
        self.balance += amount

    def withdrawal(self):
        amount = float(input('Enter amount to be withdrawn: '))
        if self.balance < amount :
            print('Impossible operation! Insufficient balance!')
        else:
            self.balance -= amount

    def bankFees(self):
        self.balance = (95/100)* self.balance

    def display(self):
        print('\nAccount Number :' , self.accountNumber)
        print('Account Name :' , self.name)
        print('Account Balance :' , self.balance , '€')

print('Hello! Welcome to Deposit & Withdrawal Machine')
new_account = BankAccount(accountNumber=int(input('Account Number: ')), name=input('Account Name: '), balance=int(input('Account Balance: ')))
new_account.withdrawal()
new_account.deposit()
new_account.display()


















# class BankAccount:
#     def __init__(self, accountNumber, name, balance):
#         self.accountNumber = accountNumber
#         self.name = name
#         self.balance = balance
#         print('Hello! Welcome to the Deposit & Withdrawal Machine')

#     def deposit(self):
#         amount = float(input('Enter amount to be deposited: '))
#         self.balance += amount

#     def withdrawal(self):
#         amount = float(input('Enter amount to be withdrawn: '))
#         if self.balance < amount :
#             print('Impossible operation! Insufficient balance!')
#         else:
#             self.balance -= amount

#     def bankFees(self):
#         self.balance = (95/100)* self.balance

#     def display(self):
#         print('Account Number :' , self.accountNumber)
#         print('Account Name :' , self.name)
#         print('Account Balance :' , self.balance , '€')

# print('Please enter your account information: ')
# new_account = BankAccount()
# new_account.withdrawal()
# new_account.deposit()
# new_account.display()

