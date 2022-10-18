import time

class  BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def deposit(self):
        
        time.sleep(0.5)
        
        print('*** Bank User deposit ***\n')
        self.accountNumber = (input("Please put the Account Number: "))
        self.name = (input("Please put the Name: ").upper())
        self.balance = int((input(f"Please put the mount to deposit: ")))
        
        time.sleep(0.5)
        
        usr =BankAccount (f'{self.accountNumber}', {self.name}, {self.balance})
        list_bankacc = list()
        list_bankacc.append(usr)
        
        usr_dcit = usr.__dict__
        print('\n',usr_dcit)
        print("\n Succes !\n")
        time.sleep(0.5)

    def withdrawal(self):
        
        print('*** Withdrawal ***\n')
        
        print(f"Yor balance is  {self.balance}")
        print()
        wd = int((input("Please put the mount to Withdrawal: ")))
        
        time.sleep(0.5)
        
        if wd > self.balance:
            print('Impossible operation, Insufficient funds !')
            time.sleep(0.5)
            exit()
        else:
            self.balance = self.balance - wd

    def bankFees(self):
        
        self.balance = self.balance - (self.balance * (5 / 100))
        
        time.sleep(0.5)
        
        print(f"The bank have a fess (5 %), you tax is: {self.balance}")
        
    def Display(self):

        return (f'''
                
      USER DETAILS
    ------------------
    Account Number : {self.accountNumber}
    Name of User   : {self. name}
    Balance        : {self.balance}
        ''')


usr = BankAccount('','', 0)

usr.deposit()

usr.withdrawal()

print()
usr.bankFees()

est_report = f'''
{'='*40}
{'USER REPORT'.center(40)}
{'='*40}''' 
print(est_report)
print(usr.Display())