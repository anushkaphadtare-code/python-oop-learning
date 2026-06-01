"""
OOP Exercise: Student Management System using Instance Variables and Static Methods

Objective:
Build a Student class to understand the difference between instance variables,
instance methods, and static methods in Python OOP.

Requirements:
1. Store student-specific information using instance variables:
   - name
   - email
   - age
   - course_count

2. Implement instance methods to:
   - Display student information
   - Enroll a student in courses
   - Update the student's email address

3. Implement static methods to:
   - Validate student age
   - Validate email format
   - Generate a student ID

Learning Outcome:
Understand when data should belong to an object (instance variables)
and when functionality should be independent of objects (static methods).
Learn how to organize behavior inside a class while maintaining
a clear separation between object-specific operations and utility functions.
"""

import random
class Student:
    def __init__(self, name, email, age):
        
        self.name = name
        self.email = email
        self.age = age
        self.course_count = 0
        
    def display_info(self):
        print("Name:",self.name)
        print("Email:",self.email)
        print("Age:", self.age)
        print("Courses Involved:", self.course_count)
        
    def enroll_courses(self):
        self.course_count += 1
        
    def change_email(self, new_email):
        self.email = new_email
        
    @staticmethod
    def is_valid_age(age):
        return age >= 18 and age <= 100
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email
    
    @staticmethod
    def generate_student_id(name):
        student_id = name[:3].upper() + str(random.randint(1,100000))
        return student_id
    
s1 = Student("John", "john@gmail.com", 23)
s2 = Student("Maria", "maria@gmail.com", 24)

# Test Instance methods
s1.display_info()   
s1.enroll_courses()
s1.enroll_courses() 
s1.display_info()   

# Test static methods:
print(Student.is_valid_age(23))  
print(Student.is_valid_age(150))

print(Student.is_valid_email("abc@gmail.com")) 
print(Student.is_valid_email("abcgmail.com"))   
        
print(Student.generate_student_id("John"))        
        
