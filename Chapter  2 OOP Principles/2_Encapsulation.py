"""Encapsulation is the principle of bundling data (attributes) and methods (functions) that operate on that data within a single unit, typically a class. 
It restricts direct access to some of an object's components, which helps prevent the accidental modification of data. 
Encapsulation is a fundamental concept in OOP that promotes modularity and maintainability. """

#class with encapsulation of fields and internal logic

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute


    @property
    def balance(self):
        """Getter method to access the balance"""
        return self.__balance
    
    def deposit(self, amount):
        """Public method to deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        """Public method to withdraw money from the account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")
"""The deposit and withdraw methods encapsulate the logic for modifying the balance, ensuring that the balance cannot be set directly from outside the class."""

myAccount = BankAccount(1000)
myAccount.deposit(500)  # Valid deposit 
myAccount.withdraw(200)  # Valid withdrawal
print(myAccount.balance)  # Accessing balance via getter
#myAccount.__balance = 5000  # Attempting to modify private attribute directly 

"""In summary, encapsulation allows for a clear separation between the public interface and the internal implementation of a class, providing usrs with a simplified
and intuitive way to interact with objects while hidng the complexity of how those interactions are handled internally"""