import os

def student_subject_main():
	cho= input("Press 1 to Add subject\nPress 2 to show subjects\nPress 3 to Update subject\nPress 4 to Delete subject\nEnter a Valid Choice : ")
	if cho=='1':
		create_subject()
	elif cho=='2':
		show_subject()
	elif cho=='3':
		update_subject()
	elif cho=='4':
		delete_subject()
	else:
		print("Invalid choice.Enter valid choice")
		student_subject_main()
		


def create_subject():
	subject_file=open("subject.txt",'a')
	subject_name=input("Enter subject name: ")
	fin=f"{subject_name}\n"
	subject_file.write(fin)
	subject_file.close()
	print("Successfully Added")


def show_subject():
	sub_file=open("subject.txt",'r')
	sub_data=sub_file.readlines()
	for i in sub_data:
		i=i.replace('\n','')
		print('==================')
		print(i)
		print('==================')
	sub_file.close()

def update_subject():
	show_subject()
	user_ch=input("Enter subject you want to update:")
	sub_file1=open("subject.txt",'r')
	sub_data1=sub_file1.readlines()
	sub_file1.close()

	for i in sub_data1:
		i=i.replace('\n','')
		if user_ch==i:
			i+='\n'
			up_sub_name=input("Enter updated name: ")
			curr_index=sub_data1.index(i)
			sub_data1[curr_index]=up_sub_name+'\n'
	fil_sub=open("subject.txt",'w')
	for l in sub_data1:
		fil_sub.write(l)
	fil_sub.close()


def delete_subject():
	show_subject()
	user_ch=input("Enter subject you want to delete:")
	sub_file1=open("subject.txt",'r')
	sub_data2=sub_file1.readlines()
	sub_file1.close()
	for i in sub_data2:
		i=i.replace('\n','')
		if user_ch==i:
			i+='\n'
			current_id=sub_data2.index(i)
			sub_data2.pop(current_id)
		if user_ch=='subject1':
			os.remove('sub1_internal1.txt')
			os.remove('sub1_internal2.txt')
			os.remove('sub1_internal3.txt')
		elif user_ch=='subject2':
			os.remove('sub2_internal1.txt')
			os.remove('sub2_internal2.txt')
			os.remove('sub2_internal3.txt')

	fil_sub=open("subject.txt",'w')
	for j in sub_data2:
		fil_sub.write(j)	
	fil_sub.close()
	print("Subject Deleted sussessfully")





