# Abstract Design Pattern is a design pattern that provides an interface for creating families of related objects without specifying their concrete classes, promoting encapsulation and allowing for the creation of object families that can vary independently. 

from enum import Enum
from abc import ABC, abstractmethod

class OperatingSystemType(Enum):
    WINDOWS = "Windows"
    MAC = "Mac"

class UIComponent(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(UIComponent):
    @abstractmethod
    def on_select(self):
        pass

class Button(UIComponent):
    @abstractmethod
    def on_Click(self):
        pass

# Concrete Windows Components

class WindowsButton(Button):
    def render(self):
        print("Rendering Windows")

    def on_Click(self):
        print("Windows Button Clicked")

class WindowsCheckBox(CheckBox):
    def render(self):
        print("Windows Rendering")
    
    def on_select(self):
        print("Windows CheckBox Selected")

# Concrete MAc Components

class MacButton(Button):
    def render(self):
        print("Mac Rendering")
    
    def on_Click(self):
        print("MAc Button Clicked")
 
class MacCheckBox(CheckBox):
    def render(self):
        print("Mac Rendering")
    
    def on_select(self):
        print("Mac CheckBox Selected")

# User Form Classes

class UserSettingsForm:
    def render(self,os : OperatingSystemType):
        if os == OperatingSystemType.WINDOWS:
            WindowsButton().render()
            WindowsCheckBox().render()
        elif os == OperatingSystemType.MAC:
            MacButton().render()
            MacCheckBox().render()

os = OperatingSystemType.MAC
user_Setting_form = UserSettingsForm()
user_Setting_form.render(os)

os = OperatingSystemType.WINDOWS
user_Setting_form = UserSettingsForm()
user_Setting_form.render(os)

# Here in the above code fpor every single UI we build we will need new conditionals to check the Current Operating System which violates the Open/Close Principle 

# So the solution to this is creating Abstract Factory class to create families of UI Components such as the Families of Windows UI Components 

# Refactored Solution

class OperatingSystemType(Enum):
    WINDOWS = "Windows"
    MAC = "Mac"

class UIComponentFactory(ABC):
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> CheckBox:
        pass

class WindowsUIComponentFactory(UIComponentFactory):
    def create_button(self) -> Button :
        return WindowsButton()
    
    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()
    
class MAcUIComponentFactory(UIComponentFactory):
    def create_button(self) -> Button :
        return MacButton()
    
    def create_checkbox(self) -> CheckBox :
        return MacCheckBox()
        

class UIComponent(ABC):
    @abstractmethod
    def render(self):
        pass

class CheckBox(UIComponent):
    @abstractmethod
    def on_select(self):
        pass

class Button(UIComponent):
    @abstractmethod
    def on_Click(self):
        pass

# Concrete Windows Components

class WindowsButton(Button):
    def render(self):
        print("Rendering Windows")

    def on_Click(self):
        print("Windows Button Clicked")

class WindowsCheckBox(CheckBox):
    def render(self):
        print("Windows Rendering")
    
    def on_select(self):
        print("Windows CheckBox Selected")

# Concrete MAc Components

class MacButton(Button):
    def render(self):
        print("Mac Rendering")
    
    def on_Click(self):
        print("MAc Button Clicked")
 
class MacCheckBox(CheckBox):
    def render(self):
        print("Mac Rendering")
    
    def on_select(self):
        print("Mac CheckBox Selected")

# User Form Classes

class UserSettingsForm:
    def render(self,ui_component_factory : UIComponentFactory):
        ui_component_factory.create_button().render()
        ui_component_factory.create_checkbox().render()
        # if os == OperatingSystemType.WINDOWS:
        #     WindowsButton().render()
        #     WindowsCheckBox().render()
        # elif os == OperatingSystemType.MAC:
        #     MacButton().render()
        #     MacCheckBox().render()

# In this new moethod we are using Polymorphism to create our Checkbox and Button rather than having knowledge of what Operating System we are working on before we create our UI Components

os = OperatingSystemType.MAC
ui_component_factory : UIComponentFactory

if os == OperatingSystemType.WINDOWS:
    ui_component_factory = WindowsUIComponentFactory()
elif os == OperatingSystemType.MAC:
    ui_component_factory = MAcUIComponentFactory()
else: 
    raise Exception("Unsupported Operating System")

UserSettingsForm().render(ui_component_factory)

# Now the benefit here is that we have to run only a few conditional statements and not do that in all the classes. And another benefit is that we are satisfying the Open/Close Principle because if we add another Operating System we dont need to make changes to every one of our UI Classes. 

