"""
You are building a system to model different types of employees in an organization. Employees can be either full-time or part-time. The system needs to calculate the monthly salary of each employee based on their working hours and rate of pay.

The requirements are:

Create an abstract class Employee with:

An abstract method calculate_salary() to compute the employee’s salary.
A constructor (__init__) that takes the name of the employee and initializes it.
An instance method describe() that prints the employee's name and type.
Create two subclasses FullTimeEmployee and PartTimeEmployee that inherit from Employee:

The FullTimeEmployee class should have a fixed monthly salary of $3000 and should implement the calculate_salary() method to return this salary.
The PartTimeEmployee class should have a hours_worked and hourly_rate attribute. The calculate_salary() method should compute the salary as hours_worked * hourly_rate.
Demonstrate how to:

Create instances of FullTimeEmployee and PartTimeEmployee.
Use the describe() method.
Call the calculate_salary() method to compute the salary.

"""

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    def __init__(self, name):
        self.name=name

    def describe(self):
        return f"Name: {self.name} \nType: {self.__class__.__name__}"


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Monthly Salary: $3000"

class PartTimeEmployee(Employee):

    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

full_time_name=input("Enter the name of the full time employee:")
f=FullTimeEmployee(full_time_name)
print(f.describe())
print(f.calculate_salary())
print()

while True:
    try:
        part_time_name=input("Enter the name of the part time employee:")
        hours_worked=float(input("Enter the hours worked:"))
        hourly_rate=float(input("Enter the hourly rate: "))
        p=PartTimeEmployee(part_time_name,hours_worked,hourly_rate)
        print(p.describe())
        print(p.calculate_salary())
        print()
        break

    except Exception as e:
        print(e)
        print("Please try again with a valid input")
        print()
    
