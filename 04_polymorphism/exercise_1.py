class Payment:
    def process_payment(self):
        print("Processing Payment....")
        
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment via Credit Card")
        
class UPIPayment(Payment):
    def process_payment(self):
        print("Payment via UPI")
        
class PayPalPayment(Payment):
    def process_payment(self):
        print("Payment via PayPal")
        
payments =[
    CreditCardPayment(),
    UPIPayment(),
    PayPalPayment()
]

for payment in payments:
    payment.process_payment()
    
c = CreditCardPayment()
print(isinstance(c, Payment)) #isinstance() checks inheritance
print(isinstance(c, CreditCardPayment))

p = PayPalPayment()
print(type(p)) # returns the class of object
print(type(p).__name__) #returns only the class name as a string

# isinstance() checks ineritance whereas type checks exact class

"""
POLYMORPHISM NOTES

1. Polymorphism means "one interface, many forms".
   The same method name can have different implementations in different classes.

2. In this example, all payment classes have a method called process_payment(),
   but each class performs the action differently.

3. During the loop:
       for payment in payments:
           payment.process_payment()

   Python automatically calls the correct version of process_payment()
   based on the actual object type at runtime.

4. This is called Runtime Polymorphism and is achieved through
   method overriding.

5. isinstance(object, ClassName)
   - Checks whether an object belongs to a class or any of its parent classes.
   - Supports inheritance.

   Example:
       isinstance(c, Payment)            -> True
       isinstance(c, CreditCardPayment)  -> True

6. type(object)
   - Returns the exact class of the object.
   - Does not consider inheritance.

   Example:
       type(p) == Payment        -> False
       type(p) == PayPalPayment  -> True

7. Key Difference:
   - isinstance() checks inheritance relationships.
   - type() checks the exact class only.

OUTPUT:
    Payment via Credit Card
    Payment via UPI
    Payment via PayPal

    True
    True

    <class '__main__.PayPalPayment'>
    PayPalPayment
"""
