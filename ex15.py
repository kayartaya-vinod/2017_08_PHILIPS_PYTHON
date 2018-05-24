class Person:
	def about():
		print("Person class by Vinod <vinod@vinod.co>")

	def __init__(self, name, city="Bangalore", email=""):
		self.__name = name
		self.__city = city
		self.__email = email
		self.__age = 20

	def info(this):
		print("name = " + this.__name)
		print("city = " + this.__city)
		print("email = " + this.__email)
		print("age = %d years " % this.age) # call to the getter @property age function
		print()

	# Java style setter/getter functions for mutating and accessing a member
	def setname(self, name):
		self.__name = name

	def getname(self):
		return self.__name

	# C# style setter/getter property

	# getter property
	@property
	def email(self):
		return self.__email

	# setter property
	@email.setter
	def email(self, email_address):
		self.__email = email_address

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		if age<0 or age > 120:
			raise ValueError("Age must be between 0 and 120 years")
		self.__age = age

def main():

	Person.about()

	# Person() is calling the __init__() with the newly constructed object
	p1 = Person("Vinod")
	p1.info()

	p1.setname("vinod kumar")
	p1.email = "vinod@vinod.co" # call to the @email.setter function
	p1.age = 44 # call to the @age.setter function

	print("p1's name is ", p1.getname())
	print("p1's email is ", p1.email)
	print("p1's age is %d years" % p1.age)
	print("-"*50)

	p2 = Person("Vinay", email="vinaykm@gmail.com")
	# p2.info()
	Person.info(p2)

	print("p2's email is ", p2.email)
	print("-"*50)

	# does not affect; but adds 
	p1.__name = "David"
	
	# actual way to change the so called 'private' variable
	p1._Person__name = "Miller"

	p1.info()


if __name__ == '__main__':
	main()
