# Uses of different types of file handling in Python
# 1. Text File Handling 
#example:-
f = open("example.txt", "w")  # Open a file in write mode
f.write("Hello, World!")  # Write to the file
f.close()  # Close the file
#
# 2. Binary File Handling
#example:-
f = open("example.bin", "wb")  # Open a file in binary write mode
f.write(b"Hello, World!")  # Write binary data to the file
f.close()  # Close the file
#
#3. read and write file handling
#example:-
f = open("example.txt", "r")  # Open a file in read mode
data = f.read()  # Read the entire file
print(data)  # Print the data
f.close()  # Close the file
#
# 4. Append File Handling
#example:-
f = open("example.txt", "a")  # Open a file in append mode
f.write("\nAppending some text.")  # Append text to the file
f.close()  # Close the file
#
# 5. File Existence Check
#example:-
import os
if os.path.exists("example.txt"):  # Check if the file exists
    print("File exists.")   
else:
    print("File does not exist.")
#
# 6. File Size Check
#example:-
import os
file_size = os.path.getsize("example.txt")  # Get the size of the file
print("File size:", file_size, "bytes")  # Print the file size
#
# 7. File Rename
#example:-
import os
os.rename("example.txt", "renamed_example.txt")  # Rename the file
#
# 8. File Delete
#example:-
import os
input("Press and Enter Any Key to delete the file: ")
os.remove("renamed_example.txt")  # Delete the file
#
# 9. File Copy
#example:-
import shutil
f = open("example1.txt", "w")
f.write("This is a test file.")  # Create a test file
f.close()  # Close the file
shutil.copy("example1.txt", "copy_of_example.txt")  # Copy the file
#
# 10. x File Handling
#example:-
f = open("example.txt", "x")  # Open a file in exclusive creation mode
f.write("This will raise an error if the file already exists.")  # Write to the file  
f.close()  # Close the file
#
# w+ File Handling
#example:-
f = open("example.txt", "w+")  # Open a file in write and read mode
f.write("Hello, World!")  # Write to the file
f.seek(0)  # Move the cursor to the beginning of the file
data = f.read()  # Read the entire file
print(data)  # Print the data
f.close()  # Close the file
#
# a+ File Handling
#example:-
f = open("example.txt", "a+")  # Open a file in append and read mode
f.write("\nAppending some text.")  # Append text to the file
f.seek(0)  # Move the cursor to the beginning of the file
data = f.read()  # Read the entire file
print(data)  # Print the data
f.close()  # Close the file
#
# 11. r+ File Handling
#example:-
f = open("example.txt", "r+")  # Open a file in read and write mode
f.write("Hello, World!")  # Write to the file
f.seek(0)  # Move the cursor to the beginning of the file
data = f.read()  # Read the entire file
print(data)  # Print the data
f.close()  # Close the file
#


