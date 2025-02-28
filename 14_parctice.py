#WAP a program to check whether the number enter by the user is ODD Or EVEN:-
print("\nWAP a program to check whether the number enter by the user is ODD Or EVEN:-")
a =  int(input("ENTER THE NUMBER:"))

if(a%2==0):
    print("EVEN")
elif(a%2!=0):
    print("ODD")
else:
    print("ENTER A VALID NUMBER")
    
print("---------------------------------\n")

#WAP to find the maximum number out of 3
print("\n WAP to find the maximum number out of 3:-")
a =  float(input("ENTER THE NUMBER:"))
b =  float(input("ENTER THE NUMBER:"))
c =  float(input("ENTER THE NUMBER:"))

if(a>b or b>a):
    if(a>c):
        print("A is maximum: ",a)
    elif(b>c):
        print("B is maximum: ",b)
    else:
        print("C is maximum: ",c)

else:
    print("ENTER THE PROPER NUMBER") 
     
print("---------------------------------\n")  

#WAP program if the number is multiple of 7 or NOT:-
print("\nWAP program if the number is multiple of 7 or NOT:- ")

a =  int(input("ENTER THE NUMBER:"))

if(a%7==0):
    print("IT IS A MULTIPLE OF 7:",a)
else:
    print("IT IS NOT AMULTIPLE OF 7",a)