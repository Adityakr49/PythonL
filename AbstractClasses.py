# Prevents a user from creating an object of that class +
#compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC,abstractmethod #abc->abstract base class

class Vehicle(ABC):

    @abstractmethod#need atleast one abstract method
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self): #implement all abstract method is inheriting abstract class
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")

# vehicle=Vehicle()
# vehicle.go() #won't work for abstract class

car=Car()
motorcycle=Motorcycle()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()