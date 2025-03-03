#In this program we will do slicing in list and with their element:-
marks=[90,89,88,87,86,85]

#We will call number 1 to 4 between elements:-
print("\n Slicing: ",marks[1:4])
#We will call number 0 to 4 between elements:-
print("\n Slicing: ",marks[0:4])
print("\nAbove code is also same like this Slicing: ",marks[:4])# It will take it zero by default
#We will call number 2 to end between elements:-
print("\n Slicing: ",marks[2:])
#OR
print("\nAbove code is also same like this Slicing: ",marks[2:len(marks)])
#we will call number in reverse from -4 to -1 :-
print("\n Slicing: ",marks[-4:-1])