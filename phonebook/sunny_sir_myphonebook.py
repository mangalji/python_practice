#my_phonebook.py
#contact - name,email,phonenumber 
#create contact
#single contact display
#display all contacts
#search contact
#update contact 
#delete contact 
#to be added 
#1. Import Contacts
#2. Export Contacts

filename = "master_phonebook_list.txt"

def create_contact() :
	name = input("Enter Contact Name : ")
	email = input("Enter Contact Email : ")
	phone_number = input("Enter Contact Number : ")

	contact_entry = "{},{},{}\n".format(name,email,phone_number)
	file = open(filename,"a")
	file.write(contact_entry)
	file.close()

	print("Contact Added Successfully")


"""
Name : Mohit
Email : mohit@gmail.com
Phone Number : 5464353534
"""

def display_contact(x):
	#print(x)
	x = x.replace("\n","")
	#print(x)
	contact = x.split(",")
	#print(contact)
	print("Name : ",contact[0])
	print("Email : ",contact[1])
	print("phone_number : ",contact[2])

def display_all_contact():
	file = open(filename,"r")
	master_data = file.readlines()
	print(master_data)
	print("================================")
	for i in master_data : 
		display_contact(i)
		print("================================")
	file.close()

def search_contact():
	search_term = input("Enter a Search Term : ")
	file = open(filename,"r")
	master_data = file.readlines()
	for i in master_data : 
		i = i.replace("\n","")
		contact = i.split(",")
		if search_term in contact : 
			print("================================")
			display_contact(i)
			print("================================")
			return master_data,i,contact
			break
	else : 
		print("Contact Not Found ")

	file.close()

def update_contact():
	master_data,current_contact, updated_contact = search_contact()
	current_contact = current_contact + "\n"
	#print("current_contact",current_contact)

	update_choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to Contact Number\nEnter Valid Input : ")
	if update_choice == "1" :
		new_name = input("Enter New Name : ")
		updated_contact[0] = new_name
	elif update_choice == "2":
		new_email = input("Enter New Email : ")
		updated_contact[1] = new_email
	elif update_choice == "3":
		new_number = input("Enter New Number : ")
		updated_contact[2] = new_number
	else :
		print("Invalid Choice")

	new_contact = "{},{},{}\n".format(updated_contact[0],updated_contact[1],updated_contact[2])

	current_index = master_data.index(current_contact)
	print("Before Change")
	print(master_data)
	master_data[current_index] = new_contact
	print("After Change")
	print(master_data)

	file = open(filename,"w")
	for j in master_data : 
		file.write(j)
	file.close()

	print("Contact Updated Successfully")


def delete_contact():
	master_data,current_contact, updated_contact = search_contact()
	current_contact = current_contact + "\n"
	master_data.remove(current_contact)
	print(master_data)

	file=open(filename,"w")
	for j in master_data:
		file.write(j)
	file.close()

	print("Contact successfully deleted!!")
			



