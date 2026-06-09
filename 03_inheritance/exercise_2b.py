# IMPORTANT RULE ABOUT super()
#
# When a child class defines its own __init__(),
# the parent's __init__() is NOT called automatically.
#
# Use:
#     super().__init__(...)
#
# to call the parent constructor and initialize
# the attributes defined in the parent class.
#
# The arguments passed to super().__init__()
# must match the parameters expected by the
# parent class constructor.
#
# Example:
#
# Parent:
#     class User:
#         def __init__(self, name, email):
#             self.name = name
#             self.email = email
#
# Child:
#     class Student(User):
#         def __init__(self, name, email):
#             super().__init__(name, email)
#             self.courses = []
#
# Result:
#     self.name      -> initialized by User
#     self.email     -> initialized by User
#     self.courses   -> initialized by Student
# Same example using super():

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def login(self):
        print(f"{self.name} logged in successfully!")
        
    def display_info(self):
        print("details:")
        print("Name:",self.name)
        print("Email:",self.email)
        
class Student(User):
    
    def __init__(self, name, email):
        super().__init__(name,email)
        self.course = []
        
        
        
    def enroll_course(self,course):
        self.course.append(course)
        print("courses enrolled are: ",self.course)
        
class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.created_course = []
        
    def add_the_course(self, add_course):
        self.created_course.append(add_course)
        print(f"{self.created_course} added successfully!")
        
s1 = Student("John",'john@yahoo.com')
s1.login()
s1.enroll_course("SQL")
s1.enroll_course("LLM")

i1 = Instructor("Maria","maria@gmail.com")
i1.login()
i1.display_info()
i1.add_the_course("Fine Tuning LLMs")


