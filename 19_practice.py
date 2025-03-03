#WAP to ask the user to enter names of their 3 favourite movies and  store them in a list:-
list = []
mname = list.append(input("Enter The Movie Name:"))
mname1 = list.append(input("Enter The Movie Name:"))
mname2 = list.append(input("Enter The Movie Name:"))

print(list)

#WAP to check if a list contain the a palindrome elements Example:- [1,2,3,2,1]
list = []
N1 = list.append(input("ENTER THE NUMBER:"))
N1 = list.append(input("ENTER THE NUMBER:"))
N1 = list.append(input("ENTER THE NUMBER:"))
N1 = list.append(input("ENTER THE NUMBER:"))
N1 = list.append(input("ENTER THE NUMBER:"))
N1 = list.append(input("ENTER THE NUMBER:"))
N1 = list.append(input("ENTER THE NUMBER:"))
list2 = list.copy()
list2.reverse()

if(list2 == list):
    print("The list contain palindrome of elements")
else:
    print("The list does not contain palindrome of elements")

#WAP to count the number of student with a 'A' grade in th following tuple.
tup = ('A','B','C','D','A','A','C')
print("Total Count: ",tup.count("A"),"\n")

#WAP store the above tup elements in a list and sort it from A to D:-
list7 = ['A','B','C','D','A','A','C']
list7.sort()
print("After Sorting: ",list7,"\n")