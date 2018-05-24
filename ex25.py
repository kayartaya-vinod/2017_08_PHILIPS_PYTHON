import http.client 
import json

# import os
# os.environ["http_proxy"] = "http://165.225.96.34:9480"

conn = http.client.HTTPConnection("vinod.co")

print("sending the request....")
conn.request("GET", "/rest/contacts.php?id=1")
print("request sent, response received.")

resp = conn.getresponse()

body = resp.read().decode()

p1 = json.loads(body)

print("Name = {} {}".format(p1["first_name"], p1["last_name"]))
print("Email = {}".format(p1["email"]))

# print(body)


