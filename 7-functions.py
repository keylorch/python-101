# Function
# Syntaxis and info on python's functions

# Function with a return value. All the statements of the function
# should be 
def myFunction(number1, number2):
	result = number1 ** number2
	return result

print("myFunction(2, 3): ", myFunction(2, 3))

# Parameters can be named: 
print("myFunction(number2=3, number1=2): ", myFunction(number2=2, number1=3))

# Function without a return statement return None
def myNoneFunction():
	i = 10

print("myNoneFunction(): ", myNoneFunction())

# Global variables 

myVar = 50	

def func1():
	myVar = 100	# As the assignment is done, a new local variable is delcared 
	print("func1.myVar: ", myVar)

func1()
print("myVar: ", myVar)

# To bind local variables to global variables and be able to change them: 
def func2():
	global myVar
	myVar += 100
	print("func2.myVar: ", myVar)

func2()
print("myVar: ", myVar)

# Default Values
def func3(param = 100):
	print("func3.param: ", param)

func3()

# Return multiple values as tuples:
def func4(a, b, c):
	return a * 2, b * 2, c * 2

print("func4(2,3,4): ", func4(2,3,4))
