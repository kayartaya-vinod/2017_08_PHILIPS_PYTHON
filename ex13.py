def is_even(n):
	return n%2==0

def main_1():
	nums = [10, 21, 30, 192, 384, 585, 223, 383, 222, 283, 422]

	evens = filter(is_even, nums)
	print("evens", list(evens))
	odds = filter(lambda x:x%2, nums)
	print("odds", list(odds))

def main_2():
	names = ["vinod kumar", 100,  "john doe", "jane doe", "VINAY kumar", "RAMESH raj", "Harish"]

	f = lambda x:x.title() if type(x) is str else x
	modified_names = map(f, names)

	for name in modified_names:
		print(name)

def main_3():
	people = [{
		  "first_name": "Leshia",
		  "last_name": "Matteo",
		  "gender": "Female"
		}, {
		  "first_name": "Grady",
		  "last_name": "Kildea",
		  "gender": "Male"
		}, {
		  "first_name": "Nico",
		  "last_name": "Arundel",
		  "gender": "Male"
		}, {
		  "first_name": "Katrine",
		  "last_name": "Ginni",
		  "gender": "Female"
		}, {
		  "first_name": "Carlee",
		  "last_name": "Valentetti",
		  "gender": "Female"
		}, {
		  "first_name": "Enoch",
		  "last_name": "Curnnok",
		  "gender": "Male"
		}, {
		  "first_name": "Ingmar",
		  "last_name": "Messier",
		  "gender": "Male"
		}, {
		  "first_name": "Benji",
		  "last_name": "De Filippi",
		  "gender": "Male"
		}, {
		  "first_name": "Adoree",
		  "last_name": "Jeness",
		  "gender": "Female"
		}, {
		  "first_name": "Florinda",
		  "last_name": "New",
		  "gender": "Female"
		}]

	f = lambda p: ("Mr." if p["gender"]=="Male" else "Ms.") + p["last_name"] + " " + p["first_name"]

	r = map(f, people)
	lst = list(r)

	for p in lst:
		print(p)


def main():
	nums = [10, 21, 30, 192, 384, 585, 223, 383, 222, 283, 422]
	import functools

	total = functools.reduce(lambda a,b:a+b, nums)
	print("total", total)

	max_num = functools.reduce(lambda a,b: a if a>b else b, nums)
	print("max_num", max_num)
	
if __name__ == '__main__':
	main()


















