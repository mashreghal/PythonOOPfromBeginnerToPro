"""
Static Attributes Example
========================

Static attributes (also called class attributes) are shared among all instances
of a class. They belong to the class itself rather than to any specific instance.
"""

class BankAccount:
    # ========== STATIC ATTRIBUTES (CLASS ATTRIBUTES) ==========
    # These belong to the CLASS itself, NOT to individual instances
    # They are SHARED among ALL instances of the class
    
    bank_name = "Global Bank"      # ← STATIC: Same bank for all accounts
    interest_rate = 0.03           # ← STATIC: Same rate for all accounts (3%)
    total_accounts = 0             # ← STATIC: Counts ALL accounts created
    
    # Why use static attributes?
    # 1. MEMORY EFFICIENCY: Only one copy exists, not one per instance
    # 2. SHARED DATA: Information that should be the same for all instances
    # 3. CLASS-LEVEL COUNTERS: Track statistics across all instances
    # 4. CONFIGURATION: Settings that apply to the entire class
    
    def __init__(self, account_holder, initial_balance=0):
        # ========== INSTANCE ATTRIBUTES ==========
        # These belong to THIS SPECIFIC INSTANCE only
        # Each object has its own copy of these attributes
        
        self.account_holder = account_holder    # ← INSTANCE: Different for each account
        self.balance = initial_balance          # ← INSTANCE: Each account has different balance
        
        # Increment the STATIC counter when a new account is created
        # Notice: We use ClassName.attribute to access static attributes
        BankAccount.total_accounts += 1         # ← Modifying STATIC attribute
    
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount")
    
    def calculate_interest(self):
        """Calculate interest using the STATIC interest rate"""
        # Using STATIC attribute: BankAccount.interest_rate
        # This ensures all accounts use the SAME interest rate
        interest = self.balance * BankAccount.interest_rate  # ← STATIC attribute usage
        return interest
    
    def display_account_info(self):
        """Display account information"""
        print(f"Bank: {BankAccount.bank_name}")                    # ← STATIC attribute
        print(f"Account Holder: {self.account_holder}")            # ← INSTANCE attribute
        print(f"Balance: ${self.balance}")                         # ← INSTANCE attribute
        print(f"Interest Rate: {BankAccount.interest_rate * 100}%") # ← STATIC attribute
    
    @classmethod
    def get_total_accounts(cls):
        """Class method to access static attribute"""
        return cls.total_accounts
    
    @classmethod
    def set_interest_rate(cls, new_rate):
        """Class method to modify static attribute"""
        cls.interest_rate = new_rate
        print(f"Interest rate updated to {new_rate * 100}%")


