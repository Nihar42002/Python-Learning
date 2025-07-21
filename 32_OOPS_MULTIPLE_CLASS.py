#WAP to make multiple parents and child classes with multiple inheritance.
class Parent1:
    def __init__(self, name):
        self.name = name
        print(f"Parent1 Name: {self.name}")

    def greet(self):
        print(f"Hello from Parent1, {self.name}!")
class Parent2:
    def __init__(self, age):
        self.age = age
        print(f"Parent2 Age: {self.age}")

    def info(self):
        print(f"Parent2 is {self.age} years old.")
class Child(Parent1, Parent2):
    def __init__(self, name, age):
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)
        print(f"Child Name: {self.name}, Age: {self.age}")

    def child_info(self):
        print(f"Child Info: Name - {self.name}, Age - {self.age}")
# Create an instance of the Child class
c = Child("Nihar", 20)
c.greet()  # Call method from Parent1
c.info()    # Call method from Parent2  
c.child_info()  # Call method from Child class
super(Child, c).greet()  # Using super to call Parent1's method


