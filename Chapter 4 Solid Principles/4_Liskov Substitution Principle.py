"""
The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
This means that subclasses should extend the behavior of the superclass without changing its original functionality.
To adhere to LSP, subclasses should not override methods in a way that alters the expected behavior of the superclass. Instead, they should enhance or extend the functionality while maintaining the same interface and behavior.
"""
from abc import ABC, abstractmethod
#Let's start with a bad example that violates the Liskov Substitution Principle (LSP)
class Bird:
    def fly(self):
        print("Flying") 

class Sparrow(Bird):
    pass #inherits fly() as is

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")

#Example usage
def make_bird_fly(bird:Bird):
    bird.fly()

sparrow = Sparrow()
make_bird_fly(sparrow)  # Works fine
ostrich = Ostrich()
make_bird_fly(ostrich)  # Raises NotImplementedError

#In this bad example, the Ostrich class violates the Liskov Substitution Principle because it overrides the fly method in a way that changes the expected behavior of the Bird class.
#Let's refactor the code to adhere to the Liskov Substitution Principle by using interfaces.

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Flying")

class NonFlyingBird(Bird):
    def move(self):
        print("Walking")

class Sparrow(FlyingBird):
    pass

class Ostrich(NonFlyingBird):
    pass

#Example usage
def make_bird_move(bird:Bird):
    bird.move()

sparrow = Sparrow()
make_bird_move(sparrow)  # Works fine 

ostrich = Ostrich()
make_bird_move(ostrich)  # Works fine

#In this refactored example, we created two separate abstract classes: FlyingBird and NonFlyingBird, both inheriting from the Bird interface.
#The Sparrow class inherits from FlyingBird, while the Ostrich class inherits from NonFlyingBird. This way, each subclass adheres to the expected behavior of its parent class without violating the Liskov Substitution Principle.
#This adheres to the Liskov Substitution Principle because any instance of Bird can be replaced with an instance of its subclasses (FlyingBird or NonFlyingBird) without altering the correctness of the program.
#In the end of the day we use Bird objects that behave as expected without surprises.
