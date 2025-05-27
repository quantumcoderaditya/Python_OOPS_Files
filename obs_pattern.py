# Observer Pattern - The observer pattern which is an object also known as subject, maintaining a list of its dependent objects, called observers and notify them automatically of any state changes.

class Sheet2:
    def __init__(self):
        self.total = 0 
    
    def calculate_total(self,values: list[float]):
        sum = 0
        for value in values:
            sum += value
        
        self.total = sum
        print(f"New Total: {sum}")
        return self.total

class BarCharts:
    def render(self, values: list[float]):
        print("Rendering Bar chart with new values")

class DataSource:
    def __init__(self):
        self._values : list[float] =[]
        self.dependents : list[object] = []

    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self,new_value : list[float]) -> None:
        self._value = new_value
        # Update Dependencies
        for dependent in self.dependents:
            if isinstance(dependent, Sheet2):
                dependent.calculate_total(self._value)
            elif isinstance(dependent, BarCharts):
                dependent.render(self._value)
    
    def add_dependent(self, dependent : object):
        self.dependents.append(dependent)
    
    def remove_dependent(self, dependent : object):
        self.dependents.remove(dependent)

sheet = Sheet2()
barChart = BarCharts()

data_source = DataSource()
data_source.add_dependent(sheet)
data_source.add_dependent(barChart)

data_source.values = [1,2,3,4.1]
print("Removing Bar Chart....")
data_source.remove_dependent(barChart)
data_source.values = [10,1]

# The two most obvious violations we see here are :
# 1. Single Responsibility Principle is being violated because data source has two responsibilities. One of storing data and another of managing dependent observers by adding and removing dependents and its also storing the dependence in a list.

# 2. We are also violating the Open/Close Principle because every time we create a new observer object we have to modify data source 

# How to resolve this:

# 1. For Managing the Single Responsible Principle we can create a new class for managing dependent observers objects. 

# 2. For solving the Open/Close Principle we can say that all observer objects ex sheet2 and Bar Chart implement a common interface so that they provide consistent methods allowing us to use Polymorphism in Data Source.

# Observer Pattern Refactored Code 

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update() -> None :
        pass

class Sheet2(Observer):
    def __init__(self,data_source):
        self.total = 0 
        self.data_source = data_source
    
    def update(self) -> None:
        self.total = self.calculate_total(self.data_source.values)
        
    
    def calculate_total(self,values: list[float]):
        sum = 0
        for value in values:
            sum += value
        
        self.total = sum
        print(f"New Total: {sum}")
        return self.total

class BarCharts(Observer):

    def __init__(self,data_source):
        self.total = 0 
        self.data_source = data_source

    def update(self):
        print("Rendering Bar chart with new values")

class Subject:
    '''This is an Observer Manager'''
    def __init__(self):
        self.observers : list[Observer] = []

    def add_observer(self, observer: Observer):
        '''Method for adding an observer'''
        self.observers.append(observer)
    
    def remove_observer(self,observer:Observer):
        '''Method for removing an observer'''
        self.observers.remove(observer)
    
    def notify_observer(self):
        for obs in self.observers:
            obs.update()


class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self._values : list[float] =[]

    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self,new_value : list[float]) -> None:
        self._value = new_value
        super().notify_observer()
        # # Update Dependencies
        # for dependent in self.dependents:
        #     if isinstance(dependent, Sheet2):
        #         dependent.calculate_total(self._value)
        #     elif isinstance(dependent, BarCharts):
        #         dependent.render(self._value)
    
    # def add_dependent(self, dependent : object):
    #     self.dependents.append(dependent)
    
    # def remove_dependent(self, dependent : object):
    #     self.dependents.remove(dependent)

# sheet = Sheet2()
# barChart = BarCharts()

# data_source = DataSource()
# data_source.add_dependent(sheet)
# data_source.add_dependent(barChart)

# data_source.values = [1,2,3,4.1]
# print("Removing Bar Chart....")
# data_source.remove_dependent(barChart)
# data_source.values = [10,1]

data_source = DataSource()
sheet2 = Sheet2(data_source)
barChart = BarCharts(data_source)

data_source.add_observer(sheet2)
data_source.add_observer(barChart)

print(data_source.values)
data_source.values = [1,2,3,4.1]
