# Time Complexity in Python: A Detailed Explanation with Examples

**Time complexity** is a way to describe how the runtime of an algorithm changes as the size of the input increases. It's a critical concept in understanding the efficiency of algorithms. The time complexity is often expressed using "Big O" notation, which provides an upper limit on the growth rate of the runtime.

---

## Big O Notation

Here are some common time complexities:

- **O(1)**: Constant time.
- **O(log n)**: Logarithmic time.
- **O(n)**: Linear time.
- **O(n log n)**: Log-linear time.
- **O(n²)**: Quadratic time.
- **O(2^n)**: Exponential time.
- **O(n!)**: Factorial time.

---

### 1. **O(1) - Constant Time**

An algorithm with constant time complexity takes the same amount of time to execute, regardless of the input size.

#### Example:
```python
def constant_function(items):
    return items[0]

my_list = [1, 2, 3, 4, 5]
print(constant_function(my_list))  # Always runs in O(1)
```
Here, the function only accesses the first element, so its runtime doesn't change no matter how big the list is.

**Tip:** If an operation doesn't depend on the size of the input, it's O(1).

---

### 2. **O(log n) - Logarithmic Time**

Algorithms that halve the input size at each step, such as binary search, have logarithmic time complexity.

#### Example:
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # O(log n) search
```
With each iteration, the size of the search space is halved, leading to logarithmic time complexity.

**Shortcut to Remember:** "Cutting in half repeatedly is O(log n)."

---

### 3. **O(n) - Linear Time**

An algorithm with linear time complexity will increase proportionally with the size of the input.

#### Example:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # O(n) search
```
Here, the time taken increases directly with the size of the list.

**Tip:** If you need to look at every element once, the time complexity is O(n).

---

### 4. **O(n log n) - Log-Linear Time**

Algorithms like Merge Sort and Quick Sort have O(n log n) complexity, where the input size is divided, and each division is processed linearly.

#### Example:
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [3, 1, 4, 1, 5, 9]
print(merge_sort(arr))  # O(n log n)
```
This is typical for efficient sorting algorithms, where we need to divide the input into smaller pieces (log n divisions) and process them linearly (n times).

---

### 5. **O(n²) - Quadratic Time**

Algorithms with quadratic time complexity often involve nested loops, where every element is compared to every other element.

#### Example:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 1, 4, 2, 8]
print(bubble_sort(arr))  # O(n²)
```
As the input size grows, the number of operations increases quadratically.

**Tip:** If you see nested loops, it’s likely O(n²).

---

### 6. **O(2^n) - Exponential Time**

Algorithms with exponential time complexity double their runtime with each additional input element. Recursive algorithms, such as the recursive Fibonacci sequence, often have exponential time complexity.

#### Example:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # O(2^n)
```
For each call to the function, two new calls are made, leading to exponential growth.

---

### 7. **O(n!) - Factorial Time**

Factorial time complexity occurs in algorithms that generate all permutations of a set, for example.

#### Example:
```python
import itertools

def generate_permutations(arr):
    return list(itertools.permutations(arr))

arr = [1, 2, 3]
print(generate_permutations(arr))  # O(n!)
```
As the number of items increases, the number of permutations grows factorially.

---

## Summary of Common Time Complexities:

| Time Complexity | Example Code       | Common Scenarios          |
|-----------------|--------------------|---------------------------|
| **O(1)**        | Accessing an array element | Constant-time lookup |
| **O(log n)**    | Binary search       | Divide and conquer       |
| **O(n)**        | Linear search       | Scanning an array         |
| **O(n log n)**  | Merge sort, Quick sort | Efficient sorting     |
| **O(n²)**       | Bubble sort         | Nested loops              |
| **O(2^n)**      | Recursive Fibonacci | Exponential growth        |
| **O(n!)**       | Permutations        | Generating combinations   |

---

## Tips & Tricks:

1. **Nested loops?** Think **O(n²)**.
2. **Cutting the problem in half?** It's likely **O(log n)**.
3. **Multiple recursive calls?** It might be **O(2^n)**.
4. **Sorting algorithms** like merge sort are usually **O(n log n)**.

---

### Shortcut to Estimate Time Complexity:

- **Single for-loop** = O(n)
- **Two nested loops** = O(n²)
- **Halving the input** = O(log n)
- **Divide and conquer** = O(n log n)

