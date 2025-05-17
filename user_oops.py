class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email  = email
        self.password = password

    def say_hi_to_user(self,user):
        print(f"Sending Message to {user.username}:Hi!!! {user.username}, it is {self.username}")

user1 = User("Dantheman","dan@gmail.com","123")
user2 = User("Batman","bat@outlook.com","abc")

user1.say_hi_to_user(user2)

