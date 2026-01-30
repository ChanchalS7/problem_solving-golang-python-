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

## 🎯 Understanding Through Real-Life Analogies

### O(1) — Constant Time: Like a Light Switch
```
Turning on a light takes the same time whether your house has 
1 room or 100 rooms. You just flip the switch!

🏠 1 room    → flip switch → 💡 instant
🏢 100 rooms → flip switch → 💡 instant

Real Examples:
• Looking up a contact by their saved position in your phone
• Opening a locker with its number
• Pressing elevator button for your floor
```

### O(log n) — Logarithmic Time: Like Finding a Word in Dictionary
```
When you search for "Python" in a dictionary:
1. Open middle → "M" — Python comes after M, ignore first half
2. Open middle of remaining → "R" — Python comes before R
3. Open middle of remaining → "P" — Getting close!
4. Found "Python"!

📖 1,000 pages → ~10 steps
📖 1,000,000 pages → ~20 steps

You HALVE the problem each time!
```

### O(n) — Linear Time: Like Reading a Book
```
To read a 100-page book, you read 100 pages.
To read a 500-page book, you read 500 pages.

📕 100 pages → 100 minutes (1 page/min)
📚 500 pages → 500 minutes

Time grows DIRECTLY with input size.
```

### O(n²) — Quadratic Time: Like Handshakes at a Party
```
If everyone at a party must shake hands with everyone else:

👥 5 people  → 10 handshakes  (5×4/2)
👥 10 people → 45 handshakes  (10×9/2)
👥 100 people → 4,950 handshakes!

Each new person shakes hands with ALL existing people.
```

### O(2ⁿ) — Exponential Time: Like the Rice & Chessboard Story
```
Legend: A king offered to pay with rice on a chessboard:
• Square 1: 1 grain
• Square 2: 2 grains
• Square 3: 4 grains
• ...doubling each square

🌾 Square 10: 512 grains
🌾 Square 20: 524,288 grains
🌾 Square 64: 9,223,372,036,854,775,808 grains!

This is why exponential algorithms become impossible quickly.
```

---

## 🧠 Mental Models for Quick Analysis

### The Loop Counting Method

```
┌──────────────────────────────────────────────────────────────┐
│  COUNT YOUR LOOPS - Quick Mental Calculation                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  No loops            → O(1)                                  │
│  1 loop (0 to n)     → O(n)                                  │
│  2 nested loops      → O(n²)                                 │
│  3 nested loops      → O(n³)                                 │
│  Loop halving        → O(log n)                              │
│  Loop + halving      → O(n log n)                            │
│                                                              │
│  EXAMPLE ANALYSIS:                                           │
│                                                              │
│  for i := 0; i < n; i++ {           ← 1 loop = O(n)         │
│      for j := 0; j < n; j++ {       ← nested = O(n²)        │
│          for k := 0; k < n; k++ {   ← triple = O(n³)        │
│              // operation                                    │
│          }                                                   │
│      }                                                       │
│  }                                                           │
└──────────────────────────────────────────────────────────────┘
```

### The "What Happens When Input Doubles?" Test

```
┌─────────────────────────────────────────────────────────────┐
│  If n doubles, how does time change?                        │
├─────────────────────────────────────────────────────────────┤
│  Stays same      → O(1)     constant                        │
│  Adds a step     → O(log n) logarithmic                     │
│  Doubles         → O(n)     linear                          │
│  Bit more than 2x→ O(n log n) linearithmic                  │
│  Quadruples (4x) → O(n²)    quadratic                       │
│  Squares itself  → O(2ⁿ)    exponential                     │
└─────────────────────────────────────────────────────────────┘

EXAMPLE:
If sorting 1000 items takes 1 second...
• O(n): 2000 items → ~2 seconds
• O(n²): 2000 items → ~4 seconds
• O(n log n): 2000 items → ~2.2 seconds
```

---

## 📊 Complexity Analysis by Code Pattern

### Pattern 1: Simple Iteration
```go
// O(n) Time, O(1) Space
for i := 0; i < n; i++ {
    // O(1) operation
}
```

### Pattern 2: Nested Loops (Same Range)
```go
// O(n²) Time, O(1) Space
for i := 0; i < n; i++ {
    for j := 0; j < n; j++ {
        // O(1) operation
    }
}
```

### Pattern 3: Nested Loops (Different Range)
```go
// O(n × m) Time, O(1) Space
for i := 0; i < n; i++ {
    for j := 0; j < m; j++ {
        // O(1) operation
    }
}
```

### Pattern 4: Loop with Halving
```go
// O(log n) Time, O(1) Space
for i := n; i > 0; i = i / 2 {
    // O(1) operation
}
```

