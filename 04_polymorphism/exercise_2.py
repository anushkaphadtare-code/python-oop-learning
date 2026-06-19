from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    
    def start_engine(self):
        print("car started")
        
class Bike(Vehicle):
    
    def start_engine(self):
        print("Bike started")
        
class Truck(Vehicle):
    
    def start_engine(self):
        print("Truck started")
        
vehicles =[
    Car(),
    Bike(),
    Truck()
]
for vehicle in vehicles:
    vehicle.start_engine()
    
    
"""
ABSTRACTION NOTES

1. Abstraction hides implementation details and only exposes
   the required behavior.

2. ABC stands for Abstract Base Class.

3. @abstractmethod forces all child classes to implement
   the specified method.

4. Abstract classes cannot be instantiated directly.

5. Vehicle acts as a blueprint that defines what every vehicle
   must be able to do (start_engine).

6. Car, Bike and Truck provide their own implementations of
   start_engine().

7. The loop demonstrates polymorphism:
       vehicle.start_engine()

   Python automatically calls the appropriate implementation
   based on the actual object type.

CONCEPTS USED:
✔ Inheritance
✔ Method Overriding
✔ Polymorphism
✔ Abstraction
"""
