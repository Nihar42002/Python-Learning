#String Printing:-
print("String Printing:-\n")
str1= "Nihar Parwani"
print(str1)

#How to excess a particular of a string:-
print("\nHow to excess a particular of a string:-\n")
str2 =  "Nihar Parwani"
ch = str2[0]
ch1 = str2[7]
print("Particular letter: ",ch,"\nParticular letter: ",ch1)

#How to find the lenght of the String:-
print("\nHow to find the lenght of the String:- \n")
str3 = "Nihar Parwani"
len1 = len(str3)
print("Lenght: ",len1)

#How to do slicing in a positive direction:-
print("\n How to do sclicing in a positive direction:- \n")
str4 = "Nihar Parwani"
print("slicing: ",str4[2:8]) #har Pa this will be the output
print("slicing: ",str4[2:len(str4)]) #har Parwani this will be the output
print("slicing: ",str4[2:])#har Parwani this will be the output bcoz it will take default to end of the string
print("slicing: ",str4[:8])#Nihar Pa this will be the output

#How to do slicing in a Negative direction:-
print("\n How to do sclicing in a positive direction:- \n")
str4 = "Nihar Parwani"
print("slicing: ",str4[-5:-1]) #rwan this will be the output
print("slicing: ",str4[-7:])#parwani  this will be the output bcoz it will take default to end of the string
