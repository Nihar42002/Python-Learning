#WAP take a input from user and show its is eligble for license and for voting using if ,elif, else.

age = int(input("Enter Your Age: "))

if(age>=18):
    print("You are eligble for license","\nYou are eligble for voting")
elif(age>=16):
    print("You are eligble for learning license")
else:
    print("You are NOT eligble for license","\nYou are NOT eligble for voting")
    