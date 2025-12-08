class Contact:
	def file_handling_use():
		pass

	def __init__(self):
		self.name = input("Enter the name: ")
		self.contact = int(input("Enter the contact no.: "))
		self.email = input("Enter the Email id: ")
		self.address = input("Enter the address: ")	
		# contact_entry = "{},{},{},{}\n".format(self.name,self.contact,self.email,self.address)
		# file = open("my_phonebook.txt","a")
		# file.write()  
	
	def show_data(self):
		print("Person Name: ",self.name)
		print("Person Contact No.: ",self.contact)
		print("Person Email id: ",self.email)
		print("Person Address: ",self.address)

	def update_data():
		con_choice = True
		while con_choice == True:
			choice = input("Press 1 to update name\nPress 2 to update contact no.\nPress 3 to update email id\nPress 4 to update address\nEnter the value: ")
			if choice == "1":
				self.name = input("Enter the updated name: ")
				break
			elif choice == "2":
				self.contact = int(input("Enter the updated contact no.: "))
				break
			elif choice == "3":
				self.email = input("Enter the updated Email id: ")
				break
			elif choice == "4":
				self.address = input("Enter the new address: ")
			else:
				print("Invalid Entry! please enter valid number.")
				con_choice = True
		else:
			print("Person's data updated successfully..")
			con_choice = False

	def search_data():
		pass


	def delete_data():
		pass

# person_1 = Contact()
# person_1.show_data()
ob_list=[]
for i in range(1,4):
	a=f"person{i}"
	print(a)
	a=Contact()
	ob_list.append(a)
abcd = ob_list[2]
abcd.show_data()


