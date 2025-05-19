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