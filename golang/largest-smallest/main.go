package main

import (
	"fmt"
	"math"
)

type MinMax struct {
	Largest  int
	Smallest int
}

func smallestLargest(arr []int) MinMax {
	smallest := math.MaxInt
	largest := math.MinInt

	for i := 0; i < len(arr); i++ {
		if arr[i] > largest {
			largest = arr[i]
		}
		if arr[i] < smallest {
			smallest = arr[i]
		}
	}
	ans := MinMax{Largest: largest, Smallest: smallest}
	return ans
}

func main() {
	arr := []int{-3, 9, 7, 8, 5, 14, 16}
	fmt.Println(smallestLargest(arr))
}

/*
Alternative Solution: Using range with value iteration
-------------------------------------------------------
func smallestLargest(arr []int) MinMax {
    smallest := math.MaxInt
    largest := math.MinInt

    for _, val := range arr {
        if val > largest {
            largest = val
        }
        if val < smallest {
            smallest = val
        }
    }

    return MinMax{Largest: largest, Smallest: smallest}
}

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Only using two variables

Pros:
  - More idiomatic Go using range
  - Cleaner syntax, no index variable needed
  - Direct value access without array indexing
  - Same efficiency as index-based approach

Cons:
  - Cannot modify array elements (value is a copy)
  - No access to index if needed later

Note: This is the preferred Go style when you don't need the index
*/
