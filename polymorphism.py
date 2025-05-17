# Polymorphism - It means that it has many forms. In OOPS it means the ability of an object to take many forms.

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
    def __init__(self, brand, model, year,no_of_doors):
        super().__init__(brand,model,year)
        self.no_of_doors = no_of_doors
        # self.no_of_wheels = no_of_wheels
    
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand,model,year)
    def start(self):
        print("Motorcycle is starting!!!")

    def stop(self):
        print("Motorcycle is stopping!!!")

class Plane(Vehicle):
    def __init__(self, brand, model, year,no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels

    def start(self):
        print("Plane is flying")
    
    def stop(self):
        print("Plane is stopping")


vehicles = [
    Car("Ford","Focus",2008,5),
    Motorcycle("Honda","Scoopy",2018)
]

#Looping through Vehicles

# for vehicle in vehicles:
#     if isinstance(vehicle,Car):
#         print(f"{vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start_car()
#         vehicle.stop_car()
#     elif isinstance(vehicle,Motorcycle):
#         print(f"{vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start_bike()
#         vehicle.stop_bike()

#     else:
#         print("Wrong Input")

for vehicle in vehicles:
    if isinstance(vehicle,Vehicle):
        print(f"{vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        print("Wrong Vehicle")

# Here in the above code we have inherited the superclass Vehicle and also overrided its functions like start and stop by naming it similar to start and stop of super class Vehicle 

# So, despite Car and Motorcycle being two different types of vehicles we can treat them as same with the help of Polymorphism and all of the instances of both classes as same of vehicle class 