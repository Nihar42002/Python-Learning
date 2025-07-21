#create a students class that take name and marks of 3 subjects and calculate the total and average marks
class college:
    def __init__(self, name, marks1, marks2, marks3):
        print("SVIT COLLEGE OF ENGINEERING, VASAD")
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2    
        self.marks3 = marks3

    def total(self):
            return self.marks1 + self.marks2 + self.marks3
        
    def average(self):
            return self.total() / 3
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks in Subject 1: {self.marks1}")
        print(f"Marks in Subject 2: {self.marks2}")
        print(f"Marks in Subject 3: {self.marks3}")
        print(f"Total Marks: {self.total()}")
        print(f"Average Marks: {self.average()}")

s3 = college("Nihar", 85, 90, 95)
s3.display()
s4 = college("Tarun", 80, 85, 90)
s4.display()