### Pattern 5: Loop with Inner Halving
```go
// O(n log n) Time, O(1) Space
for i := 0; i < n; i++ {
    for j := n; j > 0; j = j / 2 {
        // O(1) operation
    }
}
```

### Pattern 6: Two Pointers
```go
// O(n) Time, O(1) Space
left, right := 0, n-1
for left < right {
    // O(1) operation
    left++   // or right--
}
```

### Pattern 7: Sliding Window
```go
// O(n) Time, O(1) Space
for right := 0; right < n; right++ {
    // expand window
    for /* window invalid */ {
        left++  // shrink window
    }
}
```

### Pattern 8: Recursive with Branching
```go
// O(2ⁿ) Time, O(n) Space (call stack)
func recursive(n int) int {
    if n <= 1 {
        return n
    }
    return recursive(n-1) + recursive(n-2)
}
```

### Pattern 9: Recursive with Single Branch
```go
// O(n) Time, O(n) Space (call stack)
func recursive(n int) int {
    if n <= 0 {
        return 0
    }
    return 1 + recursive(n-1)
}
```

### Pattern 10: Divide and Conquer
```go
// O(n log n) Time, O(n) Space
func divideConquer(arr []int) {
    if len(arr) <= 1 {
        return
    }
    mid := len(arr) / 2
    divideConquer(arr[:mid])   // log n levels
    divideConquer(arr[mid:])   // log n levels
    merge(arr)                  // O(n) work per level
}
```

---

## 🎓 Interview Tips & Common Questions

### How to Explain Complexity in Interviews

```
FORMULA FOR EXPLAINING:
"The time complexity is O(___) because [reason], 
and the space complexity is O(___) because [reason]."

GOOD ANSWER EXAMPLE:
"The time complexity is O(n) because we iterate through the array 
once, and each operation inside the loop is O(1). The space 
complexity is O(1) because we only use a constant number of 
variables regardless of input size."
```

### Common Interview Questions & Answers

**Q: "Can you optimize this O(n²) solution?"**
```
THINK ABOUT:
• Can I use a hash map? → Often reduces to O(n)
• Is the input sorted? → Binary search gives O(log n)
• Can I use two pointers? → Often O(n)
• Can I precompute something? → Trade space for time
```

**Q: "What's the trade-off between time and space?"**
```
ANSWER FRAMEWORK:
"We can often trade space for time. For example, using a hash map 
takes O(n) extra space but reduces time from O(n²) to O(n). 
The right choice depends on constraints - if memory is limited, 
we might accept slower time; if speed is critical, we use more space."
```

**Q: "Why is O(n log n) the best for comparison-based sorting?"**
```
ANSWER:
"Any comparison-based sorting algorithm must make at least 
log₂(n!) comparisons to distinguish between n! possible 
orderings. By Stirling's approximation, this is Ω(n log n). 
Therefore, O(n log n) is optimal for comparison sorts."
```

### Complexity of Common Operations

```
╔════════════════════════════════════════════════════════════════╗
║                    DATA STRUCTURE OPERATIONS                   ║
╠════════════════════════════════════════════════════════════════╣
║  ARRAY                                                         ║
║  ├─ Access by index      O(1)                                  ║
║  ├─ Search (unsorted)    O(n)                                  ║
║  ├─ Search (sorted)      O(log n) with binary search           ║
║  ├─ Insert at end        O(1) amortized                        ║
║  ├─ Insert at beginning  O(n)                                  ║
║  └─ Delete               O(n)                                  ║
╠════════════════════════════════════════════════════════════════╣
║  HASH MAP / HASH TABLE                                         ║
║  ├─ Access               O(1) average, O(n) worst              ║
║  ├─ Search               O(1) average, O(n) worst              ║
║  ├─ Insert               O(1) average, O(n) worst              ║
║  └─ Delete               O(1) average, O(n) worst              ║
╠════════════════════════════════════════════════════════════════╣
║  LINKED LIST                                                   ║
║  ├─ Access               O(n)                                  ║
║  ├─ Search               O(n)                                  ║
║  ├─ Insert at head       O(1)                                  ║
║  ├─ Insert at tail       O(1) with tail pointer, O(n) without  ║
║  └─ Delete               O(1) if node known, O(n) to find      ║
╠════════════════════════════════════════════════════════════════╣
║  BINARY SEARCH TREE (BALANCED)                                 ║
║  ├─ Access               O(log n)                              ║
║  ├─ Search               O(log n)                              ║
║  ├─ Insert               O(log n)                              ║
║  └─ Delete               O(log n)                              ║
╠════════════════════════════════════════════════════════════════╣
║  HEAP / PRIORITY QUEUE                                         ║
║  ├─ Find min/max         O(1)                                  ║
║  ├─ Insert               O(log n)                              ║
║  ├─ Delete min/max       O(log n)                              ║
║  └─ Build heap           O(n)                                  ║
╠════════════════════════════════════════════════════════════════╣
║  STACK / QUEUE                                                 ║
║  ├─ Push/Enqueue         O(1)                                  ║
║  ├─ Pop/Dequeue          O(1)                                  ║
║  └─ Peek                 O(1)                                  ║
╚════════════════════════════════════════════════════════════════╝
```

