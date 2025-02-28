#String function:-

str1 = "I am a coder"
#It is used when the string ends with the words or letter written in the bracket
print("\nAnswer: ",str1.endswith("er"))#True

str2 = "i am a coder"
print("\nAnswer: ",str2.capitalize()) #capitalize first char


str3 = "I am a coder"
#str.replace(old,new)
print("\nAnswer: ",str3.replace("I","He"))#Replace all occurrences of old with new

str4 = "Learn the python language from the best channel in youtube"
print("\nAnswer: ",str4.find("the")) #return the 1st index of the 1st occurrences in the string

str5 = "Learn the python language from the best channel in youtube"
print("\nAnswer: ",str5.count("the"))#count the occurence of substring in the string

