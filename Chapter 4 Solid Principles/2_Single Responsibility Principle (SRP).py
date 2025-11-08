# An example that breaks the Single Responsibility Principle (SRP)
class EmailSender:
    def send(self, subject, recipient):
        print(f"Sending email to {recipient} with subject: {subject}")

class User:
    def __init__(self, username, email):
        self.username = username 
        self.email = email

    def register(self):
        """Registers the user and sends a welcome email."""
        #first responsibility: user registration
        print(f"Registering user: {self.username}") #emulate some registration logic
        #second responsibility: sending email
        email_sender = EmailSender()
        email_sender.send("Welcome!", self.email)


#Example usage
user = User("john_doe", "john_doe@gmail.com")
user.register()

# In this example, the User class has two responsibilities: managing user data and sending emails. This violates the Single Responsibility Principle because the class has more than one reason to change 
#   (e.g., changes in user management or email sending logic).

# Now let us have a look at a refactored example that adheres to the Single Responsibility Principle (SRP)
class EmailService:
    def send(self, subject, recipient):
        print(f"Sending email to {recipient} with subject: {subject}")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def register(self):
        """Registers the user."""
        print(f"Registering user: {self.username}") #emulate some registration logic

#Example usage
user = User("jane_doe", "jane_doe@gamil.com")
user.register()
# Separate responsibility: sending welcome email
email_service = EmailService()
email_service.send("Welcome!", user.email)

# In this refactored example, the User class is only responsible for managing user data and registration, while the EmailService class is responsible for sending emails.
# This adheres to the Single Responsibility Principle because each class has only one reason to change. 

#-----------------------------------------------------------------------------------------------------------
# IMPORTANT: SRP vs COUPLING - What's the difference?
#-----------------------------------------------------------------------------------------------------------
# SRP (Single Responsibility Principle):
#   - About WHAT a class does (its responsibilities)
#   - A class should have ONE REASON TO CHANGE
#   - Focus: COHESION - keeping related things together in one class
#   - Example: User class should only handle user data, not send emails
#
# COUPLING:
#   - About HOW classes interact with each other (dependencies)
#   - Classes should have MINIMAL DEPENDENCIES on other classes
#   - Focus: INDEPENDENCE - reducing connections between classes
#   - Example: User class is tightly coupled to EmailSender if it creates EmailSender() directly
#
# THE CONNECTION:
#   - Following SRP often LEADS TO lower coupling (but they're different concepts)
#   - In the bad example above, User violates SRP (2 responsibilities) AND has high coupling (depends on EmailSender)
#   - In the good example, User follows SRP (1 responsibility) AND has lower coupling (doesn't create EmailService itself)
#   - But you can have SRP without perfect coupling: User.register() still has 1 responsibility even if it creates EmailSender()
#
# THINK OF IT THIS WAY:
#   - SRP = "Do one thing well" (about the class itself)
#   - Coupling = "Don't be too dependent on others" (about relationships between classes)
