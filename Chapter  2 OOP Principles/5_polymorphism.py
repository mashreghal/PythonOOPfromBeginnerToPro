"""
The word polymorphism is derived from Greek and means having multiple forms
Poly  = many
Morph = forms
In programming, polymorphism is the ability of an object to take on many forms.
"""

# First let's checkout an example without polymorphism

class Car:
    def __init__(self,brand,model,year,number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is startinng..")

    def stop(self):
        print("Car is stopping.")


class Motorcycle:
    def __init__(self,brand,model,year,has_sidecar):
        self.brand = brand
        self.model = model
        self.year = year
        self.has_sidecar = has_sidecar

    def start(self):
        print("Motorcycle is starting..")

    def stop(self):
        print("Motorcycle is stopping.")


#create a list of vehicles to inspect
vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Motorcycle("Harley-Davidson", "Street 750", 2019, False)
]

#loop through the vehicles and start and stop each one
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Motorcycle):
        vehicle.start()
        vehicle.stop()
# As you can see above we had to check the type of each vehicle to call the start and stop methods.
# Now let's see how polymorphism can help us simplify this code
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        raise NotImplementedError("Subclasses must implement this method")

    def stop(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def start(self):
        print("Car is starting..")

    def stop(self):
        print("Car is stopping.")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def start(self):
        print("Motorcycle is starting..")

    def stop(self):
        print("Motorcycle is stopping.")

# Create a list of vehicles to inspect
vehicles = [
    Car("Toyota", "Camry", 2020, 4),
    Motorcycle("Harley-Davidson", "Street 750", 2019, False)
]

# Loop through the vehicles and start and stop each one
for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
# As you can see above, with polymorphism, we don't need to check the type of each vehicle.
# We can simply call the start and stop methods on each vehicle, and the correct method will be invoked based on the object's class.
# This makes the code more flexible and easier to maintain.

