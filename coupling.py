# Coupling - In OOPS coupling refers to the degree of dependency between different classes or modules within a system. So high coupling means the classes are tightly inter connected making it difficult to modify and maintain them independently where low coupling means loose inter connection between classes allowing for greater flexibility and ease of modification. So if classes are tightly coupled then modifying one class could break the other which could break the whole program.

# Highly Coupled Classes Example
from abc import ABC,abstractmethod                     

class SenderEmail:
    def send_message(self,message):
        print(f"Sending Message: {message}")

class Order:
    def create(self):
        # Perform Order Creation Logic
        email =SenderEmail()
        email.send_message("Hi your order was placed successfully")

order = Order()
order.create()

# The above code is an issue of coupling where SenderEmail is called through Order class and any modification to SenderEmail class will require modification through Order class

# To reduce coupling we need to perform an abstraction between SenderEmail class and Order class. So this is going to allow the order class to interact with SenderEmail class through an abstraction making it easier to replace or modify the implementation of SenderEmail without affecting the order 

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self,message:str):
        pass

class EmailService(NotificationService):
    def send_notification(self,message):
        print(f"Sending Message: {message}")

class MobileService(NotificationService):
    def send_notification(self, message:str):
        print(f"Sending Text Message: {message}")

class FaxService(NotificationService):
    def send_notification(self, message:str):
        print(f"Sending Fax Message: {message}")
        

class Order:

    def __init__(self,notification_service:NotificationService):
        self.notification_service = notification_service


    def create(self):
        # Perform Order Creation Logic
        # email =SenderEmail()
        # email.send_message("Hi your order was placed successfully")
        self.notification_service.send_notification("Hi mail sent")


order = Order(MobileService())
order.create()

order = Order(EmailService())
order.create()

order = Order(FaxService())
order.create()

# In this improved code the Order class now depends on NotificationService. This NotificationService abstracts instead of concrete or ordinary email sender class which is not a abstract class. This decouples the Order classs from the specific implementation of the NotificationService which previously was the email sender class and this allows different implementations 
