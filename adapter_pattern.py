# Adapter Pattern is a structural design pattern that allows incompatible interfaces between classes to work together by providing a wrapper that translates one interface into another. 

from abc import ABC,abstractmethod

#3rd party color filter
class Rainbow:
    def setup(self):
        print("Setting up the library")
    
    def update(self,video):
        print("Applying our filter to Video")

class Video:
    def play(self):
        print("Playing Video")
    
    def stop(self):
        print("Stopping Video")
    
class Color:
    @abstractmethod
    def apply(self,video):
        pass

class BlackandWhite(Color):
    def apply(self,video):
        print("Applying Black and white color filter")

class MidnightColor(Color):
    def apply(self,video):
        print("Applying Midnight Color color filter")

class VideoEditor:
    def __init__(self,video):
        self.video = video
    
    def apply_color(self,color : Color):
        color.apply(self.video)
        #Applying color using Polymorphism we dont need to worry about Concrete classes 

video = Video
video_editor = VideoEditor(video)
video_editor.apply_color(BlackandWhite())

# Lets assume we want to apply third party library into our application that allows us to apply more type of colors into our videos. Now since this is a 3rd party filter then we cannot touch the code as we dont know the code we have simply imported our library like we import our library in Python pip install pandas 

# The problem here is that all our concrete color classes are expected to implement the color interface. All the color classes that we have created are abstract classes so are easy to apply but that is not the case with 3rd party color classes as they do not have the apply method. 

# We can actually solve this problem by converting the interface of 3rd party classes to another form using the adapter pattern. The solution here is to create our own Color Rainbow class that implements color and is composed of the third party Rainbow Class. We can then implement the apply method inside the Rainbow Class and inside it call whatever methods that we need to call from Rainbow to apply the filter. So effectively we adapt the class into a different form. So we will create a new Rainbow class that will be composed of the Thirty Party class and is inheriting the color abstract class which means that it has an apply method. So the Rainbow color here is the adapter that is effectively converting the interface of the Rainbow (the adaptee) into a different form which in this case is color. 

# Refactored Solution

class Rainbow:
    def setup(self):
        print("Setting up the library")
    
    def update(self,video):
        print("Applying our filter to Video")

class Video:
    def play(self):
        print("Playing Video")
    
    def stop(self):
        print("Stopping Video")
    
class Color:
    @abstractmethod
    def apply(self,video):
        pass

class RainbowColor(Color):

    def __init__(self, rainbow : Rainbow):
        self._rainbow = rainbow
        

    def apply(self, video):
        self._rainbow.setup()
        self._rainbow.update(video)
        

class BlackandWhite(Color):
    def apply(self,video):
        print("Applying Black and white color filter")

class MidnightColor(Color):
    def apply(self,video):
        print("Applying Midnight Color color filter")

class VideoEditor:
    def __init__(self,video):
        self.video = video
    
    def apply_color(self,color : Color):
        color.apply(self.video)
        #Applying color using Polymorphism we dont need to worry about Concrete classes 

video = Video
video_editor = VideoEditor(video)
video_editor.apply_color(RainbowColor(Rainbow()))

# Thus we can see that RainbowColor is a wrapper that translates one interface into another. So to use any other color from the library we need to make adapter class to make it compatible with VideoEditor satisfying the Open/Close Principle.

# Now we created our Adapter class with composition. So our RainbowColor class is composed of Rainbow Objects but its also possible to use inheritance if we had inherited the class it would look like the below:

# class Rainbowcolor(Rainbow,Color) :
#     def apply(self, video: Video):
#         self.setup()
#         self.update(video)
        
# So in inheritance we can call Rainbow methods directly and here we can use Multiple Inheritance as classes can inherit Multiple Classes. However composition is still generally preferred because it leads to more flexible and modular code. 

# As composition reduces coupling making it easier to modify or replace Rainbow without affecting the Rainbow adapter because it also provides better encapsulation because it exposes only the necessary interface which is just apply method to the users of the class where with inheritance the entire interface block gets confusing because all of the public methods and attributes of the rainbow is going to be exposed to all clients which is not desirable, this makes it confusing because its just gonna have that single apply method its gonna have a load of public attributes and methods thats inherited from the Rainbow. So inheritance works perfectly in this case however the composition is the more efficient when it comes to flexibility and maintainability as priorrities.