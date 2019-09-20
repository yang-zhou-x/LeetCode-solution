'''
Given a positive integer n, break it into the sum of at least two positive integers 
and maximize the product of those integers. Return the maximum product you can get.

Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 0:
            return int(3 ** (n/3))
        elif n % 3 == 1:
            return int(3 ** ((n-4)/3) * 2 * 2)
        elif n % 3 == 2:
            return int(3 ** ((n - 2) / 3) * 2)
# Runtime: 32 ms, faster than 95.12% of Python3 online submissions for Integer Break.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Integer Break.
