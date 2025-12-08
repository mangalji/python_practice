from obfuscation import obfuscation_of_emails, deobfuscation_of_emails

def main():
	choice = input("press 1 for obfuscation email ids\npress 2 for deobfuscation email ids")

	if choice == '1':
		obfuscation_of_emails()

	elif choice == '2':
		deobfuscation_of_emails()

if __name__ == "__main__":
	main()

