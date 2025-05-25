# Make constrcutor for student class
class Student:
    def __init__(self, name, roll_no, city):
        self.name = name
        self.roll_no = roll_no
        self.city = city
        print("Constructor called")

# Create an instance of the Student class
i = 1
for i in range(2):
    if(i == 1):
        si = Student("Nihar", 89, "Vadodara")
        print(si.name, si.roll_no, si.city)
    else:
        si = Student("Tarun", 90, "Vadodara")
        print(si.name, si.roll_no, si.city)