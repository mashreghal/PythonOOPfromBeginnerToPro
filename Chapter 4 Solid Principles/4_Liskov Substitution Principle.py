"""The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
This means that subclasses should extend the behavior of the superclass without changing its original functionality.
To adhere to LSP, subclasses should not override methods in a way that alters the expected behavior of the superclass. Instead, they should enhance or extend the functionality while maintaining the same interface and behavior.
"""

from abc import ABC, abstractmethod

#Bad example that violates the Liskov Substitution Principle (LSP)
class Bird:
    def fly(self):
        print("Flying") 

class Sparrow(Bird):
    pass

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
#
#KEY INSIGHT: The move() method works for ALL subclasses of Bird!
#  - make_bird_move() expects a Bird
#  - You can pass Sparrow, Ostrich, or any other Bird subclass
#  - ALL of them will work correctly without errors or unexpected behavior
#  - This is LSP in action: subclasses are truly substitutable for their base class
#-----------------------------------------------------------------------------------------------------------
# IMPORTANT: LSP vs INHERITANCE - What's the difference?
#-----------------------------------------------------------------------------------------------------------
# LSP (Liskov Substitution Principle):
#   - About BEHAVIOR of subclasses
#   - Subclasses should be replaceable for their base classes without altering the correctness of the program
#   - Focus: BEHAVIORAL COMPATIBILITY - ensuring subclasses behave as expected
#   - Example: An Ostrich should not override fly() to raise an error if Bird
#     defines fly() - violates LSP
# INHERITANCE:
#   - About STRUCTURE of classes        
#   - Mechanism to create a new class based on an existing class
#   - Focus: CODE REUSE - sharing code between classes
#   - Example: An Ostrich can inherit from Bird to reuse code, but must ensure it
#     adheres to LSP by not breaking expected behaviors
#-----------------------------------------------------------------------------------------------------------
# IMPORTANT DISTINCTION: LSP vs POLYMORPHISM
#-----------------------------------------------------------------------------------------------------------
# LSP (Liskov Substitution Principle):
#   - A DESIGN PRINCIPLE that ensures subclasses can stand in for their base classes without altering
#     the correctness of the program
#   - Focuses on BEHAVIORAL COMPATIBILITY between base classes and subclasses
#   - Example: If a function expects a Bird, it should work correctly with any subclass of Bird
# POLYMORPHISM:
#   - A PROGRAMMING CONCEPT that allows objects of different classes to be treated as objects of a common superclass
#   - Enables methods to use objects of different types through a common interface
#   - Example: A function that takes a Bird parameter can accept Sparrow, Ostrich, etc., and call their move() method
# THE CONNECTION:
#   - LSP is a principle that guides how to design class hierarchies to ensure polymorphism works correctly
#   - Polymorphism relies on LSP to ensure that substituting subclasses for base classes does not break the program
#   - Following LSP ensures that polymorphic behavior is predictable and reliable

  