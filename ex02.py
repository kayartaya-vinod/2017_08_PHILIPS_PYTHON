# check the number of days in a given month and year

month = input("Enter month: ")
year = input("Enter year: ")

month, year = int(month), int(year)

if month==2:
	days = 29 if (year%400==0 or (year%100!=0 and year%4==0)) else 28
elif month in [4,6,9,11]:
	days = 30
elif month in [1,3,5,7,8,10,12]:
	days = 31
else:
	print("Invalid month entered. Must be between 1-12.")
	exit()

print("There are %d days in the month %d of year %d" % (days, month, year))




