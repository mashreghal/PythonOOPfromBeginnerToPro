"""abstraction in OOP refers to the concept of simplifying complex systems by modeling classes based on the essential properties and behaviors an object should have,
while hiding unnecessary details.
Abstraction allows programmers to focus on interactions at a higher level without needing to understand all the intricate workings of the underlying implementation. """

class EmailService:
    def send_email(self): # Public method to send an email
        # Call private methods within the class
        self._connect()
        self._authenticate()
        self._disconnect()

    def _connect(self):
        """Private method to simulate connecting to an email server"""
        print("Connecting to email server...")

    def _authenticate(self):
        """Private method to simulate authenticating with the email server"""
        print("Authenticating...")

    def _disconnect(self):
        """Private method to simulate disconnecting from the email server"""
        print("Disconnecting from email server...")

    """The user of the class can send emails without knowing any of the internal implementation details involved sending an email. They have been abstracted away and life is simple for the user. """

    email = EmailService()
    email.send_email()

"""In summary, abstraction in OOP helps manage complexity by allowing developers to work with higher-level concepts and interactions, while hiding the lower-level details that are not necessary for the task at hand."""

"""If the methods are protected by being prefixed with an underscore, it communicates to users of the class that these methods are intended for internal use only and should not be accessed directly from outside the class.
The python developer using EmailService class should only interact with the public send_email method, while the internal workings of connecting, authenticating, and disconnecting are hidden from them."""

"""Importantly, by using encapsulation, if any of those protected methods need to change in the future (for example, changing the authentication mechanism), the public interface remains the same. 
This means that users of the EmailService class do not need to worry about those internal changes, as long as the public method send_email continues to function as expected.
"""

"""
From chat gpt:
What’s Actually Going On

Inside the class:

_connect, _authenticate, _disconnect are implementation details.

The leading underscore _ is a Python convention (not a strict rule) indicating:

“This method is intended for internal use; don’t call it from outside.”

So, abstraction here:

Simplifies the interface.

Hides the inner workings.

Ensures consistent behavior through a controlled entry point.

🧠 In Other Words

Abstraction separates:

“What the object does” → send_email()

“How it does it” → _connect(), _authenticate(), _disconnect()

That’s why you can use the class without understanding or touching the lower-level logic.
"""