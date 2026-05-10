array = [0,2,9,8,-6,-7,4,-3,2]

def merge_sort(array):
	if len(array) <= 1:
		return array

	mid = len(array) // 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])

	return merge(left,right)

def merge(left,right):

	result = []
	i = 0
	j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while i < len(left):
		result.append(left[i])
		i += 1

	while j < len(right):
		result.append(right[j])
		j += 1
	return result

arr = merge_sort(array)

n = len(arr)
result = [0]*n
left = 0
right = n - 1
position = n -1

while left <= right:
	if arr[left]**2 > arr[right]**2:
		result[position] = arr[left]**2
		left += 1
	else:
		result[position] = arr[right]**2
		right -= 1
	position -= 1

arr = result

print(arr)
