"""
OOP Exercise: Types of Inheritance in a University Management System

Objective:
Understand and implement different types of inheritance in Python
using a university management system.

Scenario:
A common User class is created to represent all users of the system.
Different user types such as Student, Instructor, and GraduateStudent
inherit and extend the functionality of the User class.

Class Hierarchy:

                User
               /    \
              /      \
        Student    Instructor
            |
            |
            ▼
    GraduateStudent

Inheritance Types Demonstrated:

1. Single Inheritance
   User → Student

   A Student inherits common user functionality such as:
   - name
   - email
   - login()
   - display_info()

2. Hierarchical Inheritance
   User → Student
   User → Instructor

   Multiple child classes inherit from the same parent class.

3. Multilevel Inheritance
   User → Student → GraduateStudent

   GraduateStudent inherits from Student, which in turn
   inherits from User.

Concepts Practiced:
- Inheritance
- Parent (Base) Class
- Child (Derived) Class
- Constructor Inheritance
- super()
- Method Reuse
- Instance Variables
- Method Lookup
- Single Inheritance
- Hierarchical Inheritance
- Multilevel Inheritance

Classes Implemented:

User:
    - Stores common user information
    - Provides login() and display_info()

Student:
    - Inherits from User
    - Maintains enrolled courses
    - Provides enroll_course()

Instructor:
    - Inherits from User
    - Maintains created courses
    - Provides create_course()

GraduateStudent:
    - Inherits from Student
    - Maintains a research topic
    - Provides publish_research()

Key Learning Outcomes:

1. Child classes automatically inherit attributes and methods
   from their parent classes.

2. A child class can add its own attributes and methods while
   still reusing parent functionality.

3. The super().__init__() method allows a child class to
   initialize attributes defined in its parent class.

4. Inheritance is one-directional:
       Parent → Child
   and not:
       Child → Parent

5. Python searches for methods in the following order:
       Current Class
            ↓
       Parent Class
            ↓
       Grandparent Class

Example:
GraduateStudent can use:
    - login()         (from User)
    - display_info()  (from User)
    - enroll_course() (from Student)
    - publish_research() (its own method)

This demonstrates how inheritance promotes code reusability,
reduces duplication, and helps model real-world relationships
between classes.
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} logged in successfully")
        
    def display_info(self):
        print("Details:")
        print("Name:",self.name)
        print("Email:",self.email)
        
class Student(User):
    
    def __init__(self, name, email,):
        super().__init__(name, email)
        self.course = []
    
    
    def enroll_course(self, course):
        self.course.append(course)
        print("The courses are:",self.course) 
        
class Instructor(User):
    
    def __init__(self, name, email):
        super().__init__(name, email)
        self.created_courses = []
        
    def created_course(self, course_name):
        self.created_courses.append(course_name)
        print(f"{self.name} created {self.created_courses} course successfully")
        
class GraduateStudent(Student):
    def __init__(self, name, email, research_topic):
        super().__init__(name, email)
        self.research_topic = research_topic 
        
    def publish_research(self):
        print(f"Research published on {self.research_topic} by {self.name} successfully")
        
s1 = Student("John", "john@yahoo.com")
s1.login()
s1.display_info()
s1.enroll_course("SQL")

i1 = Instructor("Maria","maria@gmail.com")
i1.login()
i1.display_info()
i1.created_course("LLMs and Fine Tuning")

g1 = GraduateStudent("Billie","billie@yahoo.com", "Ingestion pipeline in RAG")
g1.login()
g1.display_info()
g1.enroll_course("RAG")
g1.publish_research()
