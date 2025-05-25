# Interface segregation Principle states that client should not be forced to depend on interfaces they do not use. And this principle encourages the creation of fine grained interfaces that contain only the methods required by the clients that use them. It helps to prevent creation of fat interfaces that force clients to implement unnecessary methods leading to more cleaner and maintainable code. Python do not have built in interfaces like java or c# but you can achieve the same effect by using abstract base classes. As we know abstract base classes allow you to define methods that must be implemented by any subclasses effectively acting as interfaces as in other languages. So by carefully designing these abstract classes to contain only methods relevant to specific clients you can adhere to interface segregation principle. 

# Remember : Whenever you see the term interface in Python you must think of abstract base class

from abc import ABC,abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def volume(self):
        raise NotImplementedError("Volume not applicable in case of 2D Shapes ")

class Sphere(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2
    
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
    
    # In this code we have an abstract class representing different shapes. However Volume method is problematic for 2D Shapes like circle because they do not have volumes. And this actually violates the Interface Segregation Principle because clients or classes inheriting from shapes may need to depend on methods they do niot need. So this circle class is forced to depend on volume method that it do not need which violates the Interface Segregation Principle 

circle = Circle(10)
print(f"Circle Area: {circle.area()}")
# print(f"Circle Volume: {circle.volume()}") Uncomment the code to see wrong implementation
sphere = Sphere(10)
print(f"Sphere Area: {sphere.area()}")
print(f"Sphere Volume: {sphere.volume()}")

# When we run the code we will get an NotImplementedError in square volume method because it does not have a vloume thus violating the interface segregation principle 

# Refactored Code - We can try to fix this issue by making one abstract class for 2D shapes and one abstract class for 3D shapes rather than one fit for all shapes which is causing an error 

class Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass

class Shape3D(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape2D):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Sphere(Shape3D):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2
    
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

circle = Circle(10)
print(f"Circle Area: {circle.area()}")
sphere = Sphere(10)
print(f"Sphere Area: {sphere.area()}")
print(f"Sphere Volume: {sphere.volume()}")

# Thus we have segregated the Shape interface to two smaller shapes focused on different types of shapes. And now each shape class only implements the interface relevant to its functionality and this adheres to interface segregation principle 