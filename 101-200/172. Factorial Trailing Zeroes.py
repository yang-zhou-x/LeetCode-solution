'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        base = 5  # 有5时才有0
        while n // base > 0:
            ans += n // base
            base *= 5  # 25、125...时，多加1个0
        return ans
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Factorial Trailing Zeroes.
# Memory Usage: 10.7 MB, less than 68.75% of Python online submissions for Factorial Trailing Zeroes.
