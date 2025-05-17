
# Accessing, Modifying and Updating Data within an object

class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email  = email # If we precede an class attribut with an underscore then we make it private
        self.password = password

    # def say_hi_to_user(self,user):
    #     print(f"Sending Message to {user.username}:Hi!!! {user.username}, it is {self.username}")

    # def get_email(self):
    #     return self._email

    def clean_email(self):
        return self.__email.lower().strip()

user1 = User("Dantheman","  Dan@gmail.com  ","123")
print(user1.__email)
print(user1.clean_email())

# Remember : By prefixing anything with an underscore we are essentially communicating to Python Developers
# that this is an protected attribute and shouldnt be accessed outside the class

# The consulting adults philosophy

# Python rely on developer responsibiltiy rather the strict rules

# The developers are trusted to follow the convention of not accessing the underscore prefixed attributes
# or methods and the access is not strictly prevented as Python assumes the developer will act 
# responsibly and wont misuse or access protected members unless or until very necessary