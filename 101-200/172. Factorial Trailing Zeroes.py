class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        a=5  # 有5时才有0
        while n//a>0:
            ans+=n//a
            a*=5  # 25、125...时，多加1个0
        return ans
        
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Factorial Trailing Zeroes.
# Memory Usage: 10.7 MB, less than 68.75% of Python online submissions for Factorial Trailing Zeroes.
