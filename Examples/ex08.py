import ex07


def main_1():
	ex07.print_cal(2, 2016)
	ex07.print_cal(2)
	ex07.print_cal(None, 2018)
	ex07.print_cal(year=2018)

def add_all(*args):
	# print("Type of args is %s" % type(args))
	# Type of args is <class 'tuple'>
	s = 0
	for n in args:
		s+=n
	return s

def main_2():
	total = add_all(10, 294, 59, 383, 383, 484, 282)
	print("Total is %d" % total)

def report(**kwargs):
	# print("Type of kwargs is %s" % type(kwargs))
	# Type of kwargs is <class 'dict'>
	for key in kwargs.keys():
		print("%s --> %s" % (key, kwargs[key]))

def info(name, city="Bangalore", *args, **kwargs):
	print("name", name)
	print("city", city)
	print("args", args)
	print("kwargs", kwargs)

def main():
	# report(name="Vinod", email="vinod@vinod.co", city="Bangalore")
	# info(city = "Bengaluru", name="Vinod")
	info("vinod", 100, 200, 300, "mysore", company="Philips", email="vinod@vinod.co")

if __name__ == '__main__':
	main()






