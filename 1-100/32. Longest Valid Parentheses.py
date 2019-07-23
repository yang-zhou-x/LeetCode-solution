'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()  # 最近'('的索引
                    # 当前位置的值 = '('前紧邻的合格字串长度 + 当前合格的字串长度
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)
# Runtime: 44 ms, faster than 99.39% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 13.7 MB, less than 42.67% of Python3 online submissions for Longest Valid Parentheses.

# 20190723
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * (len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    pos = stack.pop()  # 在当前位置之前，最近的一个'('
                    # 当前位置 = pos之前的长度 + 当前段的长度
                    dp[i + 1] = dp[pos] + i - pos + 1
        return max(dp)
# Runtime: 48 ms, faster than 85.95% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.3 MB, less than 7.51% of Python3 online submissions for Longest Valid Parentheses.
