class Person: #This is class definition as we have created a class
    '''This is a person class'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello!!! my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice",30) # This line creates a new object for the class person
person1.greet() # This line is used to call a specific method of a class

person2 = Person("Bob",42)# This line creates a new object for the class person
person2.greet() # This line is used to call a specific method of a class

# Each of the object of class Person greets differently depending upon its attributes. This shows both are independent of each other

