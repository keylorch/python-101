# 1 - Hola Mundo 
# Just some phyton basics: syntax, variables, types, functions, etc.

# First thing first, hello world example. Notice there are no ; at the end
# of lines
print("hola mundo")

# - Interpreted language
# - Dynamically typed
# - Strongly typed
# - Everything in phyton is an object, even primitives
myVar1 = 100 		# myVar1 will be int. 
myVar2 = "hola"		# myVar2 will be String 

myVar1 = "myVar1"	# myVar1 will now be string
print(myVar1)
print(myVar2)

# Multiple assignments at once 
x = y = z = 200
print(x, y, z)

x, y, z = 1, 2, 3
print(x, y, z)

# boolean 
myBoolean = True 	# True or False. 0, [], {}, () are also false
print(myBoolean)



# modules are imported via import keyword
import math
print("math.pi: ", math.pi)

# to check the type of a variable 
print("type(myVar1): ", type(myVar1))
print ("type(math.pi):", type(math.pi))


# Math operators
print("2 ** 3: ", 2 ** 3)	# Exp
print("4 // 3: ", 4 // 3)	# int division

# Object references: id() gives the memory address of the object
print("-id(x)-", id(x))
print("-id(myVar1)- ", id(myVar1))





