"""composition in object-oriented programming (OOP) is a design principle where a class is composed of one or more objects from other classes, rather than inheriting from them.
This allows for greater flexibility and modularity in code design, as objects can be combined and reused in different ways without being tightly coupled through inheritance."""

class Engine:
    def start(self):
        print("Engine started.")

class Wheels:
    def rotate(self):
        print("Wheels are rotating.")

class chassis:
    def support(self):
        print("Chassis is supporting the vehicle.")

class Seats:
    def sit(self):
        print("Sitting on the seat.")


# Car class uses composition to include Engine, Wheels, Chassis, and Seats
class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()
        self.chassis = chassis()
        self.seats = Seats()

    def drive(self):
        self.engine.start()
        self.wheels.rotate()
        self.chassis.support()
        self.seats.sit()
        print("Car is driving.")

my_car = Car()
my_car.drive()

"""Composition vs Inheritance:
Inheritance is a mechanism where a new class derives properties and behavior (methods) from an existing class
Composition, on the other hand, involves building complex objects by combining simpler ones."""