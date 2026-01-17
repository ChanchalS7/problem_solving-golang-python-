package main

import "fmt"

func countNegatives(arr []int) int {
	count := 0

	for _, val := range arr {
		if val < 0 {
			count++
		}
	}
	return count
}

func main() {
	arr := []int{2, 3, -1, -5, -6, 7, -8, -4, 9}
	fmt.Println(countNegatives(arr))
}
