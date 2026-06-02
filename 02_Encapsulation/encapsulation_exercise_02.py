"""
OOP Exercise: Bank Account System using Python Properties (@property)

Objective:
Learn Pythonic encapsulation by using private attributes along with
@property and @property.setter to provide controlled access to object data
without explicitly creating getter and setter methods.

Requirements:
1. Store account information using private attributes:
   - __balance

2. Create a property getter to:
   - Read the account balance using attribute-like syntax

3. Create a property setter to:
   - Update the account balance
   - Prevent negative balance values

4. Demonstrate property usage through:
   - Reading balance
   - Updating balance
   - Validating balance updates
   - Using augmented assignment (+=)

Concepts Practiced:
- Classes and Objects
- Constructors (__init__)
- Private Attributes (__variable)
- Encapsulation
- Properties (@property)
- Property Setters (@property_name.setter)
- Data Validation
- Object State Management
- Pythonic Getters and Setters

Learning Outcome:
Understand how Python properties allow methods to be accessed like
attributes while still providing validation and encapsulation.
Learn how @property and @property.setter work together to create
a clean and maintainable interface for object data.
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    # setters typically do not return anything
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            print("Invalid balance")
            return
        else:
            self.__balance = new_balance
            
            
b1 = BankAccount("John", 10000)
print(b1.balance)  # basically this is calling our newly implemented getter method
b1.balance = 15000 # this one calss our newly implemented setter method
print(b1.balance)
b1.balance = -900

b1.balance += 2000
print(b1.balance)
