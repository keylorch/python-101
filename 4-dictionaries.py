# Dictionaries
# Basic information and operations on Dictionaries in python

# Dictionaries store key value pairs
# Dictionaries are mutable

# How to create a list
print("-----------------BASICS----------------")

# Currencies dictionary
dic = {
	"CRC": "colon", 
	"USD": "us dolar"
}
print("dic: ", dic)

print("dic[\"CRC\"]: ", dic["CRC"])

# To update values:
dic["CRC"] = "costa rican colon"
print("dic: ", dic)

# Delete items
del dic["USD"]
print("dic: ", dic)

# Add new items 
dic["EUR"] = "euro"
print("dic: ", dic)

# Looping
for key in dic:
	print("Key: ", key)

print("CRC in dic: ", "CRC" in dic)
print("len(dic): ", len(dic))

# Note: dic["not-a-key"] throws an exception
#		but dic.get("not-a-key") returns None
print("dic.get(USD): ", dic.get("USD"))