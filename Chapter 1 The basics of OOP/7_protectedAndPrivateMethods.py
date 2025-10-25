#jsut like attributes methods can be protected or private

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def _is_is_valid_amount(self, amount): #this is a protected method meaning it can be accessed by this class and subclasses
        """Protected method to check if the amount is valid (greater than 0)"""
        return amount > 0
    
    def deposit(self, amount):
        """Public method to deposit money into the account"""
        if self._is_is_valid_amount(amount):
            self._balance += amount
            self._log_transcation(amount, "Deposit")
        else:
            print("Deposit amount must be positive")

    def _log_transcation(self, amount, transaction_type): #this is a private method meaning it can only be accessed by this class
        """Private method to log transactions"""
        print(f"Transaction: {transaction_type} of ${amount}. Current balance: ${self._balance}")   


    myAccount = BankAccount(1000)
    myAccount.deposit(500)  # Valid deposit
    myAccount.deposit(-200)  # Invalid deposit

    
