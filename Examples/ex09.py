def test(n):
	print("recieved n as", n)
	print("yielding 100..")
	yield 100
	print("yielding 200..")
	yield 200
	print("yielding 300..")
	yield 300

def main():
	t = test(999) # DOES NOT CALL THE test() function here; just creates a generator object
	print("calling next(t)..")
	x = next(t) # calls test() function first time until `yield` is found
	print("x is", x)
	print("calling next(t)..")
	x = next(t) # calls test(), resumes from the previous `yield` to the next `yield`
	print("x is", x)

if __name__ == '__main__':
	main()