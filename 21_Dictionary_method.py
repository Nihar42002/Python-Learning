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

#This methods return all the value in the form of tuples as a pair and we can use as a list also.
print(Student.items())
#OR
#we can also convert the above dictionary into list:
print(list(Student.items()))
Var = list(Student.items())
print(Var[0])
print(Var[1])

#This method help to ignore the value when we have ask to return wrong key
# And this method will Ignore that error and run the pending right code.
print(Student.get("Name"))
print(Student.get("City"))

#This method is use to update the new key aur to change the value of that key.
Language={
    "Hindi":"B2",
    "English":"B1",
    "Germany":"A1"
}
Student.update(Language)
print(Student)

