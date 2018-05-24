def process_numbers(fn):
	nums = [10, 20, 30, 192, 384, 585, 223, 383, 222, 283, 422]
	result = 0
	n1 = nums[0]
	for i in range(1, len(nums)):
		n2 = nums[i]
		result = fn(n1, n2)
		n1 = result

	return result

def main():
	r = process_numbers(lambda x,y:x+y)
	print("result of process_numbers", r)
	r = process_numbers(lambda x,y:x*y)
	print("result of process_numbers", r)

if __name__ == '__main__':
	main()






