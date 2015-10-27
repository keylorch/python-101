# 2 - Strings
# Some basic operations on strings

# Strings
# 	- They are inmutable (can't be changed)
myString = "hola python"

# Some opertions on strings 
print("-----------------BASICS----------------")
print("-Char index: ", myString[0])
print("-Repeat String: ", myString * 2)
print("myString[0:3]: ", myString[0:3])
print("myString[2:]: ", myString[2:])
print("len(myString): ", len(myString))
print("hola in myString: ", "hola" in myString)
print("hola not in myString: ", "hola" not in myString)

# Strings are iterable
print("itration!")
for character in myString:
	print(character) 
	# print(character, end="") # Alt, print nothing at the end instead of new lines

# Util Methods
# Other: startswith, count(substring), find, capitalize, lower, upper
# title, replace
print("-----------------METHODS----------------")
print("myString.isalnum(): ", myString.isalnum())
print("myString.isalpha(): ", myString.isalpha())
print("myString.islower(): ", myString.islower())
print("myString.endswith(\"mundo\"): ", myString.endswith("mundo"))