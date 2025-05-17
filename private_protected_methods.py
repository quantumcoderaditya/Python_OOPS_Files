# We can also create private and protect methods by using single pr double underscore

import time
class Bank_Account:
    '''A class made for bank accounts'''
    MIN_BALANCE = 100

    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            print(f"{self.owner}'s account new balance: {self._balance}")
            self.__is_deposit_time()
        else:
            print("Deposit amount should be grater than zero")
    
    @staticmethod
    def valid_int_rate(rate):
        return 0<=rate<=5
    
    def _is_valid_amount(self,amount):
        return amount>0
    
    def __is_deposit_time(self):
        print(f"Amount Deposited at {time.asctime()}")
    

account = Bank_Account("Alice",500)
account.deposit(200)

# Using the static method 

print(Bank_Account.valid_int_rate(3))
print(Bank_Account.valid_int_rate(10))