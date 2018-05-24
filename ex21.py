# import userexceptions # have to use the members with 'userexceptions.' prefix
from userexceptions import InvalidAgeException, InvalidNameException

class Person(object):
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self, name):
		if type(name) is not str: 
			raise InvalidNameException("Only string expected for name!")

		self.__name = name
		
	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		if type(age) is not int: 
			raise InvalidAgeException("Only int expected!")

		if 0 < age <= 120:
			self.__age = age
		else:
			raise InvalidAgeException()

	def __str__(self):
		return "{} is {} years old.".format(self.__name, self.__age)

def main():
	p1 = Person()
	p1.name = "John doe"
	p1.age = 22
	print(p1)


if __name__ == '__main__':
	main()