def test(*args):
	print("There are %d arguments" % len(args))
	for arg in args:
		print("\t", arg)

def print_info(**kwargs):
	print(kwargs)

def main():
	d1 = {"name": "Vinod", "city": "Bangalore"}
	d2 = dict(a=1, b=2, c=3, d=4)

	print_info(**d1)
	print("-"*50)
	print_info(**d2)

	vals = d1.values()
	test(*vals)

if __name__ == '__main__':
	main()