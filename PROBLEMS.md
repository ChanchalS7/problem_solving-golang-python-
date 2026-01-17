# Problem Statements & Solutions

This document contains detailed problem statements, examples, and solution approaches for all solved problems.

## Table of Contents
- [Count Negative Numbers](#1-count-negative-numbers)
- [Search Element](#2-search-element)
- [Find Smallest and Largest](#3-find-smallest-and-largest)
- [Second Largest Element](#4-second-largest-element)

---

## 1. Count Negative Numbers

**Difficulty:** Easy  
**Category:** Arrays & Iteration  
**Date Solved:** 2026-01-17

### Problem Statement
Given an array of integers, count and return the total number of negative numbers in the array.

### Examples

**Example 1:**
```
Input: [2, 3, -1, -5, -6, 7, -8, -4, 9]
Output: 5
Explanation: There are 5 negative numbers: -1, -5, -6, -8, -4
```

### Approach
- Iterate through the array
- Count elements less than 0
- Return the count

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only using a counter variable

### Solutions
- ✅ **Python:** [`python/count-negative/count-negative.py`](python/count-negative/count-negative.py)
- ✅ **Go:** [`golang/count-negative/main.go`](golang/count-negative/main.go)

---

## 2. Search Element

**Difficulty:** Easy  
**Category:** Arrays & Searching  
**Date Solved:** 2026-01-17

### Problem Statement
Given an array of integers and a target element, find and return the index of the target element in the array. If the element is not found, return -1.

### Examples

**Example 1:**
```
Input: arr = [2, 4, 6, 8, 7, 10, 9, 5], x = 10
Output: 5
Explanation: Element 10 is found at index 5
```

**Example 2:**
```
Input: arr = [1, 2, 3, 4, 5], x = 6
Output: -1
Explanation: Element 6 is not in the array
```

### Approach
- Linear search through the array
- Return index when element is found
- Return -1 if not found

### Complexity Analysis
- **Time Complexity:** O(n) - Worst case: search entire array
- **Space Complexity:** O(1) - No extra space used

### Solutions
- ✅ **Python:** [`python/search-element/search-element.py`](python/search-element/search-element.py)
- ✅ **Go:** [`golang/search-element/main.go`](golang/search-element/main.go)

---

## 3. Find Smallest and Largest

**Difficulty:** Easy  
**Category:** Arrays & Iteration  
**Date Solved:** 2026-01-17

### Problem Statement
Given an array of integers, find and return both the smallest and largest elements in the array.

### Examples

**Example 1:**
```
Input: [-3, 9, 7, 8, 5, 14, 16]
Output: {"smallest": -3, "largest": 16}
Explanation: -3 is the smallest element and 16 is the largest element
```

**Example 2:**
```
Input: [5]
Output: {"smallest": 5, "largest": 5}
Explanation: In a single element array, both min and max are the same element
```

### Approach
- Initialize smallest to positive infinity and largest to negative infinity
- Iterate through the array
- Update smallest if current element is smaller
- Update largest if current element is larger
- Return both values

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only using two variables

### Solutions
- ✅ **Python:** [`python/smallest-largest/smallest-largest.py`](python/smallest-largest/smallest-largest.py)
- ✅ **Go:** [`golang/largest-smallest/main.go`](golang/largest-smallest/main.go)

### Alternative Approaches
- Using built-in `min()` and `max()` functions (Python)
- Sorting the array and taking first and last elements (O(n log n))
- Using TypedDict for better type hints (Python)

---

## 4. Second Largest Element

**Difficulty:** Easy  
**Category:** Arrays & Iteration  
**Date Solved:** 2026-01-17

### Problem Statement
Given an array of integers, find and return the second largest element in the array.

### Examples

**Example 1:**
```
Input: [-3, 9, 7, 8, 5, 14, 16]
Output: 14
Explanation: 16 is the largest, 14 is the second largest
```

**Example 2:**
```
Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: 5 is the largest, 4 is the second largest
```

### Approach
- Initialize firstLargest and secondLargest to minimum possible value
- Iterate through the array:
  - If current element is greater than firstLargest:
    - Move firstLargest to secondLargest
    - Update firstLargest to current element
  - Else if current element is greater than secondLargest:
    - Update secondLargest to current element
- Return secondLargest

### Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only using two variables

### Solutions
- ✅ **Python:** [`python/second-largest/secondlargest.py`](python/second-largest/secondlargest.py)
- ✅ **Go:** [`golang/second-largest/main.go`](golang/second-largest/main.go)

### Alternative Approaches
- Sort array and return second element from end: O(n log n)
- Use set to remove duplicates, then sort: handles duplicate largest values
- Two-pass approach: find max, then find second max

---

**Note:** For each new problem, add it to this document with the same format. Update the Table of Contents with links for easy navigation.
