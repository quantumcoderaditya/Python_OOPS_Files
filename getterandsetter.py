import time
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email  = email # If we precede an class attribut with an underscore then we make it private
        self.password = password

    # def say_hi_to_user(self,user):
    #     print(f"Sending Message to {user.username}:Hi!!! {user.username}, it is {self.username}")

    def get_email(self):
        print("Email accessed at", time.asctime())
        return self._email
    
    def set_email(self,new_email):
        self._email = new_email

    def clean_email(self):
        return self._email.lower().strip()


# Remeber we use setter and getter methods here because it gives us full control over what we read and modify
# For example: If we want to print useremail and time every time any user 


user1 = User("Dantheman","dan@gmail.com","123")
# print(user1.clean_email())
print(user1.get_email())
user1.set_email("danny@outlook.com")
print(user1.get_email())