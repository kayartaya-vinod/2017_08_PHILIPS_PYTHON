import json

def main():
	d = dict(name="Vinod", email="vinod@vinod.co", website="http://vinod.co")
	s = json.dumps(d) # dict to str
	print("type of s is", type(s))
	print(s)

	print()
	
	d1 = json.loads(s) # str to dict
	print("type of d1 is", type(d1))
	print(d1)

if __name__ == '__main__':
	main()