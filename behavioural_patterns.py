# Behavioural Design Patterns focus on how objects interact with each other and how they communicate to accomplish specific tasks. These patterns address communication, responsibility and algorithmic issues in Object Oriented Software design and they help in defining clear and efficient communications mechanisms between objects and classes and these pattern can help make desig nmore flexible, extensible and maintainable by promoting better communication and separation of concerns between objects and classes in the systems. So each pattern addresses specific design issues and provides a standardized solution to common problems encountered insiftware development. 

# State Pattern - It provides an object to behave differently depending on the state that it is in. 

from enum import Enum

class DocumentationStates(Enum):
    DRAFT = 1
    MODERATION = 2
    PUBLISH = 3

class UserRoles(Enum):
    READER = 1
    EDITOR = 2
    ADMIN = 3

class Document:
    def __init__(self,state : DocumentationStates , current_user_role : UserRoles):
        self.state = state
        self.current_user_role = current_user_role
    
    def publish(self):
        if self.state == DocumentationStates.DRAFT:
            self.state = DocumentationStates.MODERATION
        elif self.state == DocumentationStates and self.current_user_role == UserRoles.ADMIN:
            self.state = DocumentationStates.PUBLISH
        elif self.state ==DocumentationStates.PUBLISH:
            pass

doc = Document(DocumentationStates.DRAFT,UserRoles.EDITOR)
print(doc.state.name)
doc.publish()

# The above code does not follow the Open/Close principle and any change in states will need us to make in all state consitionals. So what we can do is maintain classes for each separate state and extract all state separate logic into the classes. So the Docunebt class will maintain reference to one of the state classes to represent the current state that it is in. Then instead of Documnet implementing State specific behaviour by itself. it will delegate all of the state specific work to state specific object that it has a reference to 

from abc import ABC,abstractmethod

class DocumentationStates(Enum):
    DRAFT = 1
    MODERATION = 2
    PUBLISH = 3

class UserRoles(Enum):
    READER = 1
    EDITOR = 2
    ADMIN = 3

class State(ABC):
    @abstractmethod
    def publish(self):
        pass

class DraftState(State):
    def __init__(self, document):
        self._document = document
    
    def publish(self):
        self._document.state = ModerationState(self._document)

class ModerationState(State):
    def __init__(self,document):
        self._document = document
    
    def publish(self):
        if self._document.current_user_role == UserRoles.ADMIN:
            self._document.state = PublishedState(self._document)

class PublishedState(State):
    def __init__(self,document):
        self._document = document
    
    def publish(self):
        pass


class Document:
    def __init__(self, current_user_role : UserRoles):
        self.state = DraftState(self)
        self.current_user_role = current_user_role
    
    def publish(self):
        self.state.publish()
        # if self.state == DocumentationStates.DRAFT:
        #     self.state = DocumentationStates.MODERATION
        # elif self.state == DocumentationStates and self.current_user_role == UserRoles.ADMIN:
        #     self.state = DocumentationStates.PUBLISH
        # elif self.state ==DocumentationStates.PUBLISH:

doc = Document(UserRoles.ADMIN)
doc.publish()
print(doc.state.__class__.__name__)

doc.publish()
print(doc.state.__class__.__name__)


# doc = Document(UserRoles.ADMIN)
# doc.publish()
# print(doc.state.__class__.__name__)

# State Pattern when to use: If you have a class that behaves differently depending on its state and you have too many conditional statements. 

# o State pattern reduces code duplicacy and simplifies readability 
# o It also satisfies the Single Responsibility Principle by abstracting state specific logic into separate classes. 
# o It also satisfies the Open/Close Principle.


