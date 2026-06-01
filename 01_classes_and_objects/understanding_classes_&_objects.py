class Student:
    def __init__(self, name, email):
        print("I will get called automatically when you create an object")
        print("Student created")
        self.name =  name #object attribute
        self.email = email
        self.course_count = 0
        self.courses = []
        
    def display_info(self):
        print("The name of the student is: ", self.name)
        print("The email of the student is: ", self.email)
        
    def greet(self):
        print("Hi my name is:",self.name)
        
    def update_email(self,new_email):
        self.email = new_email
        
    def enroll_course(self):
        self.course_count += 1
        
    def login(self):
        print(self.name,"logged in successfully")
        
    def change_name(self, new_name):
        self.name = new_name
        
    def test(self):
        self.age = 22
        
    def add_course(self, course_name):
        self.courses.append(course_name)
        
    def introduce(self):
        print("Hi!")
        print("My name is:",self.name)
        print("My email is:",self.email)
        print("I am enrolled in:",self.course_count,"course(s)")
        print("The courses are: ",self.courses)
        
        
s1 = Student("john", "abc1@gmail.com")
s2 = Student("maria", "maria12@gmail.com")
#print(s1.name)
s1.display_info()
#s2.display_info()
s1.greet()
s1.update_email("abc@gmail.com")

s1.login()
s1.change_name("Anu")

s1.display_info()

s1.test()
print(s1.age)

s1.add_course("Python")
s1.enroll_course()
s1.add_course("SQL")
s1.enroll_course()
s1.introduce()
