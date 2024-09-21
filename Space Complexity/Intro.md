
# Space Complexity Cheat Sheet: Practical Examples and Shortcuts

## Introduction

This guide will help you find the **space complexity** of any function using practical code examples and simple shortcuts. Comments inside the code will guide you on how to analyze space complexity efficiently.

---

## Example 1: Simple Calculation (Constant Space)

```python
def add_numbers(a, b):
    result = a + b  # Only one variable `result` → O(1)
    return result
```

### Shortcut:
- If you only use a **fixed number of variables**, the space complexity is **O(1)**, no matter the size of the input.

---

## Example 2: Iterating Over a List (Constant Space)

```python
def sum_list(nums):
    total = 0  # Single variable `total` → O(1)
    for num in nums:
        total += num  # No new variables are introduced in each iteration
    return total
```

### Shortcut:
- Loops that **don’t introduce new data structures** (e.g., lists or arrays) don’t affect space complexity. Hence, it's **O(1)**.

---

## Example 3: Storing Results in a List (Linear Space)

```python
def square_elements(nums):
    result = []  # List to store results → O(N) because list grows with input
    for num in nums:
        result.append(num * num)  # Appending `N` elements
    return result
```

### Shortcut:
- **Creating a new list** or **data structure** that grows with input size (`N`) means space complexity is **O(N)**.

---

## Example 4: Recursive Factorial (Linear Space due to Recursion)

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)  # Each recursive call adds a new frame to the stack → O(N)
```

### Shortcut:
- Recursive functions consume space in the **call stack**. The space complexity depends on the **depth of recursion**.
- Here, recursion depth is `N`, so space complexity is **O(N)**.

---

## Example 5: Tail-Recursive Factorial (Optimized to Constant Space)

```python
def tail_recursive_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_recursive_factorial(n-1, n*acc)  # Tail recursion → O(1)
```

### Shortcut:
- **Tail recursion** can be optimized by the compiler to reuse the same stack frame, giving **O(1)** space.

---

## Example 6: Creating a 2D Matrix (Quadratic Space)

```python
def create_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]  # Matrix of size NxM → O(N * M)
    return matrix
```

### Shortcut:
- Nested data structures, like 2D arrays, take space proportional to their size. A matrix with `N` rows and `M` columns uses **O(N * M)** space.

---

## Example 7: Dictionary (HashMap) to Count Occurrences (Linear Space)

```python
def count_occurrences(nums):
    counts = {}  # Dictionary to store counts → O(N)
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts
```

### Shortcut:
- **Dictionaries** (hashmaps) scale with input size. If there are `N` unique elements, space complexity is **O(N)**.

---

## Example 8: Recursive Fibonacci (Inefficient)

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Each call creates two more calls → O(N) stack depth
```

### Shortcut:
- Even though Fibonacci recursion generates many calls, the **call stack depth** is what matters. Here, it's **O(N)**.

---

## Example 9: Dynamic Programming Fibonacci (Efficient)

```python
def fibonacci_dp(n):
    fib = [0, 1]  # List of size N+1 → O(N) space
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
```

### Shortcut:
- Storing results in a list for **dynamic programming** requires space proportional to the input size → **O(N)**.

---

## Example 10: Optimized Fibonacci (Constant Space)

```python
def fibonacci_optimized(n):
    a, b = 0, 1  # Only two variables → O(1) space
    for _ in range(2, n+1):
        a, b = b, a + b  # Reuse `a` and `b` → No additional space used
    return b
```

### Shortcut:
- **Constant space optimization**: By reusing variables instead of storing a list, we reduce space complexity to **O(1)**.

---

## Practical Tips

1. **Watch for Recursive Functions:**
   - Every recursive call uses stack space. Look for ways to replace recursion with iteration or optimize with tail recursion to reduce space complexity.

2. **Data Structures:**
   - Lists, dictionaries, and arrays can increase space complexity if they grow with input size. Be cautious when adding new elements.

3. **Avoid Redundant Copies:**
   - If you’re making multiple copies of a list or array in your code, you’re increasing space complexity unnecessarily. Use **in-place modifications** when possible.

4. **Reuse Variables:**
   - If you can compute results using a few variables (like in the optimized Fibonacci example), you can often reduce space to **O(1)**.

---

## Common Scenarios and Quick Rules

- **Fixed number of variables → O(1)**  
  _Example: Simple assignments, constant loops._
  
- **Arrays, lists, dictionaries that grow with input → O(N)**  
  _Example: Storing results, dynamic programming tables._

- **Recursive function calls → O(N)**  
  _Example: Recursion depth determines the stack usage._

- **Nested structures (e.g., 2D arrays) → O(N * M)**  
  _Example: Storing a matrix or grid._

-
