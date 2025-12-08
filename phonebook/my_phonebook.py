#my_phonebook.py
#contact - name,email,phonenumber 
#create contact
#single contact display
#display all contacts
#search contact
#update contact 
#delete contact 

from re import fullmatch

filename = "master_phonebook_list.txt"


def email_validation(email):
	valid = fullmatch(r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", email)
	if valid:
		return True
	else:
		return False
def contact_number_validation(number):
	check_ = len(number)
	if check_ > 10 or check_ < 10:
		return False
	else:
		return True

def email_func():
	email = input("Enter Contact Email : ")
	good_email = ""
	check_email = email_validation(email)
	correct_email = True
	while correct_email:
		if check_email == True:
			good_email = email
			correct_email = False
		else:
			print("enter the valid mail!")
			good_email = input("enter the email: ")
			again_check = email_validation(good_email)
			if again_check == True:
				correct_email = False
			else:
				correct_email = True
	return good_email

def phone_number_func():
	phone_number = input("Enter Contact Number : ")
	correct_number = ""
	check_number = contact_number_validation(phone_number)
	num_is_true = True
	while num_is_true:
		if check_number == True:
			correct_number = phone_number
			num_is_true = False
		else:
			print("enter the valid contact number!")
			correct_number = input("enter the number again: ")
			again_ch = contact_number_validation(correct_number)
			if again_ch == False:
				num_is_true = True
			else:
				num_is_true = False
	return correct_number

def read():
	file = open(filename,"r")
	master_data = file.readlines()
	file.close()
	return master_data

def write_mode(master_data):
	file = open(filename,"w")
	for j in master_data : 
		file.write(j)
	file.close()

def create_contact() :
	name = input("Enter Contact Name : ")
	email_ = email_func() 
	phone_number_ = phone_number_func()
	contact_entry = "{},{},{}\n".format(name,email_,phone_number_)
	file = open(filename,"a")
	file.write(contact_entry)
	file.close()

	print("Contact Added Successfully")

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
	master_data = read()
	for i in master_data : 
		i = i.replace("\n","")
		contact = i.split(",")
		if search_term in contact : 
			print("================================")
			display_contact(i)
			print("================================")
			return i, contact
			break
	else : 
		print("Contact Not Found ")
		return search_contact()

def update_contact():
	current_contact, updated_contact = search_contact()
	current_contact = current_contact + "\n"
	master_data = read()

	update_choice = input("Press 1 to change Name\nPress 2 to change Email\nPress 3 to Contact Number\nEnter Valid Input : ")
	if update_choice == "1" :
		new_name = input("Enter New Name : ")
		updated_contact[0] = new_name
	elif update_choice == "2":
		updated_contact[1] = email_func() 
	elif update_choice == "3":
		updated_contact[2] = phone_number_func() 
	else :
		print("Invalid Choice")
		return update_contact()

	new_contact = "{},{},{}\n".format(updated_contact[0],updated_contact[1],updated_contact[2])

	current_index = master_data.index(current_contact)
	print("Before Change")	
	print(master_data)
	master_data[current_index] = new_contact
	print("After Change")
	print(master_data)

	write_mode(master_data)
	print("Contact Updated Successfully")

def delete_contact():
	current_contact,updated_contact = search_contact()
	current_contact += "\n"
	master_data = read()

	current_index = master_data.index(current_contact)
	master_data.pop(current_index)
	# print(master_data)
	for k in master_data:
		print("================================")
		display_contact(k)
		print("================================")

	file = write_mode(master_data)	

	print("---Contact deleted Successfully-----")

'''def delete_contact():
	search_term = input("enter the term which you want to delete: ")
	# current_contact = ""
	# updated_contact = []
	file = open(filename,"r")
	master_data = file.readlines()
	file = open(filename,"w")
	file.close()
	file = open(filename,"a")
	for line in master_data:
		if search_term not in line:
			file.write(line)
	print("---deleted---")
	file.close()	'''
	


















