def test(*args):
	try:
		n1 = args[0]
		n2 = args[1]

		n1 = int(n1) if type(n1) is str else n1
		n2 = int(n2) if type(n2) is str else n2

		if n1<5 : return;

		q = n1//n2
		return q
		
	except (ValueError, ZeroDivisionError) as x:
		print(x)
	except IndexError:
		print("Two numbers were expected, got {}".format(len(args)))
	except BaseException:
		print("There was an error")
	finally:
		print("Some cleanup here...")

	print("End of test() function...")
	
def main():
	n1, n2 = 17, 3
	q = test(n1, n2)

	print("{} / {} = {}".format(n1, n2, q))
	# test(2, 3)
	# test("17", "3")

	# print("-"*80)
	# test(17, 0)
	# test("17", "five")
	# test(17)


if __name__ == '__main__':
	main()