def countDigit(n:int) -> int:
	if n == 0:
		return 1
	
	n = abs(n) #handle negatives

	count = 0

	while n > 0:
		n //= 10
		count +=1


	return count 

n = 259
print(countDigit(n))	
	