# Single Responsibility Principle - This means that a class should have only one reason to change means that it should have only one responsibility or purpose

# This principle helps you to make classes that are more focused and perform one single, well defined task rather than multiple tasks. So breaking up classes into small more focused unit makes the code easier to understand, maintain and test 

# Bad Code

class EmailSender:
    def send(self, recepient, message):
        print(f"Sending Email to {recepient}: {message} ")

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email 
    
    def register(self):
        print(f"Registering User: {self.username}")
        email = EmailSender()
        email.send(self.email,f"Welcome to our platform!!! {self.username}")

user = User("adityapara1990","addy2kicku@gmail.com")
user.register()

# This code violates Single Responsibility principle as the class can change due to modifications in user data management. For ex- We can add more fields like First Name, Last Name, Gender or Hobbies. It can also change due to modifications in the process of registering user. For ex: To check if the user does exist we might check username exists or not in place of email id 

# Refactored Code

class EmailSender:
    def send(self, recepient, message):
        print(f"Sending Email to {recepient}: {message} ")

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email
    
class UserService:
    def register(self,User):
        self.user = User
        print(f"Registering User: {user.username}")
        email = EmailSender()
        email.send(user.email,f"Welcome to our platform!!! {user.username}")
    
    def update(self,User):
        self.user = User
        print(f"Updating user details: {user.username}")
    
    def delete(self,User):
        self.user = User
        print(f"Deleted User {user.username}")

user = User("adityapara1990","addy2kicku@gmail.com")
user_service = UserService()
user_service.register(user)
user_service.update(user)
user_service.delete(user)

