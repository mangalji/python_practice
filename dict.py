# nums = [2,2,1,1,1,1,5]
# nums = [3,2,2]
nums = [2,2,1,1,1,2,2,1,1]
def check(nums):
	dict_map = {}
	for n in nums:
		if n in dict_map.keys():
			dict_map[n] += 1
		else:
			dict_map[n] = 1
	
	for m,l in dict_map.items():
		if l > len(nums)/2:
			return m


print(check(nums))