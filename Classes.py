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