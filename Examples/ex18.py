class Camera(object):
	def __init__(self):
		print("From Camera constructor")

	def click(self):
		print("Smile please...click")

class Phone(object):
	def __init__(self):
		print("From Phone constructor")
	def call_number(self):
		print("Calling someone...")

	def click(self):
		print("Clicking on the phone...")


class SmartPhone(Phone, Camera):
	def __init__(self):
		# super().__init__()
		Camera.__init__(self)
		Phone.__init__(self)
		print("From SmartPhone constructor")

def main():
	sp = SmartPhone()
	sp.click()
	Camera.click(sp)
	sp.call_number()


if __name__ == '__main__':
	main()