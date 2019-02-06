class Person:
	# member of the class; will be copied to each object instances
	name = "Robert"
	def info(self):
		print("Inside the info() function, id(self) is", id(self))

def main():
	p1 = Person()
	print("Inside main(), id(p1) is", id(p1))
	p1.info()

	print("id(Person.name) is ", id(Person.name))
	print("id(p1.name) is ", id(p1.name))

	p1.name = "Miller"
	print("id(Person.name) is ", id(Person.name))
	print("id(p1.name) is ", id(p1.name))

	print("Person.name is ", Person.name)
	print("p1.name is ", p1.name)

if __name__ == '__main__':
	main()
