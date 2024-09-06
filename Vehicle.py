"""
QUESTION : 1
You are working on a project to model vehicles in a transportation system. You need to create a set of classes that represent different types of vehicles. The requirements are as follows:

Create an abstract class Vehicle with:

An abstract method get_fuel_efficiency() that must be implemented by any subclass.
A regular instance method describe() that prints out a description of the vehicle type.
A class method from_name() that creates an instance of a vehicle based on the vehicle type name provided as a string.
Create two subclasses Car and Truck that inherit from Vehicle:

The Car class should have a get_fuel_efficiency() method that returns a fuel efficiency of 25 miles per gallon.
The Truck class should have a get_fuel_efficiency() method that returns a fuel efficiency of 15 miles per gallon.
Demonstrate how to:

Create instances of Car and Truck.
Use the describe() method.
Call the get_fuel_efficiency() method.
Use the from_name() class method to create a Car or Truck based on a string input.
"""

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_fuel_efficiency(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @classmethod
    def from_name(cls,name):
        if name.lower()=='car':
            return Car()
        elif name.lower()=='truck':
            return Truck()


class Car(Vehicle):
    def get_fuel_efficiency(self):
        return 'A fuel efficiency of 25 miles per gallon'

class Truck(Vehicle):
    def get_fuel_efficiency(self):
        return 'A fuel efficiency of 15 miles per gallon'

while True:
    try:
        veh_name=input("Enter the vehicle name (car/truck): ")
        v=Vehicle.from_name(veh_name)
        print(v.describe())
        print(v.get_fuel_efficiency())
        print()

        c=Car()
        print(c.describe())
        print(c.get_fuel_efficiency())
        print()

        t=Truck()
        print(t.describe())
        print(t.get_fuel_efficiency())
        print()
        break

    except Exception as e:
        print(e)
        print("Please try again with a valid vehicle type.")

