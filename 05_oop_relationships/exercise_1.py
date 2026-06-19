# 1. Association: One object uses another object. The objects are independent
class Laptop:
    def __init__(self, brand):
        self.brand = brand
        
class Student:
    
    def __init__(self, name):
        self.name = name
        
    def use_laptop(self, laptop):
        print(f"{self.name} is using {laptop.brand}")
        
l1 = Laptop("DELL")
l2 = Laptop("Mac")
s1 = Student("John")
s1.use_laptop(l2)

# If the laptop Mac is deleted: 
del l2
#s1.use_laptop(l2) will give error as l2 not defined, however student still exists

# If student is deleted:
#del s1 : The laptop still exists

# 2. Aggregation:
class Professor:
    def __init__(self, name):
        self.name = name
        
class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []
    
    def add_professors(self, professor):
        self.professors.append(professor)
        
p1 = Professor("Smith")
p2 = Professor("John")

d = Department("Data Science")
d.add_professors(p1)
d.add_professors(p2)

# If department is deleted:
# del d
# Professors still exist because professors were created outside and merely added. 
# This is aggregation

# 3. Composition: One object owns other object completely
# If the parent dies then child dies too

class Room:
    def __init__(self, number):
        self.room_no = number
        
class House:
    def __init__(self):
        self.room1 = Room(1001)
        self.room2 = Room(1002)
        
h1 = House()
# Rooms created inside the house. They are owned by the house
# If House is gone (del h1), the rooms are gone too. This is called Composition




