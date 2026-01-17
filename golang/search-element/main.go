package main

import "fmt"

func searchElement(arr []int, x int) int {

	for i, val := range arr {
		if val == x {
			return i
		}
	}

	return -1
}
func main() {
	arr := []int{3, 4, 5, 6, 7, 8, 9, 0, 1}
	x := 7
	fmt.Println(searchElement(arr, x))
}
