def countNegative(arr: list[int])->int:
	count=0
	for i in range(len(arr)):
		if arr[i]<0:
			count+=1

	return count 

arr=[2,3,-1,-5,-6,7,-8,-4,9]
print(countNegative(arr))