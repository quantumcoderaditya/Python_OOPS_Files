# Dependency Inversion Principle states that high level modules should not depend on low level modules both should depend upon abstractions. So dependecy inversion is the strategy of depending upon interfaces or abstract class rather than upon concrete classes. So this principle promotes de coupling between modules and promotes the use of interfaces or abstract classes to define dependencies and promote more flexible and testable code. 

class Engine:
    '''This is low level module '''
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()
        print("Car Started")

car = Car()
car.start()

# In this program we see that car class directly creates an instance of engine class leading to a tight coupling between car and engine class. And if this engine class changes it may affect the car class which violated dependency inversion principle 

# A high level class is a class that typically represents the main functionality or business logic of the application. So it orchetrates the interaction between various components and is often more abstract in nature. In our case Car class can be considered the high level class because it represents the main functionality relating to starting a car and driving it 

# Low level classes is classes that provide specific functionality or services that are used by the high level class and it typically deals with the implementation details and is mpre concrete in nature. So in our class engine can be considered low level class as it provides the specific functionality of starting the engine of car. The engine class encapsulates the details of how engine works like ignition and combustion 

# Refactored Code - To adhere to dependency inversion principle we need to create an abstract class between car and engine class allowing car to depend on abstraction or abstract class instead of a concrete engine implementation

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass 

class BasicEngine(Engine):
    def start(self):
        print("Basic Engine started")

class FastEngine(Engine):
    def start(self):
        print("Fast Engine Started")

class Car:
    def __init__(self,engine:Engine):
        self.engine = engine
    
    def start(self):
        self.engine.start()
        print("Car Started")

# When we create a car object we actually need to pass an engine or inject an engine. In OOPS this is known as dependency injection. In other words we inject dependency into an object when we create it 

fasteng = FastEngine()
car = Car(fasteng)
car.start()

# Here in this last code we can inject any class into car class which inherits Engine class. So this makes our code very flexible because car class is no longer tightly coupled with Engine Class. 

# Advantages of Dependency injection: 

# 1. Decoupling - it promotes loose coupling between components by removing direct dependencies as components rely on abstraction rather than concrete implementations making them more independent and easier to maintain. 

# 2. Testabiltiy - It also improves testability because dependency injection simplifies unit testing by allowing components to be easily replaced with mock or stub implementations during testing and enables isolated testing of individual components without relying on their dependencies. 

# 3. Flexibility - It also improves flexibility by providing flexibility in configuring and swapping dependencies during runtime. So it allows different implementations of dependencies to be sued interchangeably without modifying any client code facilitating runtime customization and extensibility.

# 4. It improves readability and maintainabilty by explicitly specifying dependencies in the constructor or method parameters. It also reduces the risk of hidden dependecies leading to more maintainable and understandable code 

# 5. It also promotes component reusability decoupling them from their specific contexts or environments. So components can be designed to be independent of the application framework or platform making them more portable and reusable in different projects or scenarios 

# 6. It also helps to improve scalability by simplifying the management of dependencies inlarge scale applications by providing an standardized approach for dependency resolution 

