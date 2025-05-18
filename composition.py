# Composition - It involves creating complex object by combining simpler objects or components. So, in composition Objects are assembled together to form larger strucutures with each component object maintaining its own state and behavior. Composition are often described in terms of has a relationship. So you can remember inheritance was described in terms of is a relationship. So for car is a vehicle and bike is a vehicle. While in case of Composition we can say that car has a engine and car has seats.


# Lets define a class "CAR" which has various components like engine,wheels,chasis and seats and each component is going to be a separate class responsible for its implementation and car class is going to consist of each of its instances and is gonna delegate tasks to them. 

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

# Here in the above code we have seen that car is composed of engine,chasis,Wheels and seats and forms a composition in Car class. Here Car claass calls these components methods from its own methods 

        

    
