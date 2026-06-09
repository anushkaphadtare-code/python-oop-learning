'''
Method Overriding
-----------------
Method overriding occurs when a child class provides
its own implementation of a method that already exists
in the parent class.

Rules:
- Same method name
- Same parameter list (recommended)
- Child version takes precedence

Why Use It?
- Customize inherited behavior
- Provide child-specific implementations
- Support polymorphism (later topic)

Parent method can still be accessed using:
super().method_name()

'''

# Exercise: Notification System:
class Notification:
    def __init__(self, message):
        self.message = message
        
    def send(self):
        print("Sending generic notification:",self.message)
        
class EmailNotification(Notification):
    def send(self):
        print("Sending email: ",self.message)
        
class SMSNotification(Notification):
    def send(self):
        super().send() # Calling the send() of parent class 
        print("Sending SMS:",self.message)
        
email = EmailNotification("Welcome to the platform")
sms = SMSNotification("Your OTP is 1234")

email.send()
sms.send()


"""
OOP Exercise: Method Overriding using a Notification System

Objective:
Learn how child classes can provide their own implementation of
a method inherited from a parent class through method overriding.

Scenario:
A generic Notification class is used as a base class.
Different notification types such as Email and SMS customize
the notification sending behavior by overriding the send() method.

Requirements:
1. Create a parent class:
   - Notification
   - Store a notification message
   - Implement a generic send() method

2. Create child classes:
   - EmailNotification
   - SMSNotification

3. Override the send() method in child classes to provide
   notification-specific behavior.

4. Demonstrate how a child class can still access the parent
   implementation using:
       super().send()

Concepts Practiced:
- Inheritance
- Method Overriding
- Parent Class (Base Class)
- Child Class (Derived Class)
- Constructor Inheritance
- super()
- Method Resolution

Method Overriding:
When a child class defines a method with the same name as a
method in the parent class, the child version takes precedence.

Example:
Parent:
    send()

Child:
    send()

Result:
    Python executes the child's implementation instead of
    the parent's implementation.

Using super():
The parent method can still be called from the child class using:

    super().send()

This allows a child class to extend the parent's behavior
instead of completely replacing it.

Learning Outcome:
Understand how inherited methods can be customized in child
classes while preserving code reusability. Learn how method
overriding enables different classes to perform the same
operation in different ways.
"""