### Sorting Algorithm Comparison

```
╔══════════════════════════════════════════════════════════════════╗
║                    SORTING ALGORITHMS                            ║
╠════════════════╦═══════════╦═══════════╦═══════════╦═════════════╣
║ Algorithm      ║ Best      ║ Average   ║ Worst     ║ Space       ║
╠════════════════╬═══════════╬═══════════╬═══════════╬═════════════╣
║ Bubble Sort    ║ O(n)      ║ O(n²)     ║ O(n²)     ║ O(1)        ║
║ Selection Sort ║ O(n²)     ║ O(n²)     ║ O(n²)     ║ O(1)        ║
║ Insertion Sort ║ O(n)      ║ O(n²)     ║ O(n²)     ║ O(1)        ║
║ Merge Sort     ║ O(n log n)║ O(n log n)║ O(n log n)║ O(n)        ║
║ Quick Sort     ║ O(n log n)║ O(n log n)║ O(n²)     ║ O(log n)    ║
║ Heap Sort      ║ O(n log n)║ O(n log n)║ O(n log n)║ O(1)        ║
║ Counting Sort  ║ O(n + k)  ║ O(n + k)  ║ O(n + k)  ║ O(k)        ║
║ Radix Sort     ║ O(nk)     ║ O(nk)     ║ O(nk)     ║ O(n + k)    ║
╚════════════════╩═══════════╩═══════════╩═══════════╩═════════════╝

k = range of input values (for counting/radix sort)
```

---

## 🔢 Mathematical Foundations

### Logarithm Basics (for log n understanding)

```
WHAT IS log₂(n)?
"How many times can you divide n by 2 until you reach 1?"

log₂(8) = 3   because 8 → 4 → 2 → 1  (3 divisions)
log₂(16) = 4  because 16 → 8 → 4 → 2 → 1  (4 divisions)
log₂(1024) = 10

USEFUL TO REMEMBER:
log₂(1,000) ≈ 10
log₂(1,000,000) ≈ 20
log₂(1,000,000,000) ≈ 30
```

### Summation Formulas

```
1 + 2 + 3 + ... + n = n(n+1)/2 ≈ O(n²)
   └── Used in: nested loops where j goes from 0 to i

1 + 2 + 4 + ... + 2ⁿ = 2ⁿ⁺¹ - 1 ≈ O(2ⁿ)
   └── Used in: exponential recursion

1 + 1/2 + 1/4 + ... = 2 ≈ O(1)
   └── Used in: geometric series that converge
```

### Recurrence Relations

```
COMMON RECURRENCES AND THEIR SOLUTIONS:

T(n) = T(n-1) + O(1)      → O(n)         Linear recursion
T(n) = T(n-1) + O(n)      → O(n²)        Like selection sort
T(n) = T(n/2) + O(1)      → O(log n)     Binary search
T(n) = T(n/2) + O(n)      → O(n)         Like finding median
T(n) = 2T(n/2) + O(1)     → O(n)         Tree traversal
T(n) = 2T(n/2) + O(n)     → O(n log n)   Merge sort
T(n) = 2T(n-1) + O(1)     → O(2ⁿ)        Fibonacci naive
```

---

## 🧪 Practice Problems by Complexity

### O(1) Problems
- Check if a number is even/odd
- Swap two variables
- Access array element by index

### O(log n) Problems
- Binary search in sorted array
- Find first/last occurrence
- Search in rotated sorted array
- Find peak element

### O(n) Problems
- Find maximum/minimum in array
- Reverse an array
- Two Sum with hash map
- Valid parentheses (with stack)

### O(n log n) Problems
- Sort an array
- Find kth largest element
- Merge intervals
- Meeting rooms problem

### O(n²) Problems
- Two Sum brute force
- Bubble/Selection/Insertion sort
- Find all pairs with given sum
- Check if array has duplicates (brute force)

---

## Further Reading

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Visualizing Algorithms](https://visualgo.net/)
- [MIT OpenCourseWare - Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/)

---

**Last Updated:** January 30, 2026
