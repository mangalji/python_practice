import random

input_number = int(input("enter the number which you guess: "))

number = random.randint(1,10)
if input_number == number:
	print(f"you won you guess the {input_number}, and it comes.")
else:
	print("sorry! you loss")