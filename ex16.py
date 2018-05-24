class Product:
	def __init__(self, **kwargs):
		self.__name = kwargs["name"]
		self.__price = kwargs["price"]
		self.__category = kwargs["category"]

	def __float__(self):
		if type(self.__price) in (int, str):
			return float(self.__price)
		elif type(self.__price)==float:
			return self.__price
		else:
			return 0.0

	def __str__(self):
		return ("%s (%s)" % (self.__name, self.__category))

	def __mul__(self, value):
		return self.__price * value
	
	def __rmul__(self, value):
		return self.__mul__(value)

	def __add__(self, other):
		if type(other) in (int, float):
			return self.__price + other
		elif type(other) == Product:
			return self.__price + other.__price
		else:
			return self.__price

	def __radd__(self, other):
		return self.__add__(other)

	def print_info(self):
		print("name = {0}".format(self.__name))
		print("price = {0}".format(self.__price))
		print("category = {0}".format(self.__category))
		print("-"*50)

	def __iadd__(self, other):
		if type(other) in (int, float):
			self.__price += other
		elif type(other) is str:
			self.__name += other
		elif type(other) is Product:
			self.__name += other.__name
			self.__price += other.__price
		return self

	def __le__(self, other):
		if type(other) in (int, float):
			return self.__price <= other
		elif type(other) is str:
			return self.__name <= other
		elif type(other) is Product:
			return self.__price <= other.__price

def main():
	p1 = Product(name="Lenovo Laptop", category="Computers", price=45000.5)
	p2 = Product(name="Apple Macbook Pro", category="Computers", price=100000)
	p3 = Product(name="Toshiba", category="Computers", price=15000)

	p1.print_info()
	p1 += 4000
	p1 += " (sold by KVinod Inc)"

	p2 += p3
	# p1.print_info()
	# p2.print_info()

	print("p1 <= 50000", p1 <= 50000)
	print('p1 <= "Apple Macbook"', p1 <= "Apple Macbook")
	print("p1 <= p2", p1 <= p2)

	# x = p1 + 1000 + 2000
	# print("x = ", x)

	# y = p1 + p2 + p3
	# print("y = ", y)

	# price = float(p1)
	# print("Price = %f" % price)

	# discount = p1 * 0.25 
	# print("discount for the product '%s' is %f" % (p1, discount))

	# discount = 0.15 * p1
	# print("discount for the product '%s' is %f" % (p1, discount))



if __name__ == '__main__':
	main()








