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
    
