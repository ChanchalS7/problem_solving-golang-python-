def smallestLargest(arr:list[int]) -> dict[str,int]:
	smallest = float('inf')
	largest = float('-inf')

	for i in range(len(arr)):
		if arr[i] > largest:
			largest = arr[i]
		if arr[i] < smallest:
			smallest = arr[i]

	ans = {"smallest":smallest, "largest":largest}
	return ans

arr = [-3, 9, 7, 8, 5, 14, 16]
print(smallestLargest(arr))			

# some alternative solutions :

"""
Alternative Solution 1: Using Built-in Functions
------------------------------------------------
def smallestLargest(arr: list[int]) -> dict[str, int]:
	return {
		"smallest": min(arr),
		"largest": max(arr)
	}

Time Complexity: O(n) - min() and max() both traverse the array
Space Complexity: O(1)
Pros: Clean, readable, Pythonic
Cons: Two passes through the array
"""

"""
Alternative Solution 2: Using Sorted Array
-------------------------------------------
def smallestLargest(arr: list[int]) -> dict[str, int]:
	sorted_arr = sorted(arr)
	return {
		"smallest": sorted_arr[0],
		"largest": sorted_arr[-1]
	}

Time Complexity: O(n log n) - due to sorting
Space Complexity: O(n) - creates new sorted array
Pros: Simple to understand
Cons: Less efficient than linear scan
"""

"""
Alternative Solution 3: Using reduce from functools
----------------------------------------------------
from functools import reduce

def smallestLargest(arr: list[int]) -> dict[str, int]:
	result = reduce(
		lambda acc, x: {
			"smallest": min(acc["smallest"], x),
			"largest": max(acc["largest"], x)
		},
		arr,
		{"smallest": float('inf'), "largest": float('-inf')}
	)
	return result

Time Complexity: O(n)
Space Complexity: O(1)
Pros: Functional programming approach
Cons: Less readable for beginners
"""

"""
Alternative Solution 4: List Comprehension with Single Pass
------------------------------------------------------------
def smallestLargest(arr: list[int]) -> dict[str, int]:
	smallest = largest = arr[0]
	for num in arr[1:]:
		smallest = min(smallest, num)
		largest = max(largest, num)
	return {"smallest": smallest, "largest": largest}

Time Complexity: O(n)
Space Complexity: O(1)
Pros: Clean and efficient, no float('inf') needed
Cons: Requires non-empty array
"""

"""
Alternative Solution 5: Using TypedDict for Better Type Hints
--------------------------------------------------------------
from typing import TypedDict

class MinMax(TypedDict):
    largest: int
    smallest: int

def smallest_largest(arr: list[int]) -> MinMax:
    return {"largest": max(arr), "smallest": min(arr)}

Time Complexity: O(n) - min() and max() both traverse the array
Space Complexity: O(1)
Pros: 
  - Strong type hints with TypedDict
  - IDE autocomplete support
  - Better documentation
  - Type checkers can validate dictionary structure
Cons: 
  - Requires Python 3.8+
  - Two passes through the array
  - Additional import and class definition
"""