n = int(input("enter the number of elements"))
assert n > 0 
s = 0.0
i = 0
while n > i:
	a = float(input("enter value"))
	s = s + a
	i = i+1
	assert n==i
print(f"sum of {n} no. is {s}")