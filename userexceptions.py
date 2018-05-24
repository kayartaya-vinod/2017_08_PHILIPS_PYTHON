# this and every file with .py is known as a module
# A module may comprise: variables, functions, classes, or some executable code
# variables, functions and classes from this module can be used in other modules

class InvalidAgeException(Exception):
	def __init__(self, message = "Invalid age. Must be a number between 1 and 120"):
		self.__message = message

	def __str__(self):
		return self.__message

		
class InvalidNameException(Exception):

	def __init__(self, message = "Invalid name. Must be a string"):
		self.__message = message

	def __str__(self):
		return self.__message

