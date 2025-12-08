from internal_opt import student_name_list


def student_main():
	choice = input("Press 1 to Add Students Details\nPress 2 to Search Students Details\nPress 3 to Update Students Details\nPress 4 to Delete Students Details\nEnter a Valid Choice : ")
	if choice == "1":
		create_student()
	elif choice == "2":
		ch=input("Press 1 to dsplay specific student details.\nPress 2 to display all student details.\nEnter valid choice: ")
		if ch=='1':
			search_student()
		else:
			show_all_student_details()	
	elif choice == "3" : 
		update_student_details()
	elif choice == "4" : 
		delet_student()
	else : 
		print("Invalid Choice. Please renter a valid choice")


def create_student():
	student_detail_file=open("student_details.txt",'a')
	student_serial_num=input("Enter serial number: ")
	student_rollnum=input("Enter rollnumber: ")
	student_name=input("Enter name of the student: ")
	final_details=f"{student_serial_num},{student_rollnum},{student_name}\n"
	student_detail_file.write(final_details)
	student_detail_file.close()
	print("Successfully Registered")

def show_details(x):
	x=x.replace("\n",'')
	details=x.split(',')
	print("Serial Number : ",details[0])
	print("Student Rollnum : ",details[1])
	print("Student Name : ",details[2])



def search_student():
	names=student_name_list()
	print(names)
	search_name=input("Enter student name you wish to search: ")
	
	st_detail_file=open('student_details.txt','r')
	student_detail=st_detail_file.readlines()
	st_detail_file.close()
	for i in student_detail:
		i=i.replace('\n','')
		data=i.split(',')
		if search_name in data:
			print('==================================')
			show_details(i)
			print('==================================')
			return data,i
	else:
		print("Enter valid name")



def show_all_student_details():
	st_files=open("student_details.txt",'r')
	s_data=st_files.readlines()
	for i in s_data:
		print('===================================')
		show_details(i)
		print('===================================')

	st_files.close()




def update_student_details():
	updated_list,old_st_str=search_student()
	old_st_str=old_st_str+'\n'
	st_file=open('student_details.txt','r')
	info_st=st_file.readlines()
	st_file.close()
	ch=int(input("Press 1 to update serial number of the student\nPress 2 to update rollnumber\nPress 3 to update name of the student: "))
	if ch==1:
		new_serial_num=input("Enter new serial number:")
		updated_list[0]=new_serial_num
	elif ch==2:
		new_roll_num=input("Enter updated roll number:")
		updated_list[1]=new_roll_num
	elif ch==3:
		new_student_name=input("Enter updated name:")
		updated_list[2]=new_student_name
		# update_name('sub1_internal1.txt',new_student_name,updated_list[2])
		# update_name('sub1_internal2.txt',new_student_name,updated_list[2])
		# update_name('sub1_internal3.txt',new_student_name,updated_list[2])
		# update_name('sub2_internal1.txt',new_student_name,updated_list[2])
		# update_name('sub2_internal2.txt',new_student_name,updated_list[2])
		# update_name('sub2_internal3.txt',new_student_name,updated_list[2])





	final_updated_str=f"{updated_list[0]},{updated_list[1]},{updated_list[2]}\n"
	
	curr_index=info_st.index(old_st_str)

	info_st[curr_index]=final_updated_str
	file_st=open("student_details.txt",'w')
	for j in info_st:
		file_st.write(j)
	file_st.close()
	print("Updated successfully")



def delet_student():
	st_list,st_str=search_student()
	print(st_list)

	st_str=st_str+'\n'
	print(st_str)
	file_st=open('student_details.txt','r')
	student_data=file_st.readlines()
	file_st.close()
	print(student_data)
	current_index=student_data.index(st_str)
	student_data.pop(current_index)
	file_st1=open("student_details.txt",'w')
	for k in student_data:
		file_st1.write(k)
	file_st1.close()

	print("Deleted successfully")


def update_name(file,updated_name,old_name):
	with open(file,'r') as file1:
		file_data=file1.readlines()
	for i in file_data:
		i=i.replace('\n','')
		data_item=i.split(',')
		if old_name in data_item:		
			current_index=file_data.index(i)
			data_item[0]=updated_name
			updated_str=f"{data_item[0]},{data_item[1]}\n"
			file_data[current_index]=updated_str
	with open(file,'w') as file2:
		for k in file_data:
			file2.write(k)


		




	



