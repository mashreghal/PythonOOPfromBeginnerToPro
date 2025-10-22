"""
Static methods are methods that belong to the class rather than any instance. They can be called on the class itself without creating an instance.
"""

class BankAccount:
    MIN_BALANCE = 100 # Static attribute for minimum balance requirement

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    #Instance method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")

    # Static method
    @staticmethod
    def is_valid_interest_rate(rate):
        """Check if the given interest rate is valid (between 0 and 5%"""
        return 0 <= rate <= 5
    

# Let's show an exampel of this in action
account = BankAccount("Alice", 500)
account.deposit(200) # Instance method call
# Static method call
print(BankAccount.is_valid_interest_rate(3))  # True
print(BankAccount.is_valid_interest_rate(6))  # False