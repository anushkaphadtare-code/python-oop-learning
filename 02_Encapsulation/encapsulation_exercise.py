"""
OOP Exercise: Bank Account System using Encapsulation

Objective:
Build a BankAccount class to understand the concept of encapsulation
by protecting sensitive account information and controlling access
through methods.

Requirements:
1. Store account information using private attributes:
   - __account_holder
   - __balance

2. Implement methods to:
   - View account balance
   - Deposit money
   - Withdraw money
   - Display account details
   - Update balance with validation

3. Prevent invalid operations such as:
   - Setting a negative balance
   - Withdrawing more money than available
   - Directly accessing private account data

Concepts Practiced:
- Classes and Objects
- Constructors (__init__)
- Private Attributes (__variable)
- Encapsulation
- Getter Methods
- Setter Methods
- Data Validation
- Object State Management
- Name Mangling in Python

Learning Outcome:
Understand how encapsulation helps protect an object's internal state
by hiding implementation details and providing controlled access
through methods. Learn how to enforce business rules and maintain
data integrity within a class.
"""

class BankAccount:
    def __init__(self, name, balance):
        self.__account_holder = name
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance 
            
    def withdraw(self, amount):
        if  amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient balance")
    
    def display_account(self):
        print("Account Holder:", self.__account_holder)
        print("Current Balance:", self.__balance)
        
    def set_balance(self,new_balance):
        if new_balance < 0:
            print("Cannot set balance")
        else:
            self.__balance = new_balance
        
    
        
b1 = BankAccount("John", 8000)
#print(b1.__balance)  #Gives Attribute error
print(b1.get_balance())
print(b1.deposit(2000))
print(b1.withdraw(2000))
print(b1.get_balance())
b1.display_account()
b1.set_balance(-900)
print(b1.get_balance())
