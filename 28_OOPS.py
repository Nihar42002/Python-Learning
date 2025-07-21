# Make constrcutor for student class
class Student:
    college = "GEC Valsad"  # Class variable
    # Constructor to initialize instance variables  

    def __init__(self, name, roll_no, city):
        self.name = name
        self.roll_no = roll_no
        self.city = city
        print("Constructor called")

# Create an instance of the Student class
s1 = Student("Nihar", 89, "Vadodara")
print(s1.name, s1.roll_no, s1.city)
   
s2 = Student("Tarun", 90, "Vadodara")
print(s2.name, s2.roll_no, s2.city)
print(s2.college)  # Accessing class variable using instance
print(Student.college)  # Accessing class variable using class name



