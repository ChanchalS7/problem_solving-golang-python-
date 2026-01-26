# Time & Space Complexity Guide

A comprehensive guide to understanding **Time Complexity** and **Space Complexity** in algorithms — essential concepts for writing efficient code.

---

## 📚 Table of Contents

- [What is Time Complexity?](#what-is-time-complexity)
- [What is Space Complexity?](#what-is-space-complexity)
- [Big-O Notation](#big-o-notation)
- [Common Time Complexities](#common-time-complexities)
- [Common Space Complexities](#common-space-complexities)
- [How to Analyze Complexity](#how-to-analyze-complexity)
- [Visual Comparison Chart](#visual-comparison-chart)
- [Real-World Algorithm Examples](#real-world-algorithm-examples)
- [Tips for Optimization](#tips-for-optimization)
- [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## What is Time Complexity?

**Time Complexity** measures how the **runtime** of an algorithm grows as the input size increases.

It answers the question: *"How much longer will my algorithm take if I double the input size?"*

### Key Points:
- We measure the **number of operations**, not actual time (seconds)
- We focus on the **worst-case scenario** (unless specified otherwise)
- We care about **growth rate** as input becomes very large

### Diagram: Time vs Input Size

```
Runtime
   ▲
   │                                          ╱ O(n²)
   │                                        ╱
   │                                      ╱
   │                                   ╱
   │                               ╱
   │                          ╱        _____ O(n log n)
   │                     ╱     _______
   │               ╱  _______            _____ O(n)
   │          ╱ ____                ____
   │     ╱____               ______
   │ ____           _________           _____ O(log n)
   │___________________________________________O(1)
   └──────────────────────────────────────────▶ Input Size (n)
```

---

## What is Space Complexity?

**Space Complexity** measures how much **extra memory** an algorithm uses as input size grows.

It answers the question: *"How much additional memory does my algorithm need?"*

### Key Points:
- We measure **auxiliary space** (extra space beyond input)
- Input space is sometimes included (total space complexity)
- In-place algorithms have O(1) auxiliary space

### Diagram: Memory Allocation

```
┌─────────────────────────────────────────────────┐
│                  MEMORY                          │
├─────────────────────────────────────────────────┤
│  ┌───────────────┐  ┌─────────────────────────┐ │
│  │ Input Array   │  │  Auxiliary/Extra Space  │ │
│  │    O(n)       │  │     (what we count)     │ │
│  │               │  │                         │ │
│  │ [1,2,3,4,5]   │  │  variables, temp arrays │ │
│  └───────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

---

## Big-O Notation

**Big-O** describes the **upper bound** of an algorithm's growth rate.

### Common Notations:

| Notation     | Name           | Description                              |
|--------------|----------------|------------------------------------------|
| O(1)         | Constant       | Same time regardless of input size       |
| O(log n)     | Logarithmic    | Halves the problem each step             |
| O(n)         | Linear         | Grows proportionally with input          |
| O(n log n)   | Linearithmic   | Slightly worse than linear               |
| O(n²)        | Quadratic      | Nested loops over input                  |
| O(n³)        | Cubic          | Triple nested loops                      |
| O(2ⁿ)        | Exponential    | Doubles with each additional input       |
| O(n!)        | Factorial      | All permutations                         |

### Other Notations:

| Notation | Meaning                              |
|----------|--------------------------------------|
| Ω (Omega)| Lower bound (best case)              |
| Θ (Theta)| Tight bound (average case)           |
| O (Big-O)| Upper bound (worst case) — most used |

---

## Common Time Complexities

### O(1) — Constant Time

```
Operation count stays the same regardless of input size.
```

**Examples:**
- Array access by index: `arr[5]`
- Hash table lookup (average)
- Push/pop from stack

```
Input Size:    10      100      1000     10000
Operations:     1        1         1         1
                ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
```

**Code Example (Go):**
```go
func getFirst(arr []int) int {
    return arr[0]  // Always 1 operation
}
```

---

### O(log n) — Logarithmic Time

```
Problem size is halved each iteration.
```

**Examples:**
- Binary search
- Finding element in balanced BST
- Exponentiation by squaring

```
Input Size:    10      100      1000     10000
Operations:     3        7        10        13
                ▬▬▬      ▬▬▬▬▬▬▬  ▬▬▬▬▬▬▬▬▬▬ ▬▬▬▬▬▬▬▬▬▬▬▬▬
```

**Visual: How Binary Search Halves**
```
Array: [1, 3, 5, 7, 9, 11, 13, 15]   Target: 11

Step 1: [1, 3, 5, 7, 9, 11, 13, 15]
                  ▲ mid=7, 11>7, go right

Step 2:          [9, 11, 13, 15]
                      ▲ mid=11, FOUND!

Only 2 steps for 8 elements! log₂(8) = 3 max steps
```

**Code Example (Go):**
```go
func binarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1
    for left <= right {
        mid := (left + right) / 2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}
```

---

### O(n) — Linear Time

```
Operations grow directly proportional to input size.
```

**Examples:**
- Iterating through an array once
- Finding max/min element
- Linear search

```
Input Size:    10      100      1000     10000
Operations:    10      100      1000     10000
               ▬▬▬▬▬▬▬▬▬▬
                        ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
```

**Code Example (Go):**
```go
func findMax(arr []int) int {
    max := arr[0]
    for _, val := range arr {  // n iterations
        if val > max {
            max = val
        }
    }
    return max
}
```

---

### O(n log n) — Linearithmic Time

```
Slightly worse than linear, but much better than quadratic.
```

**Examples:**
- Merge sort
- Quick sort (average case)
- Heap sort

```
Input Size:    10      100      1000     10000
Operations:    33      664      9966    132877
```

**Visual: Merge Sort Divide & Conquer**
```
Level 0:    [8, 4, 2, 6, 5, 1, 7, 3]        → n operations to merge
                    /            \
Level 1:    [8, 4, 2, 6]    [5, 1, 7, 3]    → n operations to merge
              /      \        /      \
Level 2:  [8,4]    [2,6]  [5,1]    [7,3]    → n operations to merge
           / \      / \    / \      / \
Level 3: [8] [4]  [2] [6] [5] [1]  [7] [3]  → n operations to merge

log₂(n) levels × n operations per level = O(n log n)
```

---

### O(n²) — Quadratic Time

```
Operations grow as the square of input size.
```

**Examples:**
- Nested loops over same array
- Bubble sort
- Selection sort
- Insertion sort

```
Input Size:    10      100      1000     10000
Operations:   100    10000   1000000  100000000
```

**Visual: Why Nested Loops = n²**
```
for i in range(n):        ─┐
    for j in range(n):     │ n × n = n²
        operation          │
                          ─┘

    j→  0   1   2   3   4
i ┌───┬───┬───┬───┬───┐
↓ │ x │ x │ x │ x │ x │  ← 5 operations
0 ├───┼───┼───┼───┼───┤
  │ x │ x │ x │ x │ x │  ← 5 operations
1 ├───┼───┼───┼───┼───┤
  │ x │ x │ x │ x │ x │  ← 5 operations
2 ├───┼───┼───┼───┼───┤
  │ x │ x │ x │ x │ x │  ← 5 operations
3 ├───┼───┼───┼───┼───┤
  │ x │ x │ x │ x │ x │  ← 5 operations
4 └───┴───┴───┴───┴───┘
        Total: 5 × 5 = 25 = n²
```

**Code Example (Go):**
```go
func bubbleSort(arr []int) {
    n := len(arr)
    for i := 0; i < n; i++ {           // n times
        for j := 0; j < n-i-1; j++ {   // n times (roughly)
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
}
```

---

### O(2ⁿ) — Exponential Time

```
Operations double with each additional input element.
```

**Examples:**
- Recursive Fibonacci (naive)
- Power set generation
- Traveling salesman (brute force)

```
Input Size:    10      20       30        40
Operations:  1024   1048576  ~1 billion  ~1 trillion
```

**Visual: Fibonacci Recursion Tree**
```
                        fib(5)
                       /      \
                   fib(4)      fib(3)
                  /    \       /    \
              fib(3)  fib(2) fib(2) fib(1)
              /   \
          fib(2) fib(1)

Each level doubles the calls → 2ⁿ total calls
```

---

## Common Space Complexities

### O(1) — Constant Space

```go
func sum(arr []int) int {
    total := 0           // Just one variable
    for _, v := range arr {
        total += v
    }
    return total
}
// Space: O(1) - only 'total' variable, regardless of input size
```

### O(n) — Linear Space

```go
func duplicate(arr []int) []int {
    result := make([]int, len(arr))  // New array of size n
    for i, v := range arr {
        result[i] = v
    }
    return result
}
// Space: O(n) - result array grows with input
```

### O(n²) — Quadratic Space

```go
func createMatrix(n int) [][]int {
    matrix := make([][]int, n)
    for i := 0; i < n; i++ {
        matrix[i] = make([]int, n)  // n arrays of size n
    }
    return matrix
}
// Space: O(n²) - n×n matrix
```

---

## How to Analyze Complexity

### Step-by-Step Guide:

```
┌─────────────────────────────────────────────────────────────┐
│  1. IDENTIFY THE INPUT                                       │
│     What is 'n'? (array length, string length, etc.)        │
├─────────────────────────────────────────────────────────────┤
│  2. COUNT THE OPERATIONS                                     │
│     - Single operation = O(1)                                │
│     - Loop from 0 to n = O(n)                               │
│     - Nested loops = multiply their complexities            │
│     - Recursive calls = count total calls                   │
├─────────────────────────────────────────────────────────────┤
│  3. FIND THE DOMINANT TERM                                   │
│     O(n² + n + 1) → O(n²)  (drop lower terms)               │
│     O(3n) → O(n)           (drop constants)                 │
├─────────────────────────────────────────────────────────────┤
│  4. IDENTIFY SPACE USAGE                                     │
│     - Count extra variables = O(1)                          │
│     - New array of size n = O(n)                            │
│     - Recursive call stack = O(depth)                       │
└─────────────────────────────────────────────────────────────┘
```

### Example Analysis:

```go
func example(arr []int) int {
    n := len(arr)               // O(1)
    sum := 0                    // O(1)
    
    for i := 0; i < n; i++ {    // O(n)
        sum += arr[i]           //   └─ O(1) per iteration
    }
    
    for i := 0; i < n; i++ {    // O(n)
        for j := 0; j < n; j++ {//   └─ O(n) per iteration
            sum += arr[i]*arr[j]//       └─ O(1)
        }
    }
    
    return sum                  // O(1)
}

// Time:  O(1) + O(1) + O(n) + O(n²) + O(1)
//      = O(n²)  ← dominant term
//
// Space: O(1)  ← only using n, sum, i, j (constant)
```

---

## Visual Comparison Chart

### Time Complexity Growth (for n = 1000):

```
O(1)        │▌                                              1
O(log n)    │▌▌                                            10
O(n)        │████████████████████                       1,000
O(n log n)  │████████████████████████████████████      10,000
O(n²)       │█████████████████████████████████...  1,000,000
O(2ⁿ)       │ OVERFLOW - astronomically large
```

### Practical Time Limits:

```
┌────────────┬─────────────┬───────────────────────────────┐
│ Complexity │ Max n       │ Typical Use Case              │
├────────────┼─────────────┼───────────────────────────────┤
│ O(n!)      │ ≤ 10        │ Permutations, brute force     │
│ O(2ⁿ)      │ ≤ 20-25     │ Subsets, recursive backtrack  │
│ O(n³)      │ ≤ 500       │ Floyd-Warshall, 3D DP         │
│ O(n²)      │ ≤ 5,000     │ Simple DP, brute comparisons  │
│ O(n log n) │ ≤ 1,000,000 │ Sorting, divide & conquer     │
│ O(n)       │ ≤ 10⁸       │ Single pass, linear scan      │
│ O(log n)   │ ≤ 10¹⁸      │ Binary search, exponentiation │
│ O(1)       │ Any         │ Math formula, hash lookup     │
└────────────┴─────────────┴───────────────────────────────┘
```

---

## Real-World Algorithm Examples

### Example 1: Array Sum — O(n) Time, O(1) Space

```
Problem: Calculate the sum of all elements in an array
Approach: Single pass through array

total = 0
for each element:          ─┐
    total += element        │  n iterations
                           ─┘

Time:  O(n) - one loop through all elements
Space: O(1) - just a single accumulator variable
```

**Code:**
```go
func arraySum(arr []int) int {
    total := 0
    for _, v := range arr {
        total += v
    }
    return total
}
```

### Example 2: Two Sum (Brute Force) — O(n²) Time, O(1) Space

```
Problem: Find two numbers that add up to target
Approach: Check every pair of elements

for i in range(n):         ─┐
    for j in range(i+1, n): │  n × n iterations
        if arr[i]+arr[j]==t │
            return (i, j)  ─┘

Time:  O(n²) - nested loops checking all pairs
Space: O(1) - only index variables
```

**Code:**
```go
func twoSumBruteForce(arr []int, target int) (int, int) {
    n := len(arr)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if arr[i]+arr[j] == target {
                return i, j
            }
        }
    }
    return -1, -1
}
```

### Example 3: Two Sum (Optimized) — O(n) Time, O(n) Space

```
Problem: Same as above, but optimized with hash map
Approach: Store seen values in a map

map = {}
for i, val in array:       ─┐
    complement = target-val │
    if complement in map:   │  n iterations
        return result       │
    map[val] = i           ─┘

Time:  O(n) - single pass with O(1) hash lookups
Space: O(n) - hash map stores up to n elements
```

**Code:**
```go
func twoSumOptimized(arr []int, target int) (int, int) {
    seen := make(map[int]int)
    for i, val := range arr {
        complement := target - val
        if j, exists := seen[complement]; exists {
            return j, i
        }
        seen[val] = i
    }
    return -1, -1
}
```

### Example 4: Binary Search — O(log n) Time, O(1) Space

```
Problem: Find target in sorted array
Approach: Eliminate half of remaining elements each step

left, right = 0, n-1
while left <= right:       ─┐
    mid = (left+right)/2    │  log₂(n) iterations
    if arr[mid] == target:  │
        return mid          │
    elif arr[mid] < target: │
        left = mid + 1      │
    else:                   │
        right = mid - 1    ─┘

Time:  O(log n) - halves search space each iteration
Space: O(1) - only three pointer variables
```

### Example 5: Merge Sort — O(n log n) Time, O(n) Space

```
Problem: Sort an array
Approach: Divide and conquer with merging

┌────────────────────────────────────────────┐
│  divide array into halves  → log n levels  │
│  merge sorted halves       → n work/level  │
│                                            │
│  Total: O(n) × O(log n) = O(n log n)       │
└────────────────────────────────────────────┘

Time:  O(n log n) - divide (log n) × merge (n)
Space: O(n) - temporary arrays for merging
```

### Example 6: Fibonacci (Naive Recursive) — O(2ⁿ) Time, O(n) Space

```
Problem: Calculate nth Fibonacci number
Approach: Recursive calls without memoization

fib(n) = fib(n-1) + fib(n-2)

                fib(5)
               /      \
           fib(4)    fib(3)    ← Same subproblems
          /    \      /    \      recalculated!
       fib(3) fib(2) fib(2) fib(1)

Time:  O(2ⁿ) - exponential recursive calls
Space: O(n) - recursion stack depth
```

### Example 7: Fibonacci (DP Optimized) — O(n) Time, O(1) Space

```
Problem: Same, but with dynamic programming
Approach: Track only previous two values

prev2, prev1 = 0, 1
for i in range(2, n+1):    ─┐
    current = prev1 + prev2 │  n iterations
    prev2 = prev1           │
    prev1 = current        ─┘

Time:  O(n) - single loop
Space: O(1) - only two/three variables
```

**Code:**
```go
func fibOptimized(n int) int {
    if n <= 1 {
        return n
    }
    prev2, prev1 := 0, 1
    for i := 2; i <= n; i++ {
        current := prev1 + prev2
        prev2 = prev1
        prev1 = current
    }
    return prev1
}
```

### Complexity Comparison Summary:

| Algorithm              | Time       | Space  | Trade-off                       |
|------------------------|------------|--------|----------------------------------|
| Array Sum              | O(n)       | O(1)   | Optimal                         |
| Two Sum (Brute)        | O(n²)      | O(1)   | Simple, slow                    |
| Two Sum (Hash)         | O(n)       | O(n)   | Fast, uses memory               |
| Binary Search          | O(log n)   | O(1)   | Requires sorted input           |
| Merge Sort             | O(n log n) | O(n)   | Stable, consistent              |
| Fibonacci (Naive)      | O(2ⁿ)      | O(n)   | Don't use this!                 |
| Fibonacci (DP)         | O(n)       | O(1)   | Optimal                         |

---

## Tips for Optimization

### Time Optimization:

```
┌─────────────────────────────────────────────────────────┐
│  1. AVOID NESTED LOOPS when possible                    │
│     O(n²) → O(n) using hash maps                        │
│                                                         │
│  2. USE BINARY SEARCH on sorted data                    │
│     O(n) → O(log n)                                     │
│                                                         │
│  3. PRECOMPUTE values you'll use repeatedly             │
│     Calculate once, use many times                      │
│                                                         │
│  4. CHOOSE RIGHT DATA STRUCTURE                         │
│     Array lookup: O(1)                                  │
│     Hash map lookup: O(1) average                       │
│     Tree search: O(log n)                               │
│                                                         │
│  5. USE DYNAMIC PROGRAMMING                             │
│     Avoid recalculating same subproblems                │
└─────────────────────────────────────────────────────────┘
```

### Space Optimization:

```
┌─────────────────────────────────────────────────────────┐
│  1. MODIFY IN-PLACE when possible                       │
│     Don't create new arrays                             │
│                                                         │
│  2. USE VARIABLES instead of arrays for tracking        │
│     prev, curr instead of dp[]                          │
│                                                         │
│  3. PROCESS STREAMING data                              │
│     Don't store what you don't need                     │
│                                                         │
│  4. REUSE MEMORY                                        │
│     Clear and reuse instead of reallocating             │
└─────────────────────────────────────────────────────────┘
```

---

## Quick Reference Cheat Sheet

```
╔═══════════════════════════════════════════════════════════════╗
║                 TIME COMPLEXITY CHEAT SHEET                   ║
╠═══════════════════════════════════════════════════════════════╣
║  O(1)       │ Hash lookup, array access, math operations      ║
║  O(log n)   │ Binary search, balanced tree operations         ║
║  O(n)       │ Linear search, single loop, array traversal     ║
║  O(n log n) │ Efficient sorts (merge, quick, heap)            ║
║  O(n²)      │ Nested loops, simple sorts (bubble, insertion)  ║
║  O(2ⁿ)      │ Recursive subsets, naive Fibonacci              ║
║  O(n!)      │ Permutations, traveling salesman brute force    ║
╠═══════════════════════════════════════════════════════════════╣
║                 SPACE COMPLEXITY CHEAT SHEET                  ║
╠═══════════════════════════════════════════════════════════════╣
║  O(1)       │ Fixed variables, in-place algorithms            ║
║  O(log n)   │ Recursive call stack (balanced recursion)       ║
║  O(n)       │ Linear data structures, 1D DP arrays            ║
║  O(n²)      │ 2D matrices, adjacency matrix                   ║
╠═══════════════════════════════════════════════════════════════╣
║                      QUICK RULES                              ║
╠═══════════════════════════════════════════════════════════════╣
║  • Drop constants: O(3n) → O(n)                               ║
║  • Drop lower terms: O(n² + n) → O(n²)                        ║
║  • Nested loops multiply: O(n) × O(m) = O(n×m)                ║
║  • Sequential code adds: O(n) + O(m) = O(n+m)                 ║
║  • Recursive: count calls × work per call                     ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Further Reading

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualizing Algorithms](https://visualgo.net/)
- [MIT OpenCourseWare - Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)

---

**Last Updated:** January 25, 2026
