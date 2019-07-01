# Object Oriented Programming OOP relies on a class structure
# In python EVERYTHING is an object, from a class

class Dog(): # Class definition
    """A simple attempt to model a dog.""" # Description

    def __init__(self, name, age): # Auto-runs 'self' not passed as argument
        """Initialize name and age attributes."""
        self.name = name # self. prefix makes var available to every method in class
        self.age = age # these var are 'attributes'

    def sit(self):
        """Simulate a dog sitting in response to command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in responce to command."""
        print(self.name.title() + " rolled over!")

# This is an 'instance' of a class
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".") # Attribute var.attribute
print("My dog is " + str(my_dog.age) + " year's old.")

# Calling other methods in the class
my_dog.sit()
my_dog.roll_over()

# Here as another instance of the class
your_dog = Dog('Jebodiah', 14)

print("My dog's name is " + your_dog.name.title() + ".") # Attribute var.attribute
print("My dog is " + str(your_dog.age) + " year's old.")
your_dog.roll_over()

# Each instance must occupy its own space in memory


# Clean class based on Resturants
class Resturant():
    """A simple model of an eatery"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
    
    def describe_resturant(self):
        """x2 items of interest"""
        print(self.name.title() + " is very busy on a friday night, and is a " 
                                + self.cuisine.title() + " style eatery.")
     
    def open_resturant(self):
        """Prints message indicating resturant is open"""
        print(self.name.title() + " is now open!\n")

a_resturant = Resturant("russo", "italian")
a_resturant.describe_resturant()
a_resturant.open_resturant()

b_resturant = Resturant("chen", "japanese")
b_resturant.describe_resturant()
b_resturant.open_resturant()

c_resturant = Resturant("knight's arms", "pub fare")
c_resturant.describe_resturant()
c_resturant.open_resturant()

# -------------------------------------------------------------------------------

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to best describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Default Value Attribute that changes over time

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's millage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject change if it attempts to roll back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer Ferris!")

    def increment_odometer(self, miles):
        """Add given amount to odometer reading"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016,)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# ---------------------------------------------------------------------------------

class ElectricCar(Car): # Example of inheritance
    """Represents aspect of the car, specific to electric vehicles."""
    
    # Parent must be in file and before Child
    def __init__(self, make, model, year,): # attributes for Car
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to Elec car.
        """
        super().__init__(make, model, year,) # Calls parent __init__
        self.battery_size = 70
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def fill_gas_tank(self): # If this were in the Parent (same name) you can override method
        """Electric cars don't typically have gas tanks."""
        print("This car doesn;t have a gas tank!")

my_tesla = ElectricCar('tesla', 'models s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()