'''
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n / 2 > 1:
            n /= 2
        return n == 1 or n == 2
# Runtime: 40 ms, faster than 56.07% of Python3 online submissions for Power of Two.
# Memory Usage: 13.3 MB, less than 24.44% of Python3 online submissions for Power of Two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
# Runtime: 36 ms, faster than 79.58% of Python3 online submissions for Power of Two.
# Memory Usage: 13.3 MB, less than 26.24% of Python3 online submissions for Power of Two.
