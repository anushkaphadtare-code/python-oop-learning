# When a child class defines its own constructor then Python stops automatically using the parent __init__

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def login(self):
        print(f"{self.name} logged in successfully!")
        
    def display_info(self):
        print("details are:")
        print("Name:",self.name)
        print("Email:",self.email)
        
class Student(User):
    def __init__(self,name, email):
        super().__init__(name, email)
        self.course = []
        
        
s1 = Student("John","john@yahoo.com") 
# STEP 1: super().__init__(name,email) calls User.__init__(name, email)
# This creates self.name and self.email

#STEP 2: self.course =[] creates self.course
#Final Object: s1 => name, email, course


'''What does super() mean? 
super() means parent class OR go one level up in the inheritance chain

GOLDEN RULE:
Whenever child class has its own constructor and we still need parent attributes; use:
super().__init__(....)

'''

'''
super()
-------
Used to access methods and constructors of the parent class.

Most common use:
Calling the parent constructor from a child class.

Syntax:
super().__init__(...)

Why Needed?
When a child defines its own __init__(),
the parent's __init__() is not called automatically.

Benefits:
- Reuse parent initialization logic
- Avoid code duplication
- Maintain inheritance hierarchy

Example:
class Student(User):

    def __init__(self, name, email):

        super().__init__(name, email)

        self.courses = []
'''
