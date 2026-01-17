def searchElement(arr:list[int],x:int)->int:
	for i in range(len(arr)):
		if arr[i]==x:
			return i
		
	return -1

arr=[2, 4, 6, 8, 7, 10, 9, 5]
x = 10	
print(searchElement(arr,x))