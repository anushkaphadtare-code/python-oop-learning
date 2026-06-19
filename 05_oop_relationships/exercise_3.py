# Aggregation Example:
class Employee:
    def __init(self, name):
        self.name = name #name of employee
        
class Company:
    
    def __init__(self, name):
        self.name = name  #name of company
        self.employees = []
        
    def add_employees(self,emp):
        self.employees.append(emp)
        
    def display_employees(self):
        print(self.employees)
        
e1 = Employee("John")
c1 = Company("Google")
c1.add_employees(e1)
c1.display_employees()
           

        
