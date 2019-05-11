'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        prev = 2
        curr = 3
        while n > 3:  # f(n) = f(n-1) + f(n-2), 即斐波那契数列
            tmp = prev
            prev = curr
            curr += tmp
            n -= 1
        return curr
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Climbing Stairs.
# Memory Usage: 10.9 MB, less than 15.22% of Python online submissions for Climbing Stairs.

# 排列组合法，速度慢一点
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n2 = n//2
        ans = 0
        for nn in range(1,n2+1):
            ans+=math.factorial(n-2*nn+nn) // (math.factorial(nn) * math.factorial(n-2*nn))
        return ans+1
        
