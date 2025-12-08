from student_subject import show_subject 

def internal_marks_main():
	choice = input("Press 1 for enter marks\nPress 2 to show marks\nPress 3 to update marks\nPress 4 to delete marks\nEnter a Valid Choice : ")
	if choice=='1':
		enter_marks()
	elif choice=='2':
		show_marks()
	elif choice=='3':
		update_marks()

	elif choice=='4':
		delete_marks()
	else:
		print("Invalid choice")
		internal_marks_main()



def student_name_list():
	student_names=[]
	with open('student_details.txt','r') as file:
		student_d=file.readlines()
	
	for lin in student_d:
		lin=lin.replace('\n','')
		data_list=lin.split(',')
		a=data_list[2]
		student_names.append(a)
	return student_names


def enter_marks():
	st_names=student_name_list()
	print(st_names)

	st_choice=input("Enter which student marks you wish to enter: ")
	if st_choice in st_names:
		show_subject()
		sub_choice=input("Enter which subject's internal marks you wish to enter.\nPress 1 for subject-1\nPress 2 for subject-2: ")
		if sub_choice=='1':
			internal_selection=input("Which internal marks you wish to enter.\nPress 1 for Internal-1.\nPress 2 for Internal-2.\nPress 3 for Internal-3: ")
			if internal_selection=='1'and st_choice in st_names:
				internal1_marks=input("Enter Internal-1 marks:")
				a=st_names.index(st_choice)
				internal1_marks_final=f"{st_names[a]},{internal1_marks}\n"
				with open("sub1_internal1.txt",'a') as file1:
					file1.write(internal1_marks_final)
			elif internal_selection=='2'and st_choice in st_names:
				internal2_marks=input("Enter Internal-2 marks:")
				b=st_names.index(st_choice)
				internal2_marks_final=f"{st_names[b]},{internal2_marks}\n"
				with open("sub1_internal2.txt",'a') as file2:
					file2.write(internal2_marks_final)
			elif internal_selection=='3'and st_choice in st_names:
				internal3_marks=input("Enter Internal-3 marks:")
				c=st_names.index(st_choice)
				internal3_marks_final=f"{st_names[c]},{internal3_marks}\n"
				with open("sub1_internal3.txt",'a') as file3:
					file3.write(internal3_marks_final)
		elif sub_choice=='2':
			internal_select=input("Which internal marks you wish to enter.\nPress 1 for Internal-1.\nPress 2 for Internal-2.\nPress 3 for Internal-3: ")
			if internal_select=='1'and st_choice in st_names:
				internal1_marks=input("Enter Internal-1 marks:")
				internal1_marks_final=f"{st_choice},{internal1_marks}\n"
				with open("sub2_internal1.txt",'a') as file1:
					file1.write(internal1_marks_final)
			elif internal_select=='2'and st_choice in st_names:
				internal2_marks=input("Enter Internal-2 marks:")
				internal2_marks_final=f"{st_choice},{internal2_marks}\n"
				with open("sub2_internal2.txt",'a') as file2:
					file2.write(internal2_marks_final)
			elif internal_select=='3'and st_choice in st_names:
				internal3_marks=input("Enter Internal-3 marks:")
				internal3_marks_final=f"{st_choice},{internal3_marks}\n"
				with open("sub2_internal3.txt",'a') as file3:
					file3.write(internal3_marks_final)
	else:
		print("student name not found")


