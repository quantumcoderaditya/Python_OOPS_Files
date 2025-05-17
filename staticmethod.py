# A Static method of a class is a method which belongs to class itself rather then instances of a class. To create a static method we use the @staticmethod decorator



class Bank_Account:
    '''A class made for bank accounts'''
    MIN_BALANCE = 100

    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance
    
    def deposit(self,amount):
        if amount>0:
            self._balance += amount
            print(f"{self.owner}'s account new balance: {self._balance}")
        else:
            print("Deposit amount should be grater than zero")
    
    @staticmethod
    def valid_int_rate(rate):
        return 0<=rate<=5
    

account = Bank_Account("Alice",500)
account.deposit(200)

# Using the static method 

print(Bank_Account.valid_int_rate(3))
print(Bank_Account.valid_int_rate(10))

# Static Method and Attribute are both stored in class itself and not in any instance or object of the class. This means we have memory efficiency which is that no matter how many instances we create we store static values only once
