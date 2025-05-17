# Inheritance - Inheritance is a fundamental concept in OOPS that focuses on creating new classes based on existing classes (super class or base class) and can also add new features or override existing ones and inheritance is always described in terms of relationship between two objects

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.year = year
        self.model = model
    
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, model, year,no_of_doors,no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_doors = no_of_doors
        self.no_of_wheels = no_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year,no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels


car1 = Car("Ford","Focus",2008,5,4)
bike1 = Bike("Honda","Scoopy",2018,2)
print(car1.__dict__)
print(bike1.__dict__)

# Here we can see that since we have created a super class "Vehicle" so we dont have to create start, stop methods twice and also dont have to create attributes like brand, model and year all we do is inherit it. Thus, decreasing the size of the code. Also in case if we have make changes in the inherited methods or attributes we will have to do it only once so it will decrease manual labor 

# Also inheriatnce allows for a very important OOPS concept called Polymorphism.