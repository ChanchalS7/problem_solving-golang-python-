# Problem Statements & Solutions

This document contains detailed problem statements, examples, and solution approaches for all solved problems.

## Table of Contents
- [Count Negative Numbers](#1-count-negative-numbers)
- [Search Element](#2-search-element)

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

**Note:** For each new problem, add it to this document with the same format. Update the Table of Contents with links for easy navigation.
