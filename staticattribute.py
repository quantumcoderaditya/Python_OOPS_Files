# Static Attribute sometimes called as class attribute is a attribute that belongs to class itself and not any specific instances of a class. Tis means that static attirbutes are shared between all objects or instances of the class Static attributes are accessed directly by class and can be accessed by instances although they are stored at class level.

class User:
    user_count = 0

    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count +=1

    def display(self):
        print(f"Username: {self.username}, Email: {self.email}")
        # print(f"No of instances: {User.user_count}")

user1 = User("Dantheman","danny@gmail.com")
user2 = User("Sally","sally@gmail.com")
# user1.display()
# user2.display()
print(User.user_count)
print(user1.user_count)
print(user2.user_count)

# Always Remember Class attributes are declared in the class and shared between class and instnaces of the class. But, instance attributes are created every time we create a new instance