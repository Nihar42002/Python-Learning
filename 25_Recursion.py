#WAP with use of recursion calaulate the sum of n natural numbers.

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print("Sum of first 5 natural numbers is:", sum(int(input("Enter a number: "))))
print("\n \n")

# WAP to print all print all the elements of list using recursion
lst = [1,2,3,4,5,6,7,8,9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def print_list_elements(lst, n=0):
    # Base case: if n is equal to or greater than the length of the list, stop recursion
    if n >= len(lst):
        return
    # Print the current element
    print(lst[n], end=" ")
    # Recursive call to print the next element
    print_list_elements(lst, n+1)

print_list_elements(lst)
print("\n \n")