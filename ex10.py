def fibo_generator():
	a, b = -1, 1
	while True:
		c = a+b
		a, b = b, c
		yield c

def main():
	fibo = fibo_generator()
	for i in range(0, 10):
		print(next(fibo))

def seq_generator(seed=1, inc=1):
	while True:
		num = seed
		seed += inc
		yield num

def main_1():
	seq1 = seq_generator()
	seq2 = seq_generator(100, 10)

	print("First 10 numbers from seq1")
	for i in range(0, 10):
		print(next(seq1))

	print("-"*80)
	print("First 10 numbers from seq2")
	for i in range(0, 10):
		print(next(seq2))

if __name__ == '__main__':
	main()