def sum_of_two_numbers(a, b):
    return a + b

# Example usage:
result = sum_of_two_numbers(5, 7)
print("Sum:", result)

#OR 
print("\n \n")

def sum(a,b):
    s = a + b
    print("Sum:", s)
    return s

sum(34,40)

print("\n \n")

# my a function to print the lenght of the list

list = [1,2,3,4,5,6,7,8,9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
heros = ["Ironman", "Thor", "Hulk", "Captain America", "Black Widow"]
# This function takes a list as an argument and prints its length

def length(list):
             print("lenght: ",len(list))

length(list)
length(heros)
print("\n \n")

# WAF a program to print the list elements in a single line
def elements(list):
       for i in list:
              print(i, end = " ")
elements(list)
print("\n")
elements(heros)
print("\n \n")

# WAF to find the factorial of Number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
       return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(int(input("Enter a number: "))))
print("\n \n")

# WAF to convert the USD to INR
def Rupees(dollar):
      return dollar*85
print("USD to INR: ",Rupees(int(input("Enter the dollar: "))),"rupees")
print("\n \n")