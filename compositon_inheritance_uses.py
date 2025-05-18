class Engine:
    def start(self):
        print("Engine is starting")

class Wheels:
    def rotate(self):
        print("Wheels are rotating")

class Chasis:
    def support(self):
        print("Chasis is supporting Car")

class Seats:
    def sitting(self):
        print("People are sitting on seats")

class Car:
    def __init__(self):
        self._engine = Engine()
        self._wheels = Wheels()
        self._chasis = Chasis()
        self._seats = Seats()
    
    def start(self):
        self._engine.start()
        self._chasis.support()
        self._wheels.rotate()
        self._seats.sitting()
        print("Car Started!!")

car=Car()
car.start()

# Here the Car class can also inherit the chasis,engine,wheels and seats and then it could call them using its own method rather then using Composition.

# When to use composition:

# 1. When we need more flexibility in constructing objects by assembling smaller, reusable components.
# 2. We should also use composition when there is no clear is a relationship and there is has a relationship
# 3. Whe you want to avoid coupling and fragile base class problems 

# When use to Inheritance:

# 1. When there is "is a" relationship and the subclass objects can be treated as instances of their superclass.
# 2. When you want to promote code reuse by inheriting properties and behaviors from existing classes.

# But remember both composition and inheritance can be used to leverage polymorphism to allow objects to be treated uniformly via their interface or parent class. 

