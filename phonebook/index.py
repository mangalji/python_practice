from my_phonebook import *
# from sunny_sir_myphonebook import *
def reuse():
	choice = input("Press 1 for Creating contact\nPress 2 for Display All Contact\nPress 3 Search Contact\nPress 4 for Update Contact\nPress 5 for Delete Contact\nPlease Enter a Valid Choice : ")
	if choice == "1" :
		create_contact()
	elif choice == "2" :
		display_all_contact()
	elif choice == "3":
		search_contact()
	elif choice == "4" :
		update_contact()
	elif choice == "5":
		delete_contact()
	else : 
		print("Invalid Choice, Please enter a valid choice ")
		reuse()

def continue_choice():
	temp = True
	again_input = input("Do you want to re-check your phonebook. if yes: enter Y, if no: enter N\n").upper()
	if again_input == 'Y':
		temp = True
	elif again_input == 'N':
		temp = False
	else:
		continue_choice()
	return temp

print("Welcome to My Phonebook Project")
Reuse_phonebook = True
while Reuse_phonebook:
	reuse()
	Reuse_phonebook = continue_choice()
