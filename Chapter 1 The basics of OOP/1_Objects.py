"""
Understanding 'self' in Python Classes
======================================

WHAT IS SELF?
- 'self' is a reference to the INSTANCE (object) of the class
- It allows each object to access its own attributes and methods
- It's automatically passed when you call a method on an object

BEFORE INSTANTIATION:
- 'self' is just a parameter placeholder in the method definition
- The class is like a blueprint - self doesn't "exist" until an object is created

AFTER INSTANTIATION:
- 'self' refers to the specific object that was created
- Each object has its own 'self' pointing to itself
"""

class Dog:
    def __init__(self, first_name, last_name, breed):
        # At this moment, 'self' refers to the NEW object being created
        # self.first_name means "this object's first_name attribute"
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed
        print(f"Inside __init__, self is: {self}")

    def bark(self):
        # Here, 'self' refers to whichever Dog object called this method
        return f"{self.first_name} says Woof!"
    
    def get_full_name(self):
        return f"{self.first_name} "" {self.last_name}"
    
    def show_identity(self):
        # This method demonstrates what 'self' actually is
        print(f"self is: {self}")
        print(f"self's type: {type(self)}")
        print(f"self's id: {id(self)}")
        return self


# ============================================
# DEMONSTRATION: Understanding 'self'
# ============================================

print("=" * 50)
print("BEFORE INSTANTIATION:")
print("The class Dog exists, but 'self' doesn't exist yet.")
print("'self' is just waiting in the method definitions.")
print("=" * 50)

# Creating first object
print("\n--- Creating dog1 ---")
dog1 = Dog("Buddy", "Smith", "Golden Retriever")
print(f"dog1 object is: {dog1}")
print(f"dog1's id: {id(dog1)}")

# Creating second object
print("\n--- Creating dog2 ---")
dog2 = Dog("Max", "Jones", "Beagle")
print(f"dog2 object is: {dog2}")
print(f"dog2's id: {id(dog2)}")

print("\n" + "=" * 50)
print("AFTER INSTANTIATION:")
print("Now 'self' exists! Each object has its own 'self'")
print("=" * 50)

# When dog1 calls a method, 'self' = dog1
print("\n--- dog1 calling show_identity() ---")
print("When dog1.show_identity() is called, self = dog1")
returned_value = dog1.show_identity()
print(f"Method returned: {returned_value}")
print(f"Is returned value the same as dog1? {returned_value is dog1}")

# When dog2 calls a method, 'self' = dog2
print("\n--- dog2 calling show_identity() ---")
print("When dog2.show_identity() is called, self = dog2")
returned_value = dog2.show_identity()
print(f"Method returned: {returned_value}")
print(f"Is returned value the same as dog2? {returned_value is dog2}")

print("\n" + "=" * 50)
print("KEY INSIGHT:")
print("=" * 50)
print("• 'self' in the class definition is just a placeholder")
print("• When dog1.bark() is called, Python automatically does: Dog.bark(dog1)")
print("• When dog2.bark() is called, Python automatically does: Dog.bark(dog2)")
print("• That's why each object can have different attribute values!")

print("\n--- Calling bark() on different objects ---")
print(f"dog1.bark(): {dog1.bark()}")
print(f"dog2.bark(): {dog2.bark()}")

print("\n--- Behind the scenes (equivalent calls) ---")
print(f"Dog.bark(dog1): {Dog.bark(dog1)}")
print(f"Dog.bark(dog2): {Dog.bark(dog2)}")

print("\n" + "=" * 50)
print("CONCLUSION:")
print("=" * 50)
print("✓ Before instantiation: 'self' is just a parameter in method definitions")
print("✓ After instantiation: 'self' refers to the specific object")
print("✓ Each object's 'self' points to itself")
print("✓ This allows each object to maintain its own unique state")
