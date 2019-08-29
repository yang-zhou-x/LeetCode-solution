'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x*self.myPow(x,n-1)
        else:
            return self.myPow(x*x,n/2)
# Runtime: 20 ms, faster than 96.13% of Python online submissions for Pow(x, n).
# Memory Usage: 10.8 MB, less than 38.57% of Python online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:  # n为奇数
            return x * self.myPow(x, n - 1)
        else:  # n为偶数
            return self.myPow(x * x, n / 2)
# Runtime: 32 ms, faster than 92.02% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.9 MB, less than 6.90% of Python3 online submissions for Pow(x, n).
