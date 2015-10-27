# Control / Loop Statements
# Syntaxis and info on python's control and loop statements

myVar = 1;

# if
if myVar > 0:
	print("if true")

# if else
if myVar <0:
	print("if true")
else:
	print("else true")


# elif 
if myVar > 5:
	print("Bigger than 4")
elif myVar < 0:
	print("Less than 0")
elif myVar == 1:
	print("Equals to -1")
else:
	print("None")

# Boolean operators
print("True and True: ", True and True)
print("True or False: ", True or False)
print("not True: ", not True)

#for
for x in range(0,10):
	print(x, end="-")

print("")
#while 
count = 0
while count < 10:
	print(count, end="-")
	count+= 1



