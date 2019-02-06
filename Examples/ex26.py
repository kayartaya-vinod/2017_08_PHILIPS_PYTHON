import http.client
import json

conn = http.client.HTTPConnection("vinod.co")
headers = {"content-type": "application/json"}

data = dict(firstname="Albert", last_name="Einstine", email="alei@mail.com")
data = json.dumps(data)

conn.request("POST", "/rest/contacts.php", data, headers)
body = conn.getresponse()
body = body.read().decode()

body = json.loads(body)
if body["success"]==True:
	print("Data posted with new id {}".format(body["id"]))
else:
	print(body)