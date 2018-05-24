# read a number from the user
# and check if it's even or odd

num = input("Enter a number: ")

if num.isnumeric()==True:
	num = int(num)

	if num%2==0:
		print("%d is an even number" % num)
	else:
		print("{0} is an odd number".format(num))
else:
	print("OOPS! You must enter a number!")