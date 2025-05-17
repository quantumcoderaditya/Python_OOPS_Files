# Abstraction - The aim of abstraction is to hide unnecessary details and reduce complexity. For example when you use the tv remote to increase the vloume you dont have to worry about the circuits.

class Send_email:
    def _connect(self):
        print("Connecting to Email!!!!")
    
    def _authenticate(self):
        print("Authenticating!!!")
    
    def _disconnect(self):
        print("Disconnecting!!!")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending Mail!!!")
        self._disconnect()

s1 =Send_email()
s1.send_email()

# Here we have to only use send mail function and other unnecassary functionalities like connecting to internet and server, authenticating mail ids and disconnecting after sending the mail which is the responsibility of the coder has been protected and client only have to worry about sending mails.

# This might make abstraction and encapsulation sound similar. Encapsulation focuses on bundling data or attributes and methods that operate on a data in a single uhit called the class and it restricts access to the internal implementation details. So this is achieved by declaring attributes and methiods as private and exposing only control interface where as Abstraction focuses on hiding complexity by by hiding complexity by providing simplified high level interface to interact with. So by providing this simple send email method we are effectively concealing the underlying implementation of sending an email. So it allows users to focus on what an object does rather than on how it does it. So for example the send email method, as we mentioned, abstracts away those multiple internal steps required to send an email providing a nice and simple interface for the user.

# So in summary encapsulation focuses on bundling and restricting access while abstraction focuses on hiding unnecessary details. Encapsulation is a method that enables abstraction