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
        
