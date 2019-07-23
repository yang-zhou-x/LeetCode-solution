'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def f(s='',l=0,r=0):
            if len(s)==n*2:
                ans.append(s)
                return
            if l<n:
                f(s+'(',l+1,r)
            if r<l:
                f(s+')',l,r+1)
        f()
        return ans 
# Runtime: 36 ms, faster than 99.65% of Python3 online submissions for Generate Parentheses.

# 20190723
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def helper(path, left, right):
            if len(path) == n * 2:
                ans.append(path)
            if left < n:
                helper(path + '(', left + 1, right)
            if right < left:
                helper(path + ')', left, right + 1)
        helper('', 0, 0)
        return ans
# Runtime: 40 ms, faster than 79.33% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.1 MB, less than 5.01% of Python3 online submissions for Generate Parentheses.
