def isPalindromeNumber(n: int) -> bool:
	if n < 0:
		return False
	
	original = n 
	reverse = 0

	while n > 0:
		rem = n %10
		reverse = reverse * 10 + rem
		n //= 10

	return reverse == original

n = 2552
print(isPalindromeNumber(n))	