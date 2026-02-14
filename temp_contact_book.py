# def menu():
# 	print('Press 1 for showing the phone numbers\nPress 2 for add the phone numbers\nPress 3 for remove the phone numbers\nPress 4 to lookup the phone number\nPress 5 for Quit.\n\nEnter your choice')


numbers = {}
a = True
while a:

	choice = int(input('Press 1 for showing the phone numbers\nPress 2 for add the phone numbers\nPress 3 for remove the phone numbers\nPress 4 to lookup the phone number\nPress 5 for Quit.\n\nEnter your choice: '))	
	if choice == 1:
		print("All available telephone numbers: ")
		for x,y in numbers.items():
			print(f"Name: {x}, number: {y}")
		print()
	
	elif choice == 2:
		print("Add the contact of any person!")
		name = input("enter the name: ")
		phone = input("enter the phone number: ")
		numbers[name] = phone
	
	elif choice == 3:
		print("Delete the conatct number of any person!")
		name = input("enter the name: ")
		if name in numbers:
			del numbers[name]
		else:
			print(f"contact number with this {name} does not exist!!")
	
	elif choice == 4:
		print("LookUp phone numbers!")
		name = input("enter the name: ")
		if name in numbers:
			print(f"the phone number is {numbers[name]}")
		else:
			print(f"the contact number of this person named {name} does not exist!!")
	
	elif choice == 5:
		a = False