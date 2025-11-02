""" OCP is one of the SOLID principles of object-oriented design.
It states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.
This means that the behavior of a module can be extended without modifying its source code, which helps to prevent bugs and maintain stability in the existing codebase.
You can achieve this by using abstractions, interfaces, and polymorphism to allow new functionality to be added through new code rather than changing existing code.
"""

#Bad example that violates the Open/Closed Principle (OCP)
from enum import Enum
import math

class ShapeType(Enum):
    CIRCLE = "circle"
    RECTANGLE = "rectangle"

class Shape:
    def __init__(self, shape_type:ShapeType, radius:float=0, height:float=0, width:float=0):
        self.shape_type = shape_type
        self.radius = radius
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        if self.shape_type == ShapeType.CIRCLE:
            return math.pi * (self.radius ** 2)
        elif self.shape_type == ShapeType.RECTANGLE:
            return self.height * self.width
        else:
            raise ValueError("Unknown shape type")
        
#Example usage
circle = Shape(ShapeType.CIRCLE, radius=5)
rectangle = Shape(ShapeType.RECTANGLE, height=4, width=6)
print(f"Circle area: {circle.calculate_area()}")
print(f"Rectangle area: {rectangle.calculate_area()}")

#In this bad example, the Shape class violates the Open/Closed Principle
#
#because if we want to add a new shape type (e.g., Triangle), we would need to modify the calculate_area method.

#Let's refactor the code to adhere to the Open/Closed Principle by using polymorphism.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, height:float, width:float):
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width
    
#Example usage
circle = Circle(radius=5)
rectangle = Rectangle(height=4, width=6)
print(f"Circle area: {circle.calculate_area()}")
print(f"Rectangle area: {rectangle.calculate_area()}")

# This is much better! Now, if we want to add a new shape type (e.g., Triangle), we can simply create a new class that inherits from Shape and implements the calculate_area method without modifying any existing code.

#Denke an PGRTs wie die original waren, noch vor der Klasseneinführung