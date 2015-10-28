# Tuples
# Basic information and operations on Tuples in python

# Tuples are INmutable

myTuple = (1,2,3,4)
print("myTuple: ", myTuple)

print("min(myTuple): ", min(myTuple))
print("max(myTuple): ", max(myTuple))
print("sum(myTuple): ", sum(myTuple))
print("len(myTuple): ", len(myTuple))
print("1 in myTuple: ", 1 in myTuple)
print("22 in myTuple: ", 22 in myTuple)

# You can also slice, and loop 
for item in myTuple[1:]:
	print(item)

