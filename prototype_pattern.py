# The Prototype Pattern is a Creational Design Pattern that allows objects to be copied or cloned providing a mechanism to create new objects by copying existing objects without explicitly invoking their constructors or in Python their __init__ methods and its used to efficiently produce new instances with identical properties to existing objects.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self):
        self.radius = 5
    
    def draw(self):
        print(f"Drawing Circle with radius of {self.radius}")

class Rectangle(Shape):
    def __init__(self):
        self.height = 5
        self.width = 10
    
    def draw(self):
        print(f"Drawing Rectangle with height = {self.height} and width = {self.width}")

class ShapeActions:
    def duplicate(self, shape: Shape):
        if isinstance(shape,Circle):
            new_circle = Circle()
            new_circle.radius = shape.radius
            new_circle.draw()
        
        elif isinstance(shape, Rectangle):
            new_rect = Rectangle()
            new_rect.height = shape.height
            new_rect.width = shape.width
            new_rect.draw()
        else:
            raise ValueError("Invalid Shape")

# USer adds a new circle to GUI

circle = Circle()
circle.draw()

# USer clicks and add on circle to resize

circle.radius = 12
circle.draw()

# USer adds a rectangle to GUI
rect = Rectangle()
rect.draw()

# User clicks and add on Circle to resize

rect.width =  20
rect.height = 12
rect.draw()

shape_action = ShapeActions()
shape_action.duplicate(circle)
shape_action.duplicate(rect)

# If we look at the above code we can easily say that it is violating the Open/Close Principle as because to add a new shape we need to change conditionals or add more conditionals in ShapeActions. Another issue is that ShapeActions class in couples to the concrete Shape Classes so ShapeActions has to know about all the different types of shape and their specific methods and this lack of flexibilty makes it difficult to extend the application. 

# For example if we want to ask external developers to add new shapes as plugins for ShapeActions need to be modified to support each new shape making this impractical and inflexible. 

# How to solve the problem?

# The logic for duplicating a shape can be moved to each concrete shape class rather than having rather than having it all in the ShapeActions duplicate method and then we can decouple ShapeActions of all of the concrete shapes and have it to talk a shape interface. So after this ShapeActions has essentially been lifted to talk to the single Shape interface whereas before it was talking to all concrete classes 

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def duplicate(self) -> Shape:
        pass



class Circle(Shape):
    def __init__(self,raidus):
        self.radius = raidus
    
    def draw(self):
        print(f"Drawing Circle with radius of {self.radius}")
    
    def duplicate(self):
        new_circle = Circle(self.radius)
        return new_circle

class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width
    
    def draw(self):
        print(f"Drawing Rectangle with height = {self.height} and width = {self.width}")

    def duplicate(self):
        new_rect = Rectangle(self.width,self.height)
        return new_rect

class ShapeActions:
    def duplicate(self, shape: Shape):
        new_shape = shape.duplicate()
        new_shape.draw ()
        # if isinstance(shape,Circle):
        #     new_circle = Circle()
        #     new_circle.radius = shape.radius
        #     new_circle.draw()
        
        # elif isinstance(shape, Rectangle):
        #     new_rect = Rectangle()
        #     new_rect.height = shape.height
        #     new_rect.width = shape.width
        #     new_rect.draw()
        # else:
        #     raise ValueError("Invalid Shape")

shape_action =ShapeActions()
circle = Circle(5)
circle.draw()

shape_action.duplicate(circle)

rect = Rectangle(10,5)
rect.draw()
shape_action.duplicate(rect)
