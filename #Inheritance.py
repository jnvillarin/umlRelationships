#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
 
    def eat(self):
        print(f"{self.name} is eating.")
 
 
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")
 
 
dog = Dog("Buddy")
dog.eat()   # inherited from Animal
dog.bark()  # defined in Dog