# Composition Example:
class Engine:
    
    def __init__(self, name):
        self.name = name
        
class Car:
    
    def __init__(self):
        self.engine1 = Engine("version 10.0.8")
        print("Car has engine", self.engine1.name)
        
c1 = Car()
