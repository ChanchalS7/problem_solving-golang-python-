package main

import (
	"fmt"
	"strings"
)

// Pattern 1: Square of stars (5x5)
func pattern1Square() {
	fmt.Println("Pattern 1: Square")
	n := 5

	for i := 0; i < n; i++ {
		bag := ""
		for j := 0; j < n; j++ {
			bag += "* "
		}
		fmt.Println(strings.TrimSpace(bag))
	}
	fmt.Println()
}

// Pattern 2: Descending right triangle
func pattern2DescendingTriangle() {
	fmt.Println("Pattern 2: Descending Triangle")
	n := 4

	for i := n; i >= 1; i-- {
		bag := ""
		for j := 1; j <= i; j++ {
			bag += "* "
		}
		fmt.Println(strings.TrimSpace(bag))
	}
	fmt.Println()
}

// Pattern 3: Ascending right-aligned triangle
func pattern3AscendingRightTriangle() {
	fmt.Println("Pattern 3: Ascending Right-Aligned Triangle")
	n := 5

	for i := 1; i <= n; i++ {
		bag := ""

		// leading spaces (to push stars to the right)
		for s := 1; s <= n-i; s++ {
			bag += "  " // two spaces to match "* "
		}

		// stars
		for j := 1; j <= i; j++ {
			bag += "* "
		}

		fmt.Println(strings.TrimRight(bag, " "))
	}
	fmt.Println()
}

// Pattern 4: Ascending right-aligned triangle (compact)
func pattern4AscendingTriangleCompact() {
	fmt.Println("Pattern 4: Ascending Triangle (Compact)")
	n := 5

	for i := 1; i <= n; i++ {
		bag := ""

		// leading spaces
		for s := 1; s <= n-i; s++ {
			bag += "  " // two spaces per missing star
		}

		// stars
		for j := 1; j <= i; j++ {
			bag += "*" // add star
			if j < i {
				bag += " " // add space only between stars
			}
		}

		fmt.Println(bag)
	}
	fmt.Println()
}

// Pattern 5: Number ascending triangle
func pattern5NumberAscending() {
	fmt.Println("Pattern 5: Number Ascending Triangle")
	n := 5

	for i := 1; i <= n; i++ {
		bag := ""

		for j := 1; j <= i; j++ {
			bag += fmt.Sprintf("%d", j) // add the number
			if j < i {
				bag += " " // space between numbers
			}
		}

		fmt.Println(bag)
	}
	fmt.Println()
}

// Pattern 6: Number descending triangle
func pattern6NumberDescending() {
	fmt.Println("Pattern 6: Number Descending Triangle")
	n := 5

	for i := n; i >= 1; i-- {
		bag := ""

		for j := 1; j <= i; j++ {
			bag += fmt.Sprintf("%d", j) // add the number
			if j < i {
				bag += " " // space between numbers
			}
		}

		fmt.Println(bag)
	}
	fmt.Println()
}

// Pattern 7: Binary pattern (alternating by column)
func pattern7BinaryAlternateColumn() {
	fmt.Println("Pattern 7: Binary Pattern (Alternate by Column)")
	n := 5

	for i := 1; i <= n; i++ {
		bag := ""

		for j := 1; j <= i; j++ {
			// start every row with 1, then alternate 1,0,1,0,...
			var value int
			if j%2 == 1 {
				value = 1
			} else {
				value = 0
			}
			bag += fmt.Sprintf("%d", value)
			if j < i {
				bag += " "
			}
		}

		fmt.Println(bag)
	}
	fmt.Println()
}

// Pattern 8: Binary pattern (alternating by diagonal)
func pattern8BinaryAlternateDiagonal() {
	fmt.Println("Pattern 8: Binary Pattern (Alternate by Diagonal)")
	n := 5

	for i := 1; i <= n; i++ {
		bag := ""

		for j := 1; j <= i; j++ {
			// value depends on (i + j): this matches the second pattern
			var value int
			if (i+j)%2 == 0 {
				value = 1
			} else {
				value = 0
			}
			bag += fmt.Sprintf("%d", value)
			if j < i {
				bag += " "
			}
		}

		fmt.Println(bag)
	}
	fmt.Println()
}

func main() {
	fmt.Println(strings.Repeat("=", 50))
	fmt.Println("         PATTERN PRINTING PROGRAMS")
	fmt.Println(strings.Repeat("=", 50))
	fmt.Println()

	pattern1Square()
	pattern2DescendingTriangle()
	pattern3AscendingRightTriangle()
	pattern4AscendingTriangleCompact()
	pattern5NumberAscending()
	pattern6NumberDescending()
	pattern7BinaryAlternateColumn()
	pattern8BinaryAlternateDiagonal()

	fmt.Println(strings.Repeat("=", 50))
}