def show_marks():
	st_names=student_name_list()
	print(st_names)
	st_choice=input("Enter which student marks you wish to enter: ")

	if st_choice in st_names:
		show_subject()
		sub_choice=input("Enter which subject's internal marks you wish to see.\nPress 1 for subject-1\nPress 2 for subject-2.\nPress 3 to show all subject marks: ")

		if sub_choice=='1' and st_choice in st_names:
			subject1_internal1_marks = 'NA'
			subject1_internal2_marks = 'NA'
			subject1_internal3_marks = 'NA'
			#Opening internal-1 file and reading data from it.
			with open("sub1_internal1.txt",'r') as inter1_file:
				inter1_data=inter1_file.readlines()
				for info in inter1_data:
					info=info.replace('\n','')
					dat_1=info.split(',')
				
					if st_choice in dat_1:
						subject1_internal1_marks=dat_1[1]
			#Opening internal-2 file and reading data from it.
			with open("sub1_internal2.txt",'r') as inter2_file:
				inter2_data=inter2_file.readlines()
				for info1 in inter2_data:
					info1=info1.replace('\n','')
					dat_2=info1.split(',')
					if st_choice in dat_2:
						subject1_internal2_marks=dat_2[1]
			#Opening internal-3 file and reading data from it.
			with open("sub1_internal3.txt",'r') as inter3_file:
				inter3_data=inter3_file.readlines()
				for info2 in inter3_data:
					info2=info2.replace('\n','')
					dat_3=info2.split(',')
					if st_choice in dat_3:
						subject1_internal3_marks=dat_3[1]
			print(f"{st_choice}'s Subject-1 Marks")
			print('=========================')
			print(f"Internal-1 Marks:{subject1_internal1_marks}")
			print(f"Internal-2 Marks:{subject1_internal2_marks}")
			print(f"Internal-3 Marks:{subject1_internal3_marks}")
			print('=========================')
		elif sub_choice=='2' and st_choice in st_names:
			subject2_internal1_marks = 'NA'
			subject2_internal2_marks = 'NA'
			subject2_internal3_marks = 'NA'
			#Opening internal-1 file and reading data from it.
			with open("sub2_internal1.txt",'r') as inter1_file:
				inter1_data=inter1_file.readlines()
				for info_1 in inter1_data:
					info_1=info_1.replace('\n','')
					dat=info_1.split(',')
					if st_choice in dat:
						subject2_internal1_marks=dat[1]
			#Opening internal-2 file and reading data from it.
			with open("sub2_internal2.txt",'r') as inter2_file:
				inter2_data=inter2_file.readlines()
				for info_2 in inter2_data:
					info_2=info_2.replace('\n','')
					dat2=info_2.split(',')
					if st_choice in dat2:
						subject2_internal2_marks=dat2[1]
			#Opening internal-3 file and reading data from it.
			with open("sub2_internal3.txt",'r') as inter3_file:
				inter3_data=inter3_file.readlines()
				for info_3 in inter3_data:
					info_3=info_3.replace('\n','')
					dat3=info_3.split(',')
					if st_choice in dat3:
						subject2_internal3_marks=dat3[1]
			print(f"{st_choice}'s Subject-2 Marks")
			print('=======================')
			print(f"Internal-1 Marks:{subject2_internal1_marks}")
			print(f"Internal-2 Marks:{subject2_internal2_marks}")
			print(f"Internal-3 Marks:{subject2_internal3_marks}")
			print('=======================')
		elif sub_choice=='3' and st_choice in st_names:
			subject1_internal1_marks = 'NA'
			subject1_internal2_marks = 'NA'
			subject1_internal3_marks = 'NA'
			subject2_internal1_marks = 'NA'
			subject2_internal2_marks = 'NA'
			subject2_internal3_marks = 'NA'
			#Opening internal-1 file and reading data from it.
			with open("sub1_internal1.txt",'r') as inter1_file:
				inter1_data=inter1_file.readlines()
				for info in inter1_data:
					info=info.replace('\n','')
					dat_1=info.split(',')
					if st_choice in dat_1:
						subject1_internal1_marks=dat_1[1]
			#Opening internal-2 file and reading data from it.
			with open("sub1_internal2.txt",'r') as inter2_file:
				inter2_data=inter2_file.readlines()
				for info1 in inter2_data:
					info1=info1.replace('\n','')
					dat_2=info1.split(',')
					if st_choice in dat_2:
						subject1_internal2_marks=dat_2[1]
			#Opening internal-3 file and reading data from it.
			with open("sub1_internal3.txt",'r') as inter3_file:
				inter3_data=inter3_file.readlines()
				for info2 in inter3_data:
					info2=info2.replace('\n','')
					dat_3=info2.split(',')
					if st_choice in dat_3:
						subject1_internal3_marks=dat_3[1]
			print(f"{st_choice}'s Subject-1 Marks")
			print('=========================')
			print(f"Internal-1 Marks:{subject1_internal1_marks}")
			print(f"Internal-2 Marks:{subject1_internal2_marks}")
			print(f"Internal-3 Marks:{subject1_internal3_marks}")
			print('=========================')


			#Opening internal-1 file and reading data from it.
			with open("sub2_internal1.txt",'r') as inter1_file:
				inter1_data=inter1_file.readlines()
				for info_1 in inter1_data:
					info_1=info_1.replace('\n','')
					dat=info_1.split(',')
					if st_choice in dat:
						subject2_internal1_marks=dat[1]
			#Opening internal-2 file and reading data from it.
			with open("sub2_internal2.txt",'r') as inter2_file:
				inter2_data=inter2_file.readlines()
				for info_2 in inter2_data:
					info_2=info_2.replace('\n','')
					dat2=info_2.split(',')
					if st_choice in dat2:
						subject2_internal2_marks=dat2[1]
			#Opening internal-3 file and reading data from it.
			with open("sub2_internal3.txt",'r') as inter3_file:
				inter3_data=inter3_file.readlines()
				for info_3 in inter3_data:
					info_3=info_3.replace('\n','')
					dat3=info_3.split(',')
					if st_choice in dat3:
						subject2_internal3_marks=dat3[1]
			print(f"{st_choice}'s Subject-2 Marks")
			print('=======================')
			print(f"Internal-1 Marks:{subject2_internal1_marks}")
			print(f"Internal-2 Marks:{subject2_internal2_marks}")
			print(f"Internal-3 Marks:{subject2_internal3_marks}")
			print('=======================')
	else:
		print("student name not found")
	