# Example usage demonstrating static attributes
if __name__ == "__main__":
    print("=== Static Attributes Demo ===\n")
    
    # Show initial static values
    print(f"Bank Name: {BankAccount.bank_name}")
    print(f"Interest Rate: {BankAccount.interest_rate * 100}%")
    print(f"Total Accounts: {BankAccount.total_accounts}\n")
    
    # Create first account
    print("Creating first account...")
    account1 = BankAccount("Alice Johnson", 1000)
    account1.display_account_info()
    print(f"Total Accounts after creation: {BankAccount.total_accounts}\n")
    
    # Create second account
    print("Creating second account...")
    account2 = BankAccount("Bob Smith", 1500)
    account2.display_account_info()
    print(f"Total Accounts after creation: {BankAccount.total_accounts}\n")
    
    # Demonstrate that static attributes are shared
    print("=== Static Attributes Are Shared ===")
    print(f"Account1 sees bank name: {account1.bank_name}")
    print(f"Account2 sees bank name: {account2.bank_name}")
    print(f"Both access the same static attribute: {account1.bank_name == account2.bank_name}\n")
    
    # Change static attribute through class
    print("Changing interest rate through class...")
    BankAccount.set_interest_rate(0.05)  # 5%
    
    print(f"Account1 sees new rate: {account1.interest_rate * 100}%")
    print(f"Account2 sees new rate: {account2.interest_rate * 100}%")
    print("Both instances see the updated static attribute!\n")
    
    # Calculate interest using static rate
    print("=== Interest Calculations ===")
    interest1 = account1.calculate_interest()
    interest2 = account2.calculate_interest()
    print(f"Alice's interest: ${interest1:.2f}")
    print(f"Bob's interest: ${interest2:.2f}\n")
    
    # Access static attribute through class vs instance
    print("=== Accessing Static Attributes ===")
    print(f"Through class: BankAccount.total_accounts = {BankAccount.total_accounts}")
    print(f"Through instance: account1.total_accounts = {account1.total_accounts}")
    print(f"Through class method: {BankAccount.get_total_accounts()}")
    
    # Create third account to see counter increment
    print("\nCreating third account...")
    account3 = BankAccount("Charlie Brown", 500)
    print(f"Total accounts now: {BankAccount.get_total_accounts()}")
    
    print("\n=== MEMORY COMPARISON DEMO ===")
    print("Static Attributes (ONE copy for all instances):")
    print(f"  BankAccount.bank_name memory location: {id(BankAccount.bank_name)}")
    print(f"  account1.bank_name memory location:    {id(account1.bank_name)}")
    print(f"  account2.bank_name memory location:    {id(account2.bank_name)}")
    print(f"  account3.bank_name memory location:    {id(account3.bank_name)}")
    print("  ↑ Notice: ALL point to the SAME memory location!")
    
    print("\nInstance Attributes (SEPARATE copy for each instance):")
    print(f"  account1.account_holder memory location: {id(account1.account_holder)}")
    print(f"  account2.account_holder memory location: {id(account2.account_holder)}")
    print(f"  account3.account_holder memory location: {id(account3.account_holder)}")
    print("  ↑ Notice: Each has its OWN memory location!")
    
    print("\n" + "="*60)
    print("KEY CONCEPTS: STATIC vs INSTANCE ATTRIBUTES")
    print("="*60)
    
    print("\n🔹 STATIC ATTRIBUTES (Class Attributes):")
    print("   - bank_name, interest_rate, total_accounts")
    print("   - Belong to the CLASS itself")
    print("   - SHARED by ALL instances")
    print("   - Only ONE copy exists in memory")
    
    print("\n🔸 INSTANCE ATTRIBUTES:")
    print("   - account_holder, balance")
    print("   - Belong to INDIVIDUAL objects")
    print("   - UNIQUE for each instance")
    print("   - Each object has its own copy")
    
    print("\n" + "="*60)
    print("WHY USE STATIC ATTRIBUTES? - ADVANTAGES")
    print("="*60)
    
    print("\n✅ 1. MEMORY EFFICIENCY:")
    print("   - Only one copy of static data exists")
    print("   - Saves memory when you have many objects")
    print(f"   - Example: All {BankAccount.total_accounts} accounts share the same bank_name")
    
    print("\n✅ 2. CONSISTENCY:")
    print("   - Ensures all instances use the same values")
    print("   - Example: All accounts have the same interest_rate")
    
    print("\n✅ 3. CENTRALIZED CONTROL:")
    print("   - Change once, affects all instances")
    print("   - Example: Update interest_rate for ALL accounts at once")
    
    print("\n✅ 4. CLASS-LEVEL STATISTICS:")
    print("   - Track information across all instances")
    print("   - Example: total_accounts counts ALL created accounts")
    
    print("\n✅ 5. CONFIGURATION MANAGEMENT:")
    print("   - Store settings that apply to the entire class")
    print("   - Example: bank_name is the same for all accounts")
    
    print("\n" + "="*60)
    print("WHEN TO USE STATIC ATTRIBUTES")
    print("="*60)
    print("Use static attributes when:")
    print("• Data should be SHARED among all instances")
    print("• You need CLASS-LEVEL counters or statistics")
    print("• Configuration applies to ALL objects of that class")
    print("• You want to save memory by avoiding duplicate data")
    print("• You need constants that belong to the class")
