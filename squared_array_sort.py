# arr = [-4,5,1,0,-3,10]
arr = [0,2,9,8,-6,-7,4,-3,2]

def merge_sort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	return merge(left,right)

def merge(left,right):
	result = []
	i = j = 0

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

arr = merge_sort(arr)

n = len(arr)

result_arr = [0]*n
left = 0
right = n - 1
position = n - 1

while left <= right:
	if arr[left]**2 > arr[right]**2:
		result_arr[position] = arr[left]**2
		left += 1
	else:
		result_arr[position] = arr[right]**2
		right -= 1
	position -= 1

print(result_arr)
