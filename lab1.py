def linearSearch(var_list, item):
	exists = -1
	var_list.sort()
	for i in range(len(var_list)):
		if var_list[i] == item:
			exists = i
			break
	return exists

def binarySearch(var_list, item):
	first = 0
	last = len(var_list) - 1
	exists = -1
	var_list.sort()
	while first <= last and exists == -1:
		midpoint = (first + last) // 2		
		if var_list[midpoint] == item:
			exists = midpoint
		else:
			if item < var_list[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return exists

if __name__ == '__main__':
	print("Enter the array items separated by space \n")
	inparray = list(map(int, raw_input().split()))
	inparray.sort()
	print("Enter the item to search for \n")
	tosearch = int(input())

	print("Sorted array is:", inparray)
	#print("Number to search is:", tosearch)

	if(binarySearch(inparray, tosearch) == -1):
		print("Number not found in array")
	else:
		print("Number found at", binarySearch(inparray, tosearch), "position using binary search.")
		
	if(linearSearch(inparray, tosearch) == -1):
		print("Number not found in array")
	else:
		print("Number found at", linearSearch(inparray, tosearch), "position using linear search.")