def update_marks():
	st_names=student_name_list()
	print(st_names)

	st_choice=input("Enter which student marks you wish to enter: ")
	if st_choice in st_names:
		show_subject()
		sub_choice=input("Enter which subject's internal marks you wish to update.\nPress 1 for subject-1\nPress 2 for subject-2.")
		if sub_choice=='1':
			internal_choice=input("Enter which internal marks you want to update.\nPress 1 to update Internal-1 marks.\nPress 2 to update Internal-2 marks.\nPress 3 to update Internal-3 marks.")
			subject1_internal1_marks = 'NA'
			subject1_internal2_marks = 'NA'
			subject1_internal3_marks = 'NA'
			if internal_choice=='1':
				with open("sub1_internal1.txt",'r') as inter1_file:
					inter1_data=inter1_file.readlines()
					for info in inter1_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter1_index=inter1_data.index(info)
							ans=input("Enter Internal-1 updated marks: ")
							fin1=f"{st_choice},{ans}\n"
							inter1_data[inter1_index]=fin1
							with open("sub1_internal1.txt",'w') as inter1_file:
								for k in inter1_data:
									inter1_file.write(k)
				print("Updated successfully")
			elif internal_choice=='2':
				with open("sub1_internal2.txt",'r') as inter1_file:
					inter2_data=inter1_file.readlines()
					for info in inter2_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter2_index=inter2_data.index(info)
							ans1=input("Enter Internal-2 updated marks: ")
							fin2=f"{st_choice},{ans1}\n"
							inter2_data[inter1_index]=fin2
							with open("sub1_internal2.txt",'w') as inter2_file:
								for k in inter2_data:
									inter2_file.write(k)
				print("Updated successfully")
			elif internal_choice=='3':
				with open("sub1_internal3.txt",'r') as inter3_file:
					inter3_data=inter3_file.readlines()
					for info in inter3_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter3_index=inter3_data.index(info)
							ans3=input("Enter Internal-3 updated marks: ")
							fin3=f"{st_choice},{ans3}\n"
							inter3_data[inter3_index]=fin3
							with open("sub1_internal3.txt",'w') as inter3_file:
								for k in inter3_data:
									inter3_file.write(k)
				print("Updated successfully")
		elif sub_choice=='2':
			internal_choice=input("Enter which internal marks you want to update.\nPress 1 to update Internal-1 marks.\nPress 2 to update Internal-2 marks.\nPress 3 to update Internal-3 marks.")
			if internal_choice=='1':
				with open("sub2_internal1.txt",'r') as inter1_file:
					inter1_data=inter1_file.readlines()
					for info in inter1_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter1_index=inter1_data.index(info)
							ans=input("Enter Internal-1 updated marks: ")
							fin1=f"{st_choice},{ans}\n"
							inter1_data[inter1_index]=fin1
							with open("sub2_internal1.txt",'w') as inter1_file:
								for k in inter1_data:
									inter1_file.write(k)
				print("Updated successfully")
			elif internal_choice=='2':
				with open("sub2_internal2.txt",'r') as inter1_file:
					inter2_data=inter1_file.readlines()
					for info in inter2_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter2_index=inter2_data.index(info)
							ans1=input("Enter Internal-2 updated marks: ")
							fin2=f"{st_choice},{ans1}\n"
							inter2_data[inter1_index]=fin2
							with open("sub2_internal2.txt",'w') as inter2_file:
								for k in inter2_data:
									inter2_file.write(k)
				print("Updated successfully")
			elif internal_choice=='3':
				with open("sub2_internal3.txt",'r') as inter3_file:
					inter3_data=inter3_file.readlines()
					for info in inter3_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter3_index=inter3_data.index(info)
							ans3=input("Enter Internal-3 updated marks: ")
							fin3=f"{st_choice},{ans3}\n"
							inter3_data[inter3_index]=fin3
							with open("sub2_internal3.txt",'w') as inter3_file:
								for k in inter3_data:
									inter3_file.write(k)
				print("Updated successfully")
	else:
		print("Student name not found.Enter Valid name")



