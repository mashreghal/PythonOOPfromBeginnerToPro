class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Private attribute

#the user passed as parameter is another object and helps understand the concept of self
def sayHiToUser(self,user):
    print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}!")

# let's create two User objects

user1 = User("alice", "alice@gmailcom", "alice123")
user2 = User("bob", "bob@gmailcom", "bob123")

user1.sayHiToUser(user2)  # result : Sending message to bob: Hi bob, it's alice!
user2.sayHiToUser(user1)  # result : Sending message to alice: Hi

# to access/read user's data or methods, we use the dot notation

print(user1.username)  # Output: alice
print(user2.email)     # Output: bob@gmailcom   

# We can also set a user's data to something else:

user1.username = "alice_wonderland"
#------------------------------------------------------
# We need a way of controlling the way we can read or write certain attributes.
# Method 1: The traditional way: make the data private and use getters and setters
# When a developer makes an attribute private, it cannot be accessed directly from outside the class.
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # the __ name mangling makes this attribute private

    # Getter for password
    def get_password(self):
        return self.__password

    # Setter for password
    def set_password(self, new_password):
        if len(new_password) >= 6:  # Simple validation
            self.__password = new_password
        else:
            print("Password must be at least 6 characters long.")

# you can still access protected attributed directly but it's not recommended and bad practice

# If you use __ before an attribute name, it becomes private and cannot be accessed directly from outside the class.
#In summary getters and setters provide controlled access to private attributes, allowing for validation and encapsulation of data within a class.

#------------------The better approach: Using property decorators----------------------
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # private attribute

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 6:  # Simple validation
            self.__password = new_password
        else:
            print("Password must be at least 6 characters long.")

# the great advantage of using property decorators is that you can access the attribute like a normal attribute without needing to call getter and setter methods explicitly.
# So, it is basically the same kind of logic as writing getters and setters , but, in client code, accessing attributes directly and using property decorators looks cleaner and more intuitive.
