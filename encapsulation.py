# Encapsulation - It is a fundamental method of OOPS that involves bunding the data or attributes or fields and methods or the behaviors that operate on the data in a single unit called a class. Encapsulation helps in hiding the internal implementation details of the class by exposing only the necessary functionalities to the outside world. 
import time
class BadBankAccount:
    def __init__(self,balance):
        self.balance = balance

account = BadBankAccount(200)
account.balance = -1
print(account.balance)

# Here in the above code we can assign any value to the balance which could be negative as well but that is not possible in real life as we cant have negative money in our account but if we implement the code its assigning the value.

class BankAccount:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Cant Deposit negative amount")
        else:
            self._balance += amount
        
    def withdraw(self,widraw):
        if widraw <= self._balance:
            self._balance -= widraw
        else:
            raise ValueError ("Wrong Input")
        


time.sleep(0.5)
acc1 =BankAccount()
print(acc1.balance)
acc1.deposit(200)
time.sleep(0.5)
print(acc1.balance)
# print(acc1.deposit(-0.5))
time.sleep(0.5)
# print(acc1.withdraw(300))
acc1.withdraw(100)
print(acc1.balance)

# In the bank account class we have provided the getter property to display protected property balance of the account and this allows user of the accoun to check the balance but not able to manipulate the balance directly. So to modify balance bank account provide provides simple public API these two methods deposit and withdraw and this ensures the integrity of balance attribute value and that our expected program logic cant be violated. So step by step bank account encapsulates the balance of the account and its related methods into a single unit of this bank account class. The data members so balance are marked as protected, encapsulating them within the class and preventing them from direct access outside the class. Encapsulation of the methods in the bank account of the class also means that the user dont have to worry about the implementation details when interacting with the bank account object for example the user doesnt have to worry about the logic involved in withdrawing money they just have to call the method and the implementation details are hideen or encapsulated in the class 

# So we can say that encapsulation of the logic within the methods of the bank account class allows the users to interact with a bank account without knowing the internal details of how wuthdrawal works. So the encapsulation scraps away the complexity of the implementation details allowing the user to focus higher level functionality provided by bank account class. The users only need to know about the public interface of bank account class. In other words, its public methods or properties to use it effectively while the internal details remain hidden 

# So in summary encapsulation allows user to use the public interface without worrying about the internal complexity of the code

