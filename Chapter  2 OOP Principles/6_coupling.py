"""Coupling in object oriented programming refers to the degree of interdependence between software modules.
Low coupling is desirable as it promotes modularity, making the system easier to understand, maintain, and extend.
High coupling, on the other hand, can lead to a system that is difficult to modify and prone to errors, as changes in one module may have unintended consequences in others.
"""

#Bad example of high coupling. Suppose we have two classes 'Order' abd 'EmailSender' where 'Order' class is responsible for creating an order and sending a confirmation email.
# In this bad example, the 'Order' class is tightly coupled with the 'EmailSender' class, making it difficult to change the email sending logic without modifying the 'Order' class.

class EmailSender:
    def send(self,message):
        print(f"Sending email with message: {message}")

class Order:
    def create(self):
        print("Order created.")
        email_sender = EmailSender()
        email_sender.send("Your order has been created.")

order = Order()
order.create()

#In this bad example th e'order' class is tighly coupled to the 'EmailSender' class because it directly creates an instance of 'EmailSender' and calls its 'send' method.
#This makes th 'Order' class dependent on the implementation details of 'EmailSender' and any changes to the 'EmailSender' class may require changes to the 'Order' class as well.

#To reduce coupling we can introduce an abstraction between the 'Order' and 'EmailSender' classes using abstraction, making it easier to change the email sending logic without modifying the 'Order' class.

from abc import ABC, abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self,message:str):
        pass

#Concrete implementation of NotificationService
class EmailService(NotificationService):
    def send_notification(self,message:str):
        print(f"Sending email with message: {message}")

#also create a service for text messages
class SMSService(NotificationService):
    def send_notification(self,message:str):
        print(f"Sending SMS with message: {message}")

#Now the Order class depends on the abstraction NotificationService rather than the concrete implementation EmailService.
class Order:
    def __init__(self, notification_service:NotificationService):
        self.notification_service = notification_service

    def create(self):
        print("Order created.")
        self.notification_service.send_notification("Your order has been created.")

    order = Order(EmailService())
    order.create()
    order_sms = Order(SMSService())
    order_sms.create()

#In this improved example, the 'Order' class depends on the 'NotificationService' abstraction rather than the concrete implementation 'EmailService'. This decouples the 'Order' class from the 'EmailService' class, allowing us to easily switch to a different notification service (like SMSService) without modifying the 'Order' class.
#This decouples the 'Order' class from specific implementation of the notification service, promoting flexibility and maintainability in the codebase. This reduction in coupling makes the system more modular and easier to extend in the future.

#IMPORTANT DISTINCTION: COUPLING vs EXTENSIBILITY
#=========================================================
#COUPLING = The degree of dependency between classes (what we're trying to reduce)
#  - High coupling: Order knows about and directly creates EmailSender() - tight dependency
#  - Low coupling: Order only knows about NotificationService interface - loose dependency
#
#EXTENSIBILITY = The ability to add new features without modifying existing code (the BENEFIT we get from low coupling)
#  - With high coupling: Adding SMS means MODIFYING Order class (not extensible)
#  - With low coupling: Adding SMS/Push/Slack means just creating new classes (highly extensible)
#
#So COUPLING is the PROBLEM we measure, and EXTENSIBILITY is the BENEFIT we gain by reducing coupling.
#They're related but different concepts: Low coupling ENABLES extensibility.

#What are abstract classes and methods in Python?
"""
Abstract classes in Python are classes that cannot be instantiated on their own and are meant to be subclassed. They can contain abstract methods, which are methods declared in the abstract class but do not have an implementation. Subclasses of the abstract class must provide implementations for all abstract methods.
Abstract classes are defined using the 'abc' module in Python, which provides the 'ABC' class and the 'abstractmethod' decorator. An abstract class can have both abstract methods (without implementation) and concrete methods (with implementation). The purpose of abstract classes is to provide a common interface for a group of related classes, ensuring that they implement certain methods while allowing for different implementations.  
In the example above, 'NotificationService' is an abstract class with an abstract method 'send_notification'. 'EmailService' and 'SMSService' are concrete subclasses that implement the 'send_notification' method.
"""