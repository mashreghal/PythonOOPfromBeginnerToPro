"""Inheritance is a fundamental principle of Object-Oriented Programming (OOP) that allows a class (called a subclass or derived class) to inherit
attributes and methods from another class (called a superclass or base class).
This promotes code reusability and establishes a hierarchical relationship between classes. """

class Vehicel:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")

""" Now all vehicles have common attributes like brand, model, and year, as well as methods to start and stop the vehicle."""

class Car(Vehicel):
    def __init__(self, brand, model, year, num_doors,number_of_wheels=4 ):
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.num_doors = num_doors  # Additional attribute specific to Car
        self.number_of_wheels = number_of_wheels  # Additional attribute specific to Car

    def open_trunk(self):
        print("Trunk is now open.")

class Bike(Vehicel):
    def __init__(self, brand, model, year,number_of_wheels=2):
        super().__init__(brand, model, year)  # Call the constructor of the base class
        self.number_of_wheels = number_of_wheels  # Additional attribute specific to Bike

    def kick_start(self):
        print("Bike is kick-started.")


"""Car and Bike classes inherit from the Vehicle class, gaining access to its attributes and methods. They also have their own specific attributes and methods.
Also note that Inheritance allows for polymorphism......."""

""" A teaser on polymorphism that comes in the next chapter. Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name"""



    