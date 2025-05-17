import time
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email  = email # If we precede an class attribut with an underscore then we make it private
        self.password = password
    
    @property
    def email(self):
        print("Email ID Accesed at", time.asctime())
        return self._email

    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Wrong Access!!!")
            return self._email
    
     

    # # def say_hi_to_user(self,user):
    # #     print(f"Sending Message to {user.username}:Hi!!! {user.username}, it is {self.username}")

    # def get_email(self):
    #     print("Email accessed at", time.asctime())
    #     return self._email
    
    # def set_email(self,new_email):
    #     self._email = new_email

    # def clean_email(self):
    #     return self._email.lower().strip()


# Remeber we use setter and getter methods here because it gives us full control over what we read and modify
# For example: If we want to print useremail and time every time any user 


# user1 = User("Dantheman","dan@gmail.com","123")
# user1.email = "This is not an valid email" # We are setting a non vlaid email id but if we print it
# then we see it accessed even though its not an valid email
# print(user1.email)

# Here we can see that even an invalid email is accessible and is able to modify the attributes
# so we will have to get getter and setter properties


user1 = User("Dantheman","dan@gmail.com","123")
print(user1.email) 
# Here it might look as we are accessing the email directly but we are accessing it through getter property
user1.email = "This is not an email"


