queue_lst = [1,2,3,4]

def insert(arr):
	front = 0
	rear = -1
	new_ele = 5

	# rear += (len(arr) + 1)
	arr += [None] 
	
	rear +=  len(arr) 
	arr[rear] = new_ele
	return arr

print(insert(queue_lst))


def delete(arr):
	front = 0
	rear = len(arr)

	ele = arr[front]

	for i in range(front+1,rear):
		arr[i-1] = arr[i]
	rear -= 1
	arr[-1] = None
	return f"item: {ele}, remain list: {arr}"

print(delete(queue_lst)) 