def secondLargest(arr :list[int]) -> int:
	firstLargest = float('-inf')
	secondLargest = float('-inf')

	for i in range(len(arr)):
		if arr[i] > firstLargest:
			secondLargest= firstLargest
			firstLargest = arr[i]

		elif arr[i] > secondLargest:
			secondLargest = arr[i]

	return secondLargest

arr = [-3, 9, 7, 8, 5, 14, 16]
print(secondLargest(arr))    			