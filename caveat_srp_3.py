# Using Composition in SRP Example:

class EmailSender:
    def send(self, recepient, message):
        print(f"Sending Email to {recepient}: {message} ")

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    
class UserService:

    def __init__(self,user:User):
        self.user = user     

    def register(self):
        print(f"Registering User: {self.user.username}")
        email = EmailSender()
        email.send(user.email,f"Welcome to our platform!!! {self.user.username}")
    
    def update(self):
        print(f"Updating user details: {self.user.username}")
    
    def delete(self):
        print(f"Deleted User {self.user.username}")

user = User("adityapara1990","addy2kicku@gmail.com")
user_service = UserService(user)
user_service.register()
user_service.update()
user_service.delete()

# Here the advantage of Encapsulation is : 

# 1.  Less code duplicacy as we only need to intialize the user once int he UserService
# 2.  Leads to cleaner method signatures because if we look at the methods we no longer needs to take user as we need.

# Disadvantage of Composition here:

# 1.  we have less user flexibility because each service object, each individual service object is now tightly coupled to a single user instance. So if we need to handle multiple users or switch the user object, we may need to create a new userservice instance for each user.

user2 = User("Joe","joe@gmail.com")
user_service2 = UserService(user2)
user_service2.register()
user_service2.update()
user_service2.delete()

# Here we can see that we had to create a new userservice object to manage user service for the new user and this new object is tightly coupled to the new user.

# Thus we can go with the previous method where we pass user as an argument in all methods and do not use init method

class EmailSender:
    def send(self, recepient, message):
        print(f"Sending Email to {recepient}: {message} ")

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    
class UserService:
    def register(self,user):
        print(f"Registering User: {user.username}")
        email = EmailSender()
        email.send(user.email,f"Welcome to our platform!!! {user.username}")
    
    def update(self,user):
        print(f"Updating user details: {user.username}")
    
    def delete(self,user):
        print(f"Deleted User {user.username}")

user = User("adityapara1990","addy2kicku@gmail.com")
user_service = UserService()
user_service.register(user)
user_service.update(user)
user_service.delete(user)

# Here we do not need to create a new userserivce everythime we create a new user we pass the user as an argument. So now we can use the same userservice for multilple users 

user2 = User("Dantheman","dantheman@gmail.com")
# user_service = UserService()
user_service.register(user2)
user_service.update(user2)
user_service.delete(user2)

# Here above we can see that the user2 is also using the same userservice as user

# Pros of passing user as an argument rather than by using composition - Here we can pass same different users to the same userservice without creating separate userservice objects every time. Also the userservice remains stateless because it doesnt retain info between these method calls 

# Cons of passing user as an argument - We have some repetitive code because each method or object called needs us to mention the user. There can be method signature overload because if the method requires multiple paraemters then method signature can become long and cumbersome 

# Comparing the composition method and passing user as an argument we can say that passing user as an argument (a stateless service) is better because they are easier to maintain and test. Also they are more flexible allowing the service to handle multiple users within the same instance and this method also follows Single Responsible Principle more closely as the services focus on the operations and not on mantaining state of a specific user. 

# We can follow composition when the service is supposed to operate on a single user throughout its life cycle and the user object is unlikely to change then perhaps you can use composition. 