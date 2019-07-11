'''
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n%3==0:
            n=n/3
        return n==1
# Runtime: 212 ms, faster than 36.34% of Python online submissions for Power of Three.
# Memory Usage: 10.7 MB, less than 69.31% of Python online submissions for Power of Three.
        
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
# Runtime: 84 ms, faster than 89.13% of Python3 online submissions for Power of Three.
# Memory Usage: 13.3 MB, less than 38.66% of Python3 online submissions for Power of Three.
