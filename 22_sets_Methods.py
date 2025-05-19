#This is Sets and used to collect information and we can not write the same value if we write it will ignore.
#And it will not print in a order .
Sets = { 1, 2, 2, 2, 4, 3, "Nihar", "Parwani"}
print(Sets)
print(type(Sets))
#To make Empty set.
Language = set()
print(Language)


#This method helps to add elements in the set.
Sets.add(9)
Sets.add(8)
#This method helps to remove the elements in the sets.
Sets.remove(4)
print(Sets)

#this method is use to clear the Sets
Sets.clear()
print(Sets)

Sets = { 1, 2, 2, 2, 4, 3, "Nihar", "Parwani"}

#this methods helps to pop a random elements from the sets.
print(Sets.pop())

#This method help to give a final union
col1 = {1, 2, 3}
col2 = {2, 3, 4}
print("Final Sets: ",col1.union(col2))

#This method helps to give the intersection
print("Second Final Sets: ",col1.intersection(col2))
