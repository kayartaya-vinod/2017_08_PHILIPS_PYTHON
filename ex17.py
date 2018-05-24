class Person(object):

	def __init__(self):
		self.name = "Vinod"
		print("From inside of Person.__init__")

	def info(self):
		print("Information about Person")

class Employee(Person):
	def __init__(self):
		# super().__init__()
		Person.__init__(self)
		print("From inside of Employee.__init__")

	# overriding the inherited method (hides visibility of base class function)
	def info(self):
		super().info()
		# Person.info(self) # optionally invoke a similar function from base class
		print("Information about Employee")


def main():
	e1 = Employee() # --> call to the Employee.__init__
	e1.info()
	print("e1.name is", e1.name)
	# Person.info(e1)

if __name__ == '__main__':
	main()
