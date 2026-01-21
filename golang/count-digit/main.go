package main

import "fmt"

func countDigit(n int) int {

	if n == 0 {
		return 1
	}
	if n < 0 {
		n = -n
	}
	count := 0

	for n > 0 {
		n = n / 10
		count++
	}
	return count
}

func main() {
	n := 259
	fmt.Println(countDigit(n))
}
