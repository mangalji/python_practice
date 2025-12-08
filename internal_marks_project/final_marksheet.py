from internal_opt import student_name_list


def student_final_result_main():
	user_pick=input("Enter 1 to generate marksheet.\nEnter 2 to show marksheet.")
	if user_pick=='1':
		final_percentage_generator()
	elif user_pick=='2':
		show_marksheet()
	else:
		print("Enter valid choice")
		student_final_result_main()


def final_percentage_generator():
	names=student_name_list()
	print(names)
	student_selection=input("Enter student name for final marksheet genertion: ")
	s1_first_internal_marks=0
	s1_second_internal_marks=0
	s1_third_internal_marks=0
	s2_first_internal_marks=0
	s2_second_internal_marks=0
	s2_third_internal_marks=0
	student_real_name=""
	sub1_marks_list=[]
	sub2_marks_list=[]
	


	if student_selection in names:
		#subject-1 internals
		with open("sub1_internal1.txt",'r') as inter1_file:
			inter1_data=inter1_file.readlines()
			for info in inter1_data:
				info=info.replace('\n','')
				dat_1=info.split(',')
				if student_selection in dat_1:
					a=dat_1[1]
					s1_first_internal_marks=int(a)


		with open("sub1_internal2.txt",'r') as inter2_file:
			inter2_data=inter2_file.readlines()
			for info1 in inter2_data:
				info1=info1.replace('\n','')
				dat_2=info1.split(',')
				if student_selection in dat_2:
					b=dat_2[1]
					s1_second_internal_marks=int(b)



		with open("sub1_internal3.txt",'r') as inter3_file:
			inter2_data=inter3_file.readlines()
			for info3 in inter2_data:
				info3=info3.replace('\n','')
				dat_3=info3.split(',')
				if student_selection in dat_3:
					c=dat_3[1]
					s1_third_internal_marks=int(c)


		#Subject-2 Internals
		with open("sub2_internal1.txt",'r') as inter1_file:
			inter1_data=inter1_file.readlines()
			for ito in inter1_data:
				ito=ito.replace('\n','')
				dat_4=ito.split(',')
				if student_selection in dat_4:
					d=dat_4[1]
					s2_first_internal_marks=int(d)


		with open("sub2_internal2.txt",'r') as inter2_file:
			inter2_data=inter2_file.readlines()
			for op in inter2_data:
				op=op.replace('\n','')
				dat_5=op.split(',')
				if student_selection in dat_5:
					e=dat_5[1]
					s2_second_internal_marks=int(e)



		with open("sub2_internal3.txt",'r') as inter3_file:
			inter2_data=inter3_file.readlines()
			for fp in inter2_data:
				fp=fp.replace('\n','')
				dat_3=fp.split(',')
				if student_selection in dat_3:
					f=dat_3[1]
					s2_third_internal_marks=int(f)
		with open("marksheet.txt",'r') as file1:
			m_data=file1.readlines()
			for iop in m_data:
				iop=iop.replace('\n','')
				dat_5=iop.split(',')
				if student_selection in dat_5:
					u=dat_5[0]
					student_real_name=u

		sub1_marks_list=[s1_first_internal_marks,s1_second_internal_marks,s1_third_internal_marks]
		sub2_marks_list=[s2_first_internal_marks,s2_second_internal_marks,s2_third_internal_marks]
		sub1_marks_list.sort(reverse=True)
		sub2_marks_list.sort(reverse=True)
		sub1_marks_total=sub1_marks_list[0]+sub1_marks_list[1]
		sub2_marks_total=sub2_marks_list[0]+sub2_marks_list[1]
		sub1_and_sub2_total=sub1_marks_total+sub2_marks_total
		st_percentage=(sub1_and_sub2_total/80)*100
		
		st_grade=grade_generator(st_percentage)
		marksheet_str=f"{student_real_name},{sub1_marks_total},{sub2_marks_total},{sub1_and_sub2_total},{st_percentage},{st_grade}\n"
		with open('marksheet.txt','a') as marksheet_file:
			marksheet_file.write(marksheet_str)
	else:
		print("Student name not found.")


def grade_generator(x):
	if 91<x<100:
		return 'A+'
	elif 81<x<90:
		return 'A'
	elif 71<x<80:
		return 'B+'
	elif 61<x<70:
		return 'B'
	elif 51<x<60:
		return 'C'
	else:
		return 'Fail'


def show_marksheet():
	names=student_name_list()
	print(names)
	student_selection=input("Enter student name for final marksheet genertion: ")
	if student_selection in names:
		with open("marksheet.txt",'r') as mark_file:
			marksheet_data=mark_file.readlines()
			for i in marksheet_data:
				i=i.replace('\n','')
				mark_st_list=i.split(',')
				if student_selection in mark_st_list:
					print("Name:",mark_st_list[1])
					print("Subject-1 Total:",mark_st_list[1])
					print("Subject-2 Total:",mark_st_list[2])
					print("Marks out of 80:",mark_st_list[3])
					print("Percentage Acquired:",mark_st_list[4])
					print("Grade:",mark_st_list[5])
	else:
		print("Student name not found")

	

		



