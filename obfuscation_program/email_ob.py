from random import randint

file=open("file_a.txt",'r')
a_data=file.readlines()
file.close()


file1=open("file_b.txt",'r')
b_data=file1.readlines()
file1.close()



c_file=open("file_c.txt",'r')
c_data=c_file.readlines()
c_file.close()

def obf_dict_fun():
	obf_dict={}
	for i in range(len(b_data)):
		b_data[i]=b_data[i].strip()
		# value=randint(1000,2000)
		obf_dict[b_data[i]]=i
	return obf_dict

def deobf_dict_fun():
	deobf_dict={}
	for i in range(len(b_data)):
		b_data[i]=b_data[i].strip()
		# value=randint(1000,2000)
		deobf_dict[i]=b_data[i]
	return deobf_dict




def email_obfuscation():
	ans=obf_dict_fun()
	file=open("file_c.txt","a")

	for line in a_data:

		st_point1=line.find('at ')+len('at ')
		end_point1=line.find(' ',st_point1)
		first_id=line[st_point1:end_point1]

		st_point2=line.rfind('at ')+len('at ')
		end_point2=line.rfind('.',st_point2)
		second_id=line[st_point2:end_point2]
		
		if first_id in line:
			if first_id in b_data:
				new_value1=str(ans[first_id])
				line=line.replace(first_id,new_value1)
				file.write(line)

		if second_id in line:
			if second_id in b_data:
				new_value2=str(ans[second_id])
				line=line.replace(second_id,new_value2)
				file.write(line)			
	file.close()		


def email_deobfuscation():
	c_data_dict=deobf_dict_fun()
	d_file=open("D.txt",'a')
	for lin in c_data:
		st_point=lin.find('at ')+len('at ')
		end_point=lin.find(' ',st_point)
		first_id=lin[st_point:end_point]
		if first_id in lin:
			first_id=int(first_id)
			new_value1=c_data_dict[first_id]
			first_id=str(first_id)
			lin=lin[:st_point]+new_value1+lin[end_point:]
			d_file.write(lin)
	d_file.close()


