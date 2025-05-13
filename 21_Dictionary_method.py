#Dictionary Methods:-
Student = {
    "Name": "Nihar Parwani",
    "Marks": {
        "Maths": 89,
        "Chemistry": 90,
        "English": 78,
    }
}

# This methods to call the outer keys which are been used in the dictionary:
print(Student.keys())

# This methods helps to convert the dictionary into list and we can also find the lenght:
print(list(Student.keys()))
print(len(list(Student.keys())))

#This methods return all the values and all the inner keys of the dictionary:
print(Student.values())
#we can also convert the above dictionary into list:
print(list(Student.values()))
var = list(Student.values())
print(var[0])
print(var[1])
#OR:-
print(list(Student.values())[0])

#This methods 
