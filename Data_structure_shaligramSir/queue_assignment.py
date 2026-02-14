queue_lst = []

def insert(arr):
	front = 0
	rear = -1
	new_ele = 5

	rear = rear + (len(arr) + 1)

	arr[rear] = new_ele

	return arr[rear]

print(insert(queue_lst))
