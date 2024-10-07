'''
link :- https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&sortBy=submissions
'''

'''
Missing in Array
Difficulty: EasyAccuracy: 29.59%Submissions: 1.2MPoints: 2
Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive), find the missing element. The array is a permutation of size n with one element missing. Return the missing element.

Examples:

Input: n = 5, arr[] = [1,2,3,5]
Output: 4
Explanation : All the numbers from 1 to 5 are present except 4.
Input: n = 2, arr[] = [1]
Output: 2
Explanation : All the numbers from 1 to 2 are present except 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ n

'''
# solve using formula of 
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        x = n *(n+1)/2
        # code here
        z = sum(arr)
        return int(x-z)
