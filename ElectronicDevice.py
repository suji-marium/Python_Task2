from abc import ABC,abstractmethod

class ElectronicDevice(ABC):
    
    @abstractmethod
    def power_usage(self):
        pass

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def describe(self):
        print(f"Brand: {self.brand} \nModel: {self.model}")

    @classmethod
    def from_type(cls,name):
        if name.lower()=='laptop':
            brand = input("Enter the brand name of the laptop: ")
            model = input("Enter the model of the laptop: ")
            battery_life=float(input("Enter the battery life of laptop: "))
            return Laptop(brand,model,battery_life)

        elif name.lower()=='smartphone':
            brand = input("Enter the brand name of the smartphone: ")
            model = input("Enter the model of the smartphone: ")
            screen_size = float(input("Enter the screen size of smartphone: "))
            return Laptop(brand, model,screen_size)

class Laptop(ElectronicDevice):

    def __init__(self,brand,model,battery_life):
        super().__init__(brand,model)
        self.battery_life=battery_life

    def power_usage(self):
        return "Power consumption per hour of usage (50 watts per hour)"

    def describe(self):
        super().describe()
        print(f"Battery Life: {self.battery_life}")
        

class Smartphone(ElectronicDevice):
    def __init__(self,brand,model,screen_size ):
        super().__init__(brand,model)
        self.screen_size=screen_size

    def power_usage(self):
        return "power consumption per hour of usage (10 watts per hour)"

    def describe(self):
        super().describe()
        print(f"Screen size: {self.screen_size}")

while True:
    try:
        dev_name=input("Enter the device name (laptop/smartphone): ")
        e=ElectronicDevice.from_type(dev_name)
        e.describe()
        print(e.power_usage())
        break

    except Exception as e:
        print(e)
        print("Please try again with a valid input type.")


while True:
    try:
        brand = input("Enter the brand name of the laptop: ")
        model = input("Enter the model of the laptop: ")
        battery_life = float(input("Enter the battery life of laptop: "))

        l = Laptop(brand, model, battery_life)
        l.describe()
        print(l.power_usage())

        brand = input("Enter the brand name of the smartphone: ")
        model = input("Enter the model of the smartphone: ")
        screen_size = float(input("Enter the screen size of smartphone: "))

        s = Smartphone(brand, model, screen_size)
        s.describe()
        print(s.power_usage())
        break

    except Exception as e:
        print(e)
        print("Please try again with a valid input type")



