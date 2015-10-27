# Lists
# Basic information and operations on lists in python

# Lists are MUTABLE 

# How to create a list
print("-----------------BASICS----------------")
myList = [1, 2, 3, 4]
print("myList: ", myList)

# They can have different types of objects
mySecondList = [1, "hola"]
print("myList: ", mySecondList)

# Accessing elements in a list
print("myList[0]: ", myList[0])
print("myList[1]: ", myList[1])

# List Operators
print("-----------------OPERATORS----------------")
print("1 in myList: ", 1 in myList)
print("myList + mySecondList: ", myList + mySecondList) # Note: concatenation doesn't affect the original lists
print("myList * 3: ", myList * 3)
print("myList[1:3]: ", myList[1:3])
print("len(myList): ", len(myList))
print("min(myList): ", min(myList))
print("max(myList): ", max(myList))
print("sum(myList) ", sum(myList))

# Looping
for item in myList:
	print(item)


# Methods
print("-----------------METHODS----------------")
myList.append(5)
print("myList: ", myList)

print("myList.count(1): ", myList.count(1))

myList.extend([6,7])
print("myList: ", myList)

print("myList.index(7): ", myList.index(7))

print("myList.insert(0, 0): ", myList.insert(0, 0))
print("myList: ", myList)

print("myList.pop(): ", myList.pop()) 	# An index can be given
print("myList: ", myList)

print("myList.reverse(): ", myList.reverse())
print("myList: ", myList)

print("myList.sort(): ", myList.sort())
print("myList: ", myList)


print("-----------------LIST COMPREHENSION----------------")
print("[x for x in range(10)]: ", [x for x in range(10)])
print("[x * 2 for x in range(10)]: ", [x * 2 for x in range(10)])
print("[x for x in range(10) if x % 2 == 1]: ", [x for x in range(10) if x % 2 == 1])






