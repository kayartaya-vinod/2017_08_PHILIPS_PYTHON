from ex21 import Person
import pickle
import shelve

def main():
	author = shelve.open("author.info")
	print("Author name/email = {}/{}".format(author["name"], author["email"]))
	del author["email"]

	# following raises KeyError as we have deleted the key 'email'
	# print("Author name/email = {}/{}".format(author["name"], author["email"]))


def main_3():
	author = shelve.open("author.info")
	author["name"] = "Vinod"
	author["email"] = "vinod@vinod.co"
	author["city"] = "Bangalore"
	author["website"] = "http://vinod.co"

	print("author info stored in author.info file.")

def main_2():
	with open("people.bin", "rb") as fh: 
		p = pickle.Unpickler(fh)
		lst = p.load()
		# print("type of lst is", type(lst))
		for p1 in lst:
			# print("type of p1 is", type(p1))
			print(p1)

def main_1():
	p1 = Person(); p1.name = "Vinod"; p1.age = 44

	lst = []
	lst.append(p1)

	p1 = Person(); p1.name = "John Doe"; p1.age = 24
	lst.append(p1)

	p1 = Person(); p1.name = "Jane Doe"; p1.age = 22
	lst.append(p1)

	with open("people.bin", "wb") as fh: 
		p = pickle.Pickler(fh)
		p.dump(lst)

	print("People data written to people.bin")

if __name__ == '__main__':
	main()