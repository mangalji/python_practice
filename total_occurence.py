from collections import defaultdict
string = 'hello'
count = defaultdict(int)
n = len(string)
for i in string:
	count[i] += 1
	print(count)

print(count)

print(defaultdict())