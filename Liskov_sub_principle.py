# Liskov Surbstitution Pinciple

# Objects of a superclass should be replaceable with objects of a sub class without affecting the correctness of the program. And this principle ensures that inheritance hierarchies are well designed and that subclassses adhere to the contracts defined by the superclasses and violations of the Liskov Substitution Principle can lead to unexpected behavior or errors when substituting objects making code harder to reason about and maintain. 

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        '''Calculating area of a given shape'''
        pass

class Rectangle(Shape):
    def __init__(self,height : float = 0.0 ,width : float = 0.0 ):
        self._height = height
        self._width = width
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float = 0.0):
        self._width = value
    
    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, new_height : float = 0.0):
        self._height = new_height

    def area(self):
        return self._height * self._width

# Now creating a new class for Square which will inherit from Rectangle class considering that Rectangle is a kind of square with equal sides.

class Square(Rectangle):
    def __init__(self, side : float = 0.0 ):
        super().__init__(side, side)

# Also we need to override the setter and getter property of Rectangle in Square Class because we need to have the same value for both height and width 

    @Rectangle.width.setter
    def width(self,value : float = 0.0 ):
        self._height = value
        self._width = value

    @Rectangle.height.setter
    def height(self,value : float = 0.0 ):
        self._height = value
        self._width = value

rect = Rectangle()
rect.height = 5.0
rect.width = 4.0
rect.area()
print(rect.area())
square = Square()
square.width = 4.0
square.height = 5.0
print(square.area())

# In our program, square class inherits or extends the Rectangle class because mathematically Square is a type of Rectangle. 
# So now we will try to substitute the methods of superclass by the subclass "Square" methods. Thus when we run the code the objects of superclass will be over ridden by subclass square. Thus it violates Liskov Substitution Principle. So by modelling the square class as a subclass of Rectangle and width and height to be independently set we are violating the Liskov Principle.

# Refactored Solution 

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        '''Calculating area of a given shape'''
        pass

class Rectangle(Shape):
    def __init__(self,height : float = 0.0 ,width : float = 0.0 ):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

class Square(Shape):
    def __init__(self, side : float = 0.0 ):
        self.side = side
    
    def area(self):
        return self.side * self.side

rect = Rectangle(height=5,width=10)
# print(rect.area())
square = Square(side=10)
# print(square.area())

# Now lets see how this refactored code satisfies the liskov principle : We have a superclass called Shape - 

def shape_area(shape:Shape):
    return shape.area()

print(shape_area(rect))
print(shape_area(square))

# Thus when we run this function then we can substitute any shape in the function and get its area instantly. Thus satisfying Liskov Principle