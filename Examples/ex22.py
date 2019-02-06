# read the content from "people.csv" and display information

def main_1():
	file = open("people.csv", "rt")
	content = file.readlines()
	file.close()

	for line in content:
		id, fname, lname, email = line.split(",")
		print("{} {} - {}".format(fname, lname, email), end="")

def main_2():
	for line in open("people.csv"):
		id, fname, lname, email = line.split(",")
		print("{} {} - {}".format(fname, lname, email), end="")

def get_data():
	id = input("Enter id: ")
	first_name = input("Enter first_name: ")
	last_name = input("Enter last_name: ")
	email = input("Enter email: ")
	return "{},{},{},{}\n".format(id, first_name, last_name, email)

def main():
	with open("people.csv", "at") as file:
		# 'file' is accessible with in this block, and gets
		# closed automatically when the block exits
		while True:
			data = get_data()
			file.write(data)
			ans = input("Do you want to add another? (yes/no): ")
			if ans.upper() not in ("YES", "Y"):
				break

	print("Data updated to people.csv")

if __name__ == '__main__':
	main()

















