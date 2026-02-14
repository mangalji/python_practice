import json

with open("person.json","r") as file:
	# print(file)
	# print(json.load(file))
	data = json.load(file)
	print(data)		