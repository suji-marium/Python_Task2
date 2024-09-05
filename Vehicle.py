
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