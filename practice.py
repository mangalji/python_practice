# i = 1
# while i < 6 or i == 6:
# 	print(i)
# 	i += 1

mylist = [
		[1,2,3],
		[4,5,6],
		[7,8,9]
]
# for lists in mylist:
# 	for row in lists:
# 		print(row)

# a = [row for row in lists for lists in mylist]
a = [row for lists in mylist for row in lists]
print(a)