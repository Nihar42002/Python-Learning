var = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

i = 0
while i < len(var):
    print(var[i])
    i += 1
# The above code will print the elements of the list 'var' one by one.
# The while loop continues until 'i' is less than the length of the list.
# The 'i' variable is incremented by 1 in each iteration to move to the next element.

import random 

Sets = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

Sets = list(Sets)  # Convert the set to a list for indexing

Var = random.choice(list(Sets))


# Initialize the index
i = 0

# Iterate through the list
while i < len(Sets):
    if Sets[i] == Var:
        print("Random Number:", Sets[i])  # Print if the number matches
   
    i += 1

# The above code will print the random number chosen from the set 'Sets'.
# The while loop continues until 'i' is less than the length of the list.
# The 'i' variable is incremented by 1 in each iteration to move to the next element.
# The 'if' statement checks if the current element is equal to the random number.


#USing a for loop.

print("\n \n")

list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for i in list:
    num = random.choice(list)
# Initialize the index
    if(num%2 == 0):
     print("Even Number", num)
     break
    else:
        print("Odd Number", num)

# The above code will print the random number chosen from the list 'list'.
# The for loop iterates through each element in the list.

print("\n \n")

# Using a for loop with range

for i in range(10): #it shows the stop value 
    print(i)  # Print the current value of 'i'  
print("End of the loop")  # Print a message indicating the end of the loop

print("\n \n")

for i in range(2,10): #it shows the start and stop value 
    print(i)  # Print the current value of 'i'
print("End of the loop")  # Print a message indicating the end of the loop
print("\n \n")

for i in range(2, 10, 2): #it shows the start, stop and step value
    print(i)  # Print the current value of 'i'
print("End of the loop")  # Print a message indicating the end of the loop
print("\n \n")

