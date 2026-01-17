package main

import (
	"fmt"
	"math"
)

func secondLargest(arr []int) int {
	firstLargest := math.MinInt
	secondLargest := math.MinInt

	for _, val := range arr {
		if val > firstLargest {
			secondLargest = firstLargest
			firstLargest = val
		} else if val > secondLargest {
			secondLargest = val
		}
	}
	return secondLargest

}

func main() {
	arr := []int{-3, 9, 7, 8, 5, 14, 16}
	fmt.Println(secondLargest(arr))
}
