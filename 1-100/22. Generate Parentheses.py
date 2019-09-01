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
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def back_track(left, right, path):
            if len(path) == n * 2:
                ans.append(path)
            else:
                if left < n:
                    back_track(left + 1, right, path + '(')
                if right < left:
                    back_track(left, right + 1, path + ')')
        back_track(0, 0, '')
        return ans
# Runtime: 36 ms, faster than 93.63% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.2 MB, less than 5.01% of Python3 online submissions for Generate Parentheses.
