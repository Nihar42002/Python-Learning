#WAP a program in which we will print the grade according to the marks or student:-
a = float(input("Enter The Marks Of English:"))
b = float(input("Enter The Marks Of Maths:"))
c = float(input("Enter The Marks Of Science:"))

marks = (a+b+c)/3

if(marks>=90):
    print("Grade A+","\nPercentage: ",marks)
elif(90>marks>=80):
     print("Grade A","\nPercentage: ",marks) # it is use as else and it can be use number of times
elif(80>marks>=70):
      print("Grade B+","\nPercentage: ",marks)
elif(70>marks>=60):
      print("Grade B","\nPercentage: ",marks)
elif(60>marks>=50):
      print("Grade C+","\nPercentage: ",marks)
elif(50>marks>=40):
      print("Grade C","\nPercentage: ",marks)
else:
       print("Grade D","\nPercentage: ",marks)