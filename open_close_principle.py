# Open/Close Principle - Software entities classes/modules/ functions etc should be open for extension but closed for modification. It also encourages the use of abstraction and Polymorphism to achieve this goal allowing the code to be easily extended via inheritance or composition 

from enum import Enum
import math
from abc import ABC,abstractmethod

class ShapeType(Enum):
    CIRCLE = "circle"
    RECTANGLE = "rectangle"

class Shape:
    def __init__(self,shape_type : ShapeType, radius:float = 0,height : float = 0, width : float=0):
        self.type = shape_type
        self.radius = radius
        self.height = height
        self.width = width 
    
    def calculate_area(self):
        if self.type == ShapeType.CIRCLE:
            return 3.14 *self.radius**2
        elif self.type == ShapeType.RECTANGLE:
            return (self.height * self.width)
        else:
            print("Wrong Input")

circle = Shape(ShapeType.CIRCLE,radius=5)
rect = Shape(ShapeType.RECTANGLE,height=4,width=6)

print(f"Circle Area : {circle.calculate_area()}")
print(f"Rectangle Area : {rect.calculate_area()}")

# The above code violates the Open/Closed Principle as the original code need to be modified in ShapeType if lets say we want to calculate area of square or pentagon. So to adhere to Open/ Closed Principle we need create code in such a way that it needs to be open for extension and closed for modification

class Shape(ABC):

    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self,radius):
        self._radius = radius
    
    def calculate_area(self) -> float:
        return math.pi * self._radius**2

class Rectangle(Shape):
    def __init__(self,height,width):
        self._height = height
        self._width = width
    
    def calculate_area(self) -> float:
        return (self._height * self._width)

circle=Circle(5.0)
print(f"Circle Area : {circle.calculate_area()}")
print(f"Rectangle Area : {rect.calculate_area()}")

# Here in the refactored code we have defined a shape class with an abstract calculate_area method and we have now concrete shape classes for Circle and Rectangle which inherits from the shape class and provide their own implementation of calculate_area. so now if we add a new shape such as a triangle then we have to make a Triangle Class. In other words we could extend our code and not modify our code. so here extending our code base simply means we are creating a new class and we would not need to modify the existing code. This is Open/Closed Principle 




