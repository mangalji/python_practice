from student_opt import *
from student_subject import *
from internal_opt import *
from final_marksheet import *

def main():
	print("Wel-Come to Our Internal Marks Management System")
	choice = input("Press 1 for Student related Operations\nPress 2 for Subject related Operations\nPress 3 for Internal Marks Operation\nPress 4 for Result Generation\nEnter a Valid Choice : ")
	if choice == '1' :
		student_main()
	elif choice == '2':
		student_subject_main()
	elif choice == '3':
		internal_marks_main()
	elif choice =='4':
		student_final_result_main()
	else :
		print("Invalid Choice Selected. Please renter a valid choice.")


to_continue=True


while to_continue:
	main()
	if to_continue==True:	
		ch=input("Do you wish to continue.Press 'Y' for Yes,'N' for No. ").upper()
		if ch=='Y':
			main()
			
		else:
			to_continue=False


