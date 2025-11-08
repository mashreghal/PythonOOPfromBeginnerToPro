"""
Interface Segregation Principle (ISP) states that no client should be forced to depend on methods it does not use. 
This means that larger interfaces should be split into smaller, more specific ones so that clients only need to
know about the methods that are relevant to them.
Iny python whenever you see the term interface, think abstract base classes (ABCs) and abstract methods.
"""    
#Let's look at a bad example that violates the Interface Segregation Principle (ISP)
from abc import ABC, abstractmethod
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class RobotWorker(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")
    
#Example usage This is a function that has a Worker object as parameter
def manage_worker(worker:Worker):
    worker.work()
    worker.eat()

human = HumanWorker()
manage_worker(human)  # Works fine

robot = RobotWorker()
manage_worker(robot)  # Raises NotImplementedError
#In this bad example, the RobotWorker class violates the Interface Segregation Principle because it is forced to implement the eat method, which it does not use.

#---------------------Solution------------------------------
#Let's refactor the code to adhere to the Interface Segregation Principle by splitting the Worker interface into smaller, more specific interfaces.

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class RobotWorker(Workable):
    def work(self):
        print("Robot working")

#Example usage
def manage_workable(workable:Workable):
    workable.work() 

human = HumanWorker()
manage_workable(human)  # Works fine

robot = RobotWorker()
manage_workable(robot)  # Works fine

#In this refactored example, we created two separate interfaces: Workable and Eatable
#The HumanWorker class implements both interfaces, while the RobotWorker class only implements the Workable interface. 
# This way, each class only depends on the methods that are relevant to them, adhering to the Interface Segregation Principle.
#It makes sense to inherently separate the abilities of working and eating into different interfaces, as not all workers (like robots) need to eat.

#-----------------------------------------------------------------------------------------------------------
# RELATIONSHIP BETWEEN ISP AND LSP
#-----------------------------------------------------------------------------------------------------------
# ISP (Interface Segregation Principle):
#   - About NOT FORCING classes to implement methods they don't need
#   - Focus: "Should this interface have all these methods, or should it be split?"
#   - Example: Don't force Robot to implement eat() if robots don't eat
#
# LSP (Liskov Substitution Principle):
#   - About BEHAVIORAL COMPATIBILITY between parent and child classes
#   - Focus: "Can I replace a parent with a child without breaking things?"
#   - Example: Ostrich shouldn't override fly() to throw an error (breaks expected behavior)
#
# HOW THEY'RE RELATED:
#   - ISP violations often lead to LSP violations
#   - In the bad example: Robot is forced to implement eat(), so it throws an error (ISP violation)
#   - This also violates LSP because manage_worker(robot) breaks when it calls robot.eat()
#   - The solution: Split Worker into Workable and Eatable (applying ISP)
#   - Now Robot only implements Workable, so it can't be misused (achieves LSP too)
#
# THINK OF IT THIS WAY:
#   - ISP = "Don't force children to do things they can't" (interface appropriateness)
#   - LSP = "All children must behave like their parents expect" (behavioral correctness)
#   - They work together: Proper interface segregation prevents behavioral incompatibility