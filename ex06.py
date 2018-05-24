# loop through the dictionary

info = {}
info["name"] = "Vinod"
info["email"] = "vinod@vinod.co"
info["phone_numbers"] = ("9731424784", "9844083934")
info["address"] = dict(city="Bangalore", state="Karnataka", country="India")

for key in info.keys():
	val = info[key]

	if type(val) in [list, tuple]:
		print("Total %d %s found" % (len(val), key))
		for i in range(0, len(val)):
			print("\t%d %s" % (i+1, val[i]))
	elif type(val) is dict:
		print("The values for %s" % key)
		for k in val.keys():
			print("\t%s --> %s" % (k, val[k]))
	else:
		print("%s --> %s" % (key, info[key]))

