# Read a number from the user and 
# print the multiplication for the same

num = int(input("Enter a number: "))

n = 1
while n<=10: 
	p = num * n
	print("{0} * {1} = {2}".format(num, n, p))
	n += 1

