def main():
	total = 0
	while True:
		num = input("Enter a number (0 to stop): ")
		try:
			num = int(num)
			if num==0: break

			total += num
		except ValueError:
			print("Only numbers allowed. Try again!")

	print("Total of all inputs = {0}".format(total))


if __name__ == '__main__':
	main()