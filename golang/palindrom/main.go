package main

import "fmt"

func isPalindromeNumber(n int) bool {
	if n < 0 {
		return false
	}
	original := n
	reverse := 0
	for n > 0 {
		rem := n % 10
		reverse = reverse*10 + rem
		n = n / 10

	}
	return reverse == original
}

func main() {
	n := 2552
	fmt.Println(isPalindromeNumber(n))
}
