#Realization
from abc import ABC, abstractmethod
 
 
class Drawable(ABC):  # the "interface"
    @abstractmethod
    def draw(self):
        pass
 
 
class Circle(Drawable):
    def draw(self):
        print("Drawing a circle")
 
 
class Square(Drawable):
    def draw(self):
        print("Drawing a square")
 
 
for shape in [Circle(), Square()]:
    shape.draw()