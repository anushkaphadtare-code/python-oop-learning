class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def login(self):
        print(f"{self.name} logged in successfully!")
        
    def display_info(self):
        print("Details are:")
        print("Name:",self.name)
        print("Email:",self.email)
        
class Student(User):
    def enroll_course(self, course_name):
        self.course_name = []
        self.course_name.append(course_name)
        print("Enrolled courses are: ", self.course_name)
        
class Instructor(User):
    def create_course(self):
        print("Course created successfully!")
        
s1 = Student("John","john@yahoo.com")
s1.login()
s1.display_info()
s1.enroll_course("SQL")
s1.enroll_course("Python") # new list creates and Python is the first element

i1 = Instructor("Maria", "maria@gmail.com")
i1.login()
i1.display_info()
i1.create_course()


# Here the major problem is the list for enroll_course is getting created everytime
# Hence, courses has nowhere proper to be initialized
# creating it inside enroll_course(): list recreates every call

# THE PROBLEM HERE IS:
# How do I give Student its own attributes while still keeping the parent attributes??!!


'''We cannot write self.course = [] directly inside the class body(above the def enroll_course()) 
because self only exists when an object is created and a method is running. 
At class definition time, there is no object yet, so Python doesn't know what self refers to.

We can write course = [] above the def enroll_course() but this course list will be common 
for all objects and we want separate list of enrolled courses per student.
'''
