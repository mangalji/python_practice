def dec_to_bin(n):
	if n == "0":
		return 0

	bin_num = ""
	while n > 0:
		bin_num = str(n%2) + bin_num
		n = n // 2

	return bin_num

def bin_to_dec(bin_num):
	dec = 0
	for b in bin_num:
		dec = dec * 2 + int(b)
	return dec


def main():
	choice = int(input("select your choice:\nfor decimal to bin enter 1\nfor bin to decimal enter 2\nPlease enter your choice: "))

	if choice == 1:
		decimal = int(input("enter the decimal number: "))
		print(dec_to_bin(decimal))

	elif choice == 2:
		bin_num = input("enter the binary number: ")
		print(bin_to_dec(bin_num))

	else:
		print("Invaid hoice!!!")

if __name__ == '__main__':
	main()