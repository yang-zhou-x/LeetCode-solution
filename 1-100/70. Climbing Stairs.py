class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n
        prev=2
        curr=3
        while n>3: # 斐波那契数列
            tmp=prev
            prev=curr
            curr+=tmp
            n-=1
        return curr
            
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Climbing Stairs.
# Memory Usage: 10.9 MB, less than 15.22% of Python online submissions for Climbing Stairs.

# 另一种方法，排列组合，速度慢一点
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n2=n//2
        ans=0
        for nn in range(1,n2+1):
            ans+=math.factorial(n-2*nn+nn)//(math.factorial(nn)*math.factorial(n-2*nn))
        return ans+1
        
