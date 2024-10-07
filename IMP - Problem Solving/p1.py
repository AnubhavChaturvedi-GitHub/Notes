'''
question link :- https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Strings&sortBy=submissions
'''
'''
Parenthesis Checker
Difficulty: EasyAccuracy: 28.56%Submissions: 609K+Points: 2
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

Examples :

Input: {([])}
Output: true
Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.
Input: ()
Output: true
Explanation: (). Same bracket can form balanced pairs,and here only 1 type of bracket is present and in balanced way.
Input: ([]
Output: false
Explanation: ([]. Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.
Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 105
'''
# Using stack we can so it
# Solution

#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        k = ['(','{','[']
        z = []
        for i in x:
            if i in k:
                z.append(i)
            elif i == ')' and len(z)>0 and z[-1] == '(':
                z.pop()
            elif i == '}' and len(z)>0 and z[-1] == '{':
                z.pop()
            elif i == ']' and len(z)>0 and z[-1] == '[':
                z.pop()
            else:
                return False
        if len(z) == 0:
            return True
        else :
            return False
