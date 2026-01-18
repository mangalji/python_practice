def pop(stack):
	last_position = len(stack) - 1
	a = stack[last_position]
	stack.remove(a)
	print(stack)

def push(input_,stack):
	
	extra_position = len(stack)
	stack.insert(extra_position,input_)
	print(stack)


stack = [12,14,15,16,10]
print(stack)

choice = input("press 1 for pop\npress 2 for push\nplease enter your choice: ")

if choice == "1":
	pop(stack)

elif choice == "2":
	print(stack)
	b = input("enter your input: ")
	push(b,stack)

# print(stack)