def delete_marks():
	st_names=student_name_list()
	print(st_names)
	st_choice=input("Enter which student marks you wish to enter: ")
	if st_choice in st_names:
		show_subject()
		sub_choice=input("Enter which subject's internal marks you wish to delete.\nPress 1 for subject-1\nPress 2 for subject-2.")
		if sub_choice=='1':
			internal_choice=input("Enter which internal marks you want to delete.\nPress 1 to delet Internal-1 marks.\nPress 2 to delet Internal-2 marks.\nPress 3 to delet Internal-3 marks.")
			subject1_internal1_marks = 'NA'
			subject1_internal2_marks = 'NA'
			subject1_internal3_marks = 'NA'
			if internal_choice=='1':
				with open("sub1_internal1.txt",'r') as inter1_file:
					inter1_data=inter1_file.readlines()
					for info in inter1_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter1_index=inter1_data.index(info)
							inter1_data.pop(inter1_index)
							with open("sub1_internal1.txt",'w') as inter1_file:
								for k in inter1_data:
									inter1_file.write(k)
				print("Deleted successfully")
			elif internal_choice=='2':
				with open("sub1_internal2.txt",'r') as inter1_file:
					inter2_data=inter1_file.readlines()
					for info in inter2_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter2_index=inter2_data.index(info)
							inter2_data.pop(inter2_index)
							with open("sub1_internal2.txt",'w') as inter2_file:
								for k in inter2_data:
									inter2_file.write(k)
				print("Deleted successfully")
			elif internal_choice=='3':
		
				with open("sub1_internal3.txt",'r') as inter3_file:
					inter3_data=inter3_file.readlines()
					for info in inter3_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter2_index=inter3_data.index(info)
							inter3_data.pop(inter2_index)
							with open("sub1_internal3.txt",'w') as inter3_file:
								for k in inter3_data:
									inter3_file.write(k)
				print("Deleted successfully")
		elif sub_choice=='2':
			subject1_internal1_marks = 'NA'
			subject1_internal2_marks = 'NA'
			subject1_internal3_marks = 'NA'
			inter_ch=input("Enter which internal marks you want to delete.\nPress 1 to delet Internal-1 marks.\nPress 2 to delet Internal-2 marks.\nPress 3 to delet Internal-3 marks.")
			if inter_ch=='1':
				with open("sub2_internal1.txt",'r') as inter1_file:
					inter1_data=inter1_file.readlines()
					for info in inter1_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter1_index=inter1_data.index(info)
							inter1_data.pop(inter1_index)
							with open("sub2_internal1.txt",'w') as inter1_file:
								for k in inter1_data:
									inter1_file.write(k)
				print("Deleted successfully")
			elif inter_ch=='2':
				with open("sub2_internal2.txt",'r') as inter1_file:
					inter2_data=inter1_file.readlines()
					for info in inter2_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter2_index=inter2_data.index(info)
							inter2_data.pop(inter2_index)
							with open("sub2_internal2.txt",'w') as inter2_file:
								for k in inter2_data:
									inter2_file.write(k)
				print("Deleted successfully")
			elif inter_ch=='3':
				with open("sub2_internal3.txt",'r') as inter3_file:
					inter3_data=inter3_file.readlines()
					for info in inter3_data:
						info=info.replace('\n','')
						dat_1=info.split(',')
						if st_choice in dat_1:
							info+='\n'
							inter2_index=inter3_data.index(info)
							inter3_data.pop(inter2_index)
							with open("sub2_internal3.txt",'w') as inter3_file:
								for k in inter3_data:
									inter3_file.write(k)
				print("Deleted successfully")
	else:
		print("Student name not found.Enter Valid name")



	



							







	


		





