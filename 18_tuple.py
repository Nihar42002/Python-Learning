#TUPLES:-
# #Tuple is same as list it is immutable sequence of values
# Immutable sequence means we cannot add elements or cannot change the sequence of element
tup = (1,2,3,4,5,6,5,4,1,1)
print("Tuple: ",tup,"\nTuple: ",type(tup),"\n")

#Tuple method:-

#This method show the FIRST occurrence of particular element in tuple:-
tup = (1,2,3,4,5,6,5,4,1,1,98)
print("Showing the first occurrence: ",tup.index(98),"\n")

#This method count the toatl occurrence of particular elements:-
tup = (1,2,3,4,5,6,5,4,1,1,98)
print("Total occurrences: ",tup.count(1),"\n")

