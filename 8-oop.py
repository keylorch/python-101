# Object Oriented programming
# Syntaxis and info on python's object oriented programming features

# Classes 
class Phone: 

	#Class Constructor, called initializer 
	def __init__(self, model):		# All methods should have a first parameter self, refering to the object which invoques the method
		self.model = model					# Model is a public data field
		self.__pin = "1199" 				# pin in a private data field

	def showPhone(self):
		print("I am a: ", self.model)
		print("My Pin is: ", self.__pin)		# Note: self.pin would give an error. __ are needed

	def __add__(self, anotherPhone):			# Operator overloading for the + 
		return Phone("Mutant phone: " + self.model + "_" + anotherPhone.model)

# Creating an instance of an object 
android = Phone("Nexus5X")
android.showPhone()
print("android.model: ", android.model)
#print("android.__pin: ", android.__pin) 	#Error, pin is private

iphone = Phone("iPhone5")
mutantPhone = android + iphone 					# Sample example of operator overriding. 
												# Can also override: <, >=, [index], len, str
print("mutantPhone.model: ", mutantPhone.model)	# Check http://thepythonguru.com/python-operator-overloading/ for the keywords


# Inheritance Example

class SuperClass():
	def __init__(self, name):
		self.name = name

	def sayMyName(self):
		print("SuperClass.sayMyName: ", self.name)

# Sub Class: 
class SubClass(SuperClass):			# Python support multiple inherintance with: SubClass(SuperClass1, SuperClass2 )
	def __init__(self, name, color):
		super().__init__(name)
		self.color = color

	def whatIsMyColor(self):
		print("SubClass.whatIsMyColor: ", self.color)


superClass = SuperClass("Playa")
superClass.sayMyName()

subClass = SubClass("Montana", "Verde")
subClass.sayMyName()
subClass.whatIsMyColor()
