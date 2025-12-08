def left_bottom(size):
	for i in range(size):
		print("*"*(i+1))

def left_top(size):
	for i in range(size):
		count = size - i
		print("*"*(count+1))

def right_top(size):
	for i in range(size):
		count = size - i
		print(" "*count,"*"*(i+1))

def right_bottom(size):
	for i in range(size):
		count = size - i
		print(" "*(count+1),"*"*(i+1))

choice = int(input("enter the star pattern......\nPress 1 for start at left bottom\nPress2 for start at left top\nPress 3 for start at right top\nPress 4 for start at right bottom\nPlease enter the choice."))
print("-------------Enter the Size of star pattern--------------")
size = int(input("size: "))

if choice == 1:
	left_bottom(size)

elif choice == 2:
	left_top(size)

elif choice == 3:
	right_top(size)

elif choice == 4:
	right_bottom(size)

else:
	print("You enter the wrong choice..")