
'''Magic methods (dunders)
    They are special methods in Pythin that are defined inside class
    They begin and end with double underscores
    Automatically called when certain operations happen'''

class ComplexNumber:
    def __init__(self, real = 0.0, imaginary = 0.0):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):   #dunder method
        if self.real == 0:
            return f"{self.imaginary}i"
        if self.imaginary < 0:
            s = f"({self.real}{self.imaginary}i)"
        else:
            s = f"({self.real} + {self.imaginary}i)"
        return s
        
    def __add__(self,other):
        
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        
        s2 = ComplexNumber(result_real, result_imaginary)
        return s2  
    
    def __sub__(self,other):
        sub_real = self.real - other.real
        sub_imaginary = self.imaginary - other.imaginary
        
        s3 = ComplexNumber(sub_real, sub_imaginary)
        return s3
        
    def __mul__(self, other):
         pro_real = (self.real * other.real) - (self.imaginary * other.imaginary)
         pro_imaginary = (self.real * other.imaginary) + (self.imaginary * other.real) 
         
         #s3 = f"({pro_real} + {pro_imaginary}i)" =>
         # We could return a formatted string such as:
         # f"({pro_real} + {pro_imaginary}i)"
         # for display purposes, but that would return a string object.
         # Returning ComplexNumber(...) is better because the result remains
         # a ComplexNumber object and can participate in further operations
         # like addition, subtraction, multiplication, etc.
         s3 = ComplexNumber(pro_real, pro_imaginary)
         return s3  
     
    def __truediv__(self, other):
        
        denominator = (pow(other.real, 2) +pow(other.imaginary,2))
        if denominator == 0:
            raise ZeroDivisionError(
                'Cannot divide by zero complex number'
            )
        else:    
            quo_real = ((self.real * other.real) + (self.imaginary * other.imaginary)) / denominator
            quo_imag = ((self.imaginary * other.real) - (self.real * other.imaginary)) / denominator
            
            s4 = ComplexNumber(quo_real, quo_imag)
            return s4
        
    def __eq__(self, other):
        return (self.real == other.real and self.imaginary == other.imaginary)
            
               
cn1 = ComplexNumber(3,5)  
cn2 = ComplexNumber(4,3)

print(cn1)
print(cn2)

print(cn1 + cn2)
print(cn1 - cn2)
print(cn1 * cn2)
print(cn1 / cn2)
print(cn1 == cn2)

