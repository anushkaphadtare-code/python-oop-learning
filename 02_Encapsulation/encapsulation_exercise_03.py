"""
OOP Exercise: Course Enrollment System using Private Methods

Objective:
Build a Course class that allows students to enroll in a course while
enforcing eligibility rules through a private validation method.

Requirements:
1. Store course-related information:
   - course_name
   - enrolled_students
   - minimum_age

2. Allow students to enroll in a course through a public method.

3. Validate student eligibility before enrollment:
   - Students must satisfy the minimum age requirement.
   - Validation logic should be hidden from external users.

4. Maintain a list of successfully enrolled students.

5. Display course information and enrolled students.

Concepts Practiced:
- Classes and Objects
- Constructors (__init__)
- Instance Variables
- Public Methods
- Private Methods (__method_name)
- Encapsulation
- Data Validation
- List Operations
- Object State Management
- Name Mangling in Python

Private Method Used:
    __is_eligible(age)

Purpose:
    Acts as an internal helper method responsible for checking
    whether a student satisfies the minimum age requirement.

Why Private?
    Users of the class should interact with the public method
    enroll_student() rather than directly calling the validation logic.
    This hides implementation details and improves encapsulation.

Learning Outcome:
Understand how private methods can be used to hide internal logic
while exposing only the necessary functionality through public methods.
Learn the difference between public and private behavior inside a class
and observe how Python implements privacy using name mangling.
"""
class Course:
    
    def __init__(self, course_name):
        self.course_name = course_name
        self.enrolled_students = []
        self.minimum_age = 18
        
        
    def __is_eligible(self, age):
        if age >= self.minimum_age:
            return True
        else:
            return False
        
    def enroll_student(self, student_name, age):
        
        if self.__is_eligible(age):
            self.enrolled_students.append(student_name)
            print(f"{student_name} enrolled successfully")
            
        else:
            print("Student does not meet age requirement")
            
    def display_students(self):
        print("Course:",self.course_name)
        print("Students:",self.enrolled_students)
        
c = Course("Python")
c.enroll_student("John",20)
c.display_students()

c.enroll_student("Maria",56)
c.display_students()

c.enroll_student("Michael", 12)
c.display_students()  

#c.__is_eligible(20)        Attribute Error

c1 = Course("SQL")
c1.enroll_student("Bill",28)
c1.enroll_student("Stephen",30)
c1.display_students() 
