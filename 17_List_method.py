#LIST METHODS:-

#this append method is use to add a element in the series withot disturbing the series
marks = [90,89,88,87,86]
marks.append(45)
print("After add the element: ",marks,"\n")

#This method is use to sort the elements in ascending order:-
marks = [90,89,88,87,86]
marks.sort()
print("After sorting: ",marks,"\n")

#This method is use to sort the elements in descending order:-
marks = [86, 87, 88, 89, 90]
marks.sort(reverse=True)
print("After Sorting: ",marks,"\n")

#It will reverse the whole list and there elements:-
list = ['a','b','c','d','e','f']
list.reverse()
print("After reverse the elements: ",list,"\n")

#It will insert the elements at a particular index:-
#method:- list.insert(index,elements)
list = ['a','b','c','d','e','f']
list.insert(2,'g')
print("After Inserting a Elements at a particular index: ",list,"\n")

#It removes the first occurence of elements:-
marks = [86, 87, 88, 90, 89, 90]
marks.remove(90)
print("After remove: ",marks,"\n")

#This method removes elements at particular index:-
marks = [86, 87, 88, 90, 89, 90]
marks.pop(2)
print("Removes the particular index",marks,"\n")